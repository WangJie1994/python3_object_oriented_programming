from collections import namedtuple

Stock = namedtuple("Stock", "symbol current high low")
stock = Stock("GOOG", 650, high=700, low=600)

print(stock.high)
symbol, current, high, low = stock
print(current)

stock.current = 680