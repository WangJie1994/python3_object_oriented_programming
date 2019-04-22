normal_list = [1, 2, 3, 4, 5]

for i in reversed(normal_list):
    print(i)

class CustomSequence():
    def __len__(self):
        return 5

    def __getitem__(self, item):
        return "x{0}".format(item)


class FunkyBackwards(CustomSequence):
    def __reversed__(self):
        return "BACKWARDS"

for seq in normal_list, CustomSequence(), FunkyBackwards():
    print("\n{}: ".format(seq.__class__.__name__), end="")
    for item in reversed(seq):
        print(item, end=", ")
