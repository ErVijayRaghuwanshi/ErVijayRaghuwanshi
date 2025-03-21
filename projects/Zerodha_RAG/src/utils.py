import logging
import os
from logging.handlers import RotatingFileHandler


zerodha_examples = [
    ["How do I open an account online with Zerodha?"],
    ["How to log in to the Zerodha Console"],
    ["Is it possible to convert an existing account with another broker to a Zerodha account?"],
    ["What is the procedure to open a minor account online or offline at Zerodha?"],
    ["Where can I find the account opening status once I apply for a Zerodha account online?"],
    ["Why did the account opening process stop stating the IP address is outside India or not detected?"],
    ["My Zerodha account password is not working, how can I reset it"],
    ["How do I withdraw funds from my Zerodha account to my bank account?"],
    ["What are the methods available for adding funds to my Zerodha account?"],
    ["How can I link multiple bank accounts to my Zerodha account?"],
    ["What is the maximum limit for fund transfers from my Zerodha account each day?"],
    ["Why isn't my bank account showing up while trying to add it to my Zerodha account?"],
    ["How long does it usually take for funds added via net banking to reflect in my Zerodha account?"],
    ["What is the minimum amount required for depositing funds into my Zerodha account through UPI?"],
    ["My UPI transfer wasn't successful. What could be the reason?"],
    ["How can I reschedule or edit my recurring payments (like monthly SIP)?"],
    ["Why hasn't my withdrawal request been processed even though it has been several days since I submitted it?"]
]


def get_logger(name, log_level='DEBUG', log_file=None) -> logging.Logger:
    """Create and configure a logger object.
    Args:
        name (str): Name of the logger.
        log_file (str, optional): Path to the log file. Defaults to None.
        log_level (str, optional): Log level (default is 'DEBUG').
    Returns:
        logging.Logger: The configured logger object.
    """

    # Define a dictionary to map log level names to their corresponding integer values
    log_level_dict = {
        'DEBUG':    logging.DEBUG,
        'INFO':     logging.INFO,
        'WARNING':  logging.WARNING,
        'ERROR':    logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }

    # Get or create the logger with the given name
    logger = logging.getLogger(name)

    # Only add handlers to the logger if it doesn't already have any
    if not logger.handlers:
        # Set the logger's log level based on the logLevel argument
        logger.setLevel(log_level_dict.get(log_level, logging.DEBUG))

        # Create a console handler that logs messages with the specified log level
        console = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(levelname)-8s - %(lineno)3d - %(funcName)-18s - %(message)s")
        console.setFormatter(formatter)
        console.setLevel(log_level_dict.get(log_level, logging.DEBUG))

        # Add the console handler to the logger
        logger.addHandler(console)

        # Add the rotating file handler only if log_file is provided
        if log_file:
            # Create the directory for the log file if it doesn't already exist
            os.makedirs(os.path.dirname(log_file), exist_ok=True)

            file_handler = RotatingFileHandler(
                log_file, maxBytes=1024 * 1024 * 2, backupCount=50)
            file_handler.setLevel(log_level_dict.get(log_level, logging.DEBUG))
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    # Return the configured logger
    return logger


from ollama import chat, generate

# llm_model = "gemma3:4b"
llm_model = "llama3.2"

def text_generation(prompt, system_prompt=""):
    stream = generate(
        model='llama3.2',
        prompt = prompt,
        system=system_prompt,
        stream=True)
    return stream