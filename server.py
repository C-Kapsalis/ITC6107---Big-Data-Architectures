import socket
import time
import random
import datetime

PORT = 9999

stock = [
    ('IBM', 256.90), ('AAPL', 227.48), ('FB', 597.99), ('AMZN', 194.54),
    ('GOOG', 167.81), ('META', 597.99), ('MSI', 415.67), ('INTC', 19.93),
    ('AMD', 96.63), ('MSFT', 380.16), ('DELL', 90.34), ('ORKL', 148.79),
    ('HPQ', 28.98), ('CSCO', 60.06), ('ZM', 73.47), ('QCOM', 154.98),
    ('ADBE', 435.08), ('VZ', 46.49), ('TXN', 186.49), ('CRM', 272.90),
    ('AVGO', 184.45), ('NVDA', 106.98), ('MSTR', 239.27), ('EBAY', 68.19)
]

ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#ssocket.bind((socket.gethostname(), PORT))
ssocket.bind(('', PORT))
ssocket.listen()
print("Server ready: listening to port {0} for connections.\n".format(PORT))
(c, addr) = ssocket.accept()

for s in stock:
    ticker, price = s
    msg = '{{"TICK": "{0}", "PRICE": "{1:.2f}", "TS": "{2}"}}' \
        .format(ticker, price, datetime.datetime.now())
    print(msg)
    c.send((msg + '\n').encode())

while True:
    time.sleep(random.randint(2, 5))
    sl = random.randint(1, len(stock)) - 1
    ticker, price = stock[sl]
    r = random.random() / 10 - 0.05
    price *= 1 + r
    msg = '{{"TICK": "{0}", "PRICE": "{1:.2f}", "TS": "{2}"}}'\
        .format(ticker, price, datetime.datetime.now())
    print(msg)
    c.send((msg + '\n').encode())

