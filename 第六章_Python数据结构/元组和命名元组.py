stock = "GOOG", 600, 700, 550
stock = ("GOOG", 600, 700, 550)

import datetime


def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low) / 2), date)

mid_value = middle(("GOOG", 600, 700, 550), datetime.date(2010, 10, 10))
print(mid_value)

print(stock[2])
