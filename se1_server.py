from kafka import KafkaProducer
from datetime import datetime, timedelta
import json
import time

# Setup Kafka Producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Define stocks for each server
stocks_se1 = ["IBM", "AAPL", "FB", "AMZN", "GOOG", "AVGO"]
stocks_se2 = ["VZ", "INTC", "AMD", "MSFT", "DELL", "ORCL"]

def simulate_stock_exchange(server_id, stocks):
    start_date = datetime(2000, 1, 1)
    end_date = datetime(2025, 4, 1)

    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:  # Skip weekends
            stock_prices = {stock: round(100 + 10 * (0.5 - time.time() % 1), 2) for stock in stocks}
            data = {
                "date": current_date.strftime('%Y-%m-%d'),
                "server": server_id,
                "stocks": stock_prices
            }
            producer.send('StockExchange', value=data)
            print(f"Sent: {data}")
            time.sleep(2)  # Simulate daily trading (2 sec per day)
        current_date += timedelta(days=1)

# Run Servers
simulate_stock_exchange("se1", stocks_se1)
simulate_stock_exchange("se2", stocks_se2)
