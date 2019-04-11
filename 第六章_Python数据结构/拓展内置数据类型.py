class SillyInt(int):
    def __add__(self, other):
        return 0


a = SillyInt(1)
b = SillyInt(2)

print(a + b)

print(dir(list))
print(help(list.__add__))

from collections import KeysView, ValuesView, ItemsView


class DictSorted(dict):
    def __new__(*args, **kwargs):
        new_dict = dict.__new__(*args, **kwargs)
        new_dict.ordered_keys = []
        return new_dict

    def __setitem__(self, key, value):
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        super().__setitem__(key, value)

    def setdefault(self, key, value):
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        return super().setdefault(key, value)

    def keys(self):
        return KeysView(self)

    def values(self):
        return ValuesView(self)

    def items(self):
        return ItemsView(self)

    def __iter__(self):
        return self.ordered_keys.__iter__()

ds = DictSorted()
d = {}
ds['a'] = 1
ds['b'] = 2
ds.setdefault('c', 3)
ds['d'] = 4

d['a'] = 1
d['b'] = 2
d.setdefault('c', 3)
d['d'] = 4

print(ds)
print(d)

from collections import OrderedDict
help(OrderedDict)