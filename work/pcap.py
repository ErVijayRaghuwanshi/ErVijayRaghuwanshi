import os
import time
import threading
import signal
from queue import Queue, Empty
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from joblib import Parallel, delayed

class PcapProcessor:
    """
    Monitors a directory for new .pcap files (using watchdog) and processes
    them concurrently (using joblib). Files are enqueued by the event handler and
    processed in batches by a worker thread.
    """

    def __init__(self, dump_dir, worker_count=4, min_wait_time=5, poll_interval=1):
        self.dump_dir = dump_dir
        self.worker_count = worker_count
        self.min_wait_time = min_wait_time  # seconds to wait for file stability
        self.poll_interval = poll_interval  # seconds between queue polls

        # Global tracking data
        self.host_pairs = set()  # Set of unique (src, dst) tuples
        self.stats = {"processed_files": 0}  # Processed file count

        # Threading and queue
        self.file_queue = Queue()
        self.stop_flag = threading.Event()
        self.observer = None
        self.worker_thread = threading.Thread(target=self._process_queue, daemon=True)

    class PcapHandler(FileSystemEventHandler):
        """Watchdog event handler to add new .pcap files to the queue."""
        def __init__(self, processor):
            self.processor = processor

        def on_created(self, event):
            if event.is_directory or not event.src_path.endswith(".pcap"):
                return
            print(f"New file detected: {event.src_path}")
            self.processor.file_queue.put(event.src_path)

    def is_file_completed(self, file_path):
        """
        Check if a file is no longer being written by comparing its size
        over a fixed interval.
        """
        try:
            initial_size = os.path.getsize(file_path)
            time.sleep(self.min_wait_time)
            return initial_size == os.path.getsize(file_path)
        except OSError:
            # File might have been deleted or inaccessible
            return False

    def extract_host_pairs(self, file_path):
        """
        Use tshark to extract (src, dst) pairs from the pcap file.
        The command outputs two columns: ip.src and ip.dst.
        """
        print(f"Processing file: {file_path}")
        try:
            cmd = f"tshark -r {file_path} -T fields -e ip.src -e ip.dst"
            result = os.popen(cmd).read().strip().split("\n")
            local_pairs = set()
            for line in result:
                parts = line.split("\t")
                if len(parts) == 2:
                    src, dst = parts
                    local_pairs.add((src, dst))
            # Update global tracking data
            self.host_pairs.update(local_pairs)
            self.stats["processed_files"] += 1
            print(f"Processed {file_path}. Stats: {self.stats}, Unique Host Pairs: {len(self.host_pairs)}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    def _process_queue(self):
        """
        Continuously monitor the file queue. When files are available,
        filter out those that are still being written and then process the batch
        in parallel using joblib.
        """
        while not self.stop_flag.is_set():
            tasks = []
            try:
                # Try to collect all files currently in the queue
                while True:
                    file_path = self.file_queue.get_nowait()
                    tasks.append(file_path)
            except Empty:
                pass

            if tasks:
                # Filter out files that are still being written
                tasks = [f for f in tasks if self.is_file_completed(f)]
                if tasks:
                    # Process files concurrently using joblib
                    Parallel(n_jobs=self.worker_count, backend='threading', require='sharedmem')(
                        delayed(self.extract_host_pairs)(file_path) for file_path in tasks)

            time.sleep(self.poll_interval)
        print(self.get_stats)

    def start(self):
        """Starts the watchdog observer and the worker thread."""
        # Enqueue existing .pcap files
        for file_name in os.listdir(self.dump_dir):
            if file_name.endswith(".pcap"):
                file_path = os.path.join(self.dump_dir, file_name)
                print(f"Enqueuing existing file: {file_path}")
                self.file_queue.put(file_path)

        # Set up and start watchdog observer
        self.observer = Observer()
        event_handler = self.PcapHandler(self)
        self.observer.schedule(event_handler, self.dump_dir, recursive=False)
        self.observer.start()
        print("Monitoring started...")

        # Start the worker thread that processes the queue
        self.worker_thread.start()

        try:
            while not self.stop_flag.is_set():
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()


    def stop(self):
        """Stops monitoring and processing gracefully."""
        print("Stopping monitoring and processing...")
        self.stop_flag.set()
        if self.observer:
            self.observer.stop()
            self.observer.join()
        self.worker_thread.join()
        print("Stopped.")

    def get_stats(self):
        """Returns the current processing statistics."""
        return self.stats

    def get_host_pairs(self):
        """Returns the set of unique host pairs extracted so far."""
        return self.host_pairs

# === Example Usage ===
if __name__ == "__main__":
    # Replace with your actual pcap dump directory
    dump_directory = "tmp"
    processor = PcapProcessor(dump_dir=dump_directory, worker_count=4)
    
    # Setup signal handler to gracefully stop on SIGINT
    def signal_handler(sig, frame):
        processor.stop()
        exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    processor.start()

    processor.get_stats
