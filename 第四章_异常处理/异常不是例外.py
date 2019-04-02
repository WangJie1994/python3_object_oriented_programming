class Inventory:
    def lock(self, item_type):
        pass
    def unlock(self, item_type):
        pass
    def purchase(self, item_type):
        pass


item_type = 'widget'
inv = Inventory()
inv.lock(item_type)
try:
    num_left = inv.purchase()
except InvalidItemType:
    print("sorry, we don't sell {}".format(item_type))
except OutOfStock:
    print("sorry, the item is out of stock")
else:
    print("purchase complete. there are {} {}s left".format(num_left, item_type))
finally:
    inv.unlock()

