stocks = {
    "GOOG": (620, 630, 600),
    "MSFT": (230, 240, 210)
}

print(stocks["GOOG"])
# print(stocks["RIM"])

print(stocks.get("RIM"))
print(stocks.get("RIM", "Not Found"))

print(stocks.setdefault("GOOG", "Invalid"))
print(stocks.setdefault("RIM", (330, 340, 310)))
print(stocks["RIM"])

for stock, values in stocks.items():
    print("{} last value is {}".format(stock, values[0]))

stocks["GOOG"] = (100, 120, 90)
print(stocks["GOOG"])

random_keys = {}
random_keys['astring'] = "somestring"
random_keys[5] = "aninteger"
random_keys[2.5] = "float works too"
random_keys[("abc", 123)] = "so do tuples"

class AnObject:
    def __init__(self, avalue):
        self.avalue = avalue
my_object = AnObject(14)

random_keys[my_object] = "we can store objects"
my_object.avalue = 12

try:
    random_keys[[1,2,3]] = "we can't store list"
except:
    print('unable store list')

for key, value in random_keys.items():
    print("{} has value {}".format(key, value))
