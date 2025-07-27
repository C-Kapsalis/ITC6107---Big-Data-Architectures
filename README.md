# ITC6107 – Big Data Architectures

**Course:** ITC6107 – Big Data Architectures  

**Institution:** MSc in Data Science, the American College of Greece

**Term:** Winter 2025

---

## Project Description

This project simulates a distributed system for evaluating stock investor portfolios using Apache Kafka, MySQL, Apache Spark, and Python.  
Two stock exchange servers emit daily price updates, while three investor-side apps process these updates and evaluate portfolios.  
A MySQL database collects evaluations, which are analyzed using Spark.

---

## File Structure

```plaintext
.
├── Term Project Description.pdf        # Official project specs and assignment details
├── se1_server.py                       # Stock Exchange Server 1: emits JSON messages with stock prices
├── se2_server.py                       # Stock Exchange Server 2: emits different JSON messages with stock prices
├── server.py                           # Kafka producer code; may serve as controller for the two exchange emitters
├── inv1.py                             # Investor 1: consumes stock data and evaluates portfolios
├── inv2.py                             # Investor 2: same logic, different investor portfolio
├── inv3.py                             # Investor 3: same logic, different investor portfolio
```

---

## Component Explanation

| File             | Description |
|------------------|-------------|
| `se1_server.py`  | Emits simulated stock prices from Exchange Server 1 to Kafka topic `StockExchange` in JSON format. |
| `se2_server.py`  | Emits prices from Exchange Server 2. Designed to simulate asynchronous market activity. |
| `server.py`      | Main Kafka producer logic that initializes and controls the emission process. May orchestrate `se1` and `se2`. |
| `inv1.py`        | Investor Application 1: subscribes to Kafka, processes price feeds, and evaluates its own portfolio. |
| `inv2.py`        | Similar to `inv1.py`, but for a different investor configuration. |
| `inv3.py`        | Third investor-side consumer and evaluation module. |
| `Term Project Description.pdf` | Assignment brief that outlines the full system setup, evaluation logic, and expected outputs. |

---

## Technologies Used

- **Apache Kafka:** A distributed event streaming platform used to build real-time data pipelines. In this project, it handles message publishing and consumption between stock servers and investor apps.
- **Apache Spark:** A powerful engine for large-scale data processing. Used to query and analyze the evaluation data stored in MySQL, providing reports and performance metrics.
- **Python 3:** Main programming language for producers and consumers.
- **MySQL:** A relational database used to store the evaluated portfolio data.
- **JSON Protocols:** Used as the message format exchanged through Kafka for interoperability.

---

## Getting Started

1. Ensure Kafka and MySQL are running locally or via Docker.
2. Launch stock servers (`se1_server.py` and `se2_server.py`) to emit messages.
3. Start investor apps (`inv1.py`, `inv2.py`, `inv3.py`) to consume and evaluate.
4. Optionally, use `server.py` to coordinate or bootstrap startup.
5. Run Spark job (not included in this repo) to produce analytics from the MySQL-stored evaluations.

---

## Notes

- All messages are transmitted in JSON format to the `StockExchange` Kafka topic.
- Portfolio evaluation is saved into a MySQL database, assumed to be pre-configured.
- The architecture mimics real-world financial systems with decoupled producers/consumers.
