# 📡 Reference Architecture for Telecom Data Analytics (LEA)

## 1. **Data Ingestion**

* Sources:

  * **CDR** from telcos (MSISDN, IMEI, IMSI, CellID, timestamps, duration).
  * **IPDR** from ISPs (IP, port, protocol, session times, bytes transferred).
  * **VoIP logs** (SIP/RTCP events, call quality, participants).
* Tools:

  * **Kafka / Flume / NiFi** → streaming ingestion.
  * **HDFS / S3 / Delta Lake** → long-term storage.

---

## 2. **Raw Data Lake (Bronze Layer)**

* Store unprocessed records **as-is** (CSV, Parquet, ORC, JSON).
* Partition by **date/hour/operator** for efficiency.
* Keep **original copies** for auditing (LEA requirement).

---

## 3. **Data Enrichment & Cleansing (Silver Layer)**

**Libraries:**

* 🔠 **spark-daria** / regex UDFs → parse MSISDNs, emails, URIs.
* 🌍 **MaxMind GeoIP** or **ip2location** → enrich IPDR with country/city/ASN.
* 📡 **Apache Sedona / Mosaic** → map CellID → tower → lat/lon.
* 🧹 Normalization:

  * Phone numbers (E.164 format).
  * Timestamps (UTC).
  * Protocol labels (TCP/UDP mappings).

---

## 4. **Feature Engineering & Entity Resolution**

* Map **identities**: MSISDN ↔ IMSI ↔ IMEI ↔ IP ↔ location.
* Build **sessions**:

  * Aggregate per user per time window.
  * Calculate call duration, data volume, handovers.
* Compute features:

  * Call frequency, unique contacts, top destinations.
  * IP session entropy (suspicious browsing patterns).

---

## 5. **Analytics & Intelligence (Gold Layer)**

### A. **Geospatial Analysis**

* Library: **Sedona / Mosaic**
* Example use cases:

  * Suspect location correlation (were two phones near the same tower at the same time?).
  * Hotspot detection (meet-up points, frequent cell tower usage).
  * Mobility patterns (tower sequences → travel routes).

### B. **Social Network / Graph Analysis**

* Library: **GraphFrames / GraphX**
* Build a **who-called-who** graph:

  * Nodes: phone numbers / IPs / accounts.
  * Edges: calls, VoIP sessions, data flows.
* Analytics:

  * **Connected components** → hidden groups.
  * **PageRank** → key influencers.
  * **Shortest paths** → link suspects via intermediaries.

### C. **Anomaly & Fraud Detection**

* Library: **Spark MLlib**
* Use ML for:

  * Outlier detection (sudden burst of calls, mass dialing).
  * SIM box fraud detection.
  * VoIP QoS anomalies (packet loss, jitter).

---

## 6. **Storage & Indexing**

* **Delta Lake** (time travel, ACID compliance).
* **Elasticsearch** / **OpenSearch** for **search queries**:

  * “Show all IP sessions from 10.10.x.x hitting suspicious domains.”
  * “List all calls from MSISDN X near Tower Y on date Z.”

---

## 7. **Visualization & Investigation Dashboards**

* **Kibana / Grafana / Superset** → dashboards for investigators.
* **Geospatial visualizations**:

  * Map of tower hits (Leaflet/Kepler.gl).
  * Heatmaps of suspect movement.
* **Graph visualizations**:

  * Neo4j + Spark connector (for link analysis).

---

# 🔗 Example Flow (Simplified)

```
CDR/IPDR/VoIP Logs  →  Kafka/HDFS (Bronze)
        ↓
     Spark ETL + Sedona + GeoIP (Silver)
        ↓
 Entity Resolution + GraphFrames + MLlib (Gold)
        ↓
 Delta Lake + Elasticsearch + Dashboards
```

---

## ✅ Library Mapping to Workflow

| Stage                  | Libraries                        |
| ---------------------- | -------------------------------- |
| Parsing & Cleansing    | spark-daria, regex, PySpark UDFs |
| IP Geolocation         | MaxMind GeoIP, ip2location       |
| Cell Tower Mapping     | Apache Sedona, Mosaic            |
| Graph / Call Analysis  | GraphFrames, GraphX              |
| ML / Anomaly Detection | Spark MLlib                      |
| Storage & Indexing     | Delta Lake, Elasticsearch        |
| Visualization          | Kibana, Grafana, Neo4j           |

---

