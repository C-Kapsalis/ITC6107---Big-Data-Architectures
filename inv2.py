from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer('StockExchange',
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

portfolios = {
    "Inv1": {"P11": ["IBM", "AAPL"], "P12": ["VZ", "INTC"]},
    "Inv2": {"P21": ["HPQ", "CSCO"], "P22": ["TXN", "CRM"]},
    "Inv3": {"P31": ["HPQ", "ZM"], "P32": ["VZ", "AVGO"]}
}

def evaluate_portfolio(investor, portfolios):
    for message in consumer:
        stock_data = message.value
        date = stock_data["date"]
        stock_prices = stock_data["stocks"]
        
        for portfolio, stocks in portfolios.items():
            total_value = sum(stock_prices.get(stock, 0) for stock in stocks)
            data = {
                "investor": investor,
                "portfolio": portfolio,
                "date": date,
                "value": total_value
            }
            producer.send('portfolios', value=data)
            print(f"Sent: {data}")

evaluate_portfolio("Inv1", portfolios["Inv1"])
