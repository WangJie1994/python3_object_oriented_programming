class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, other):
        if self.sort_num:
            return self.number < other.number
        return self.string < other.string

    def __repr__(self):
        return "{}:{}".format(self.string, self.number)


if __name__ == '__main__':
    a = WeirdSortee("a", 4, True)
    b = WeirdSortee("b", 3, True)
    c = WeirdSortee("c", 2, True)
    d = WeirdSortee("d", 1, True)

    l = [a, b, c, d]
    print(l)

    l.sort()
    print(l)

    for i in l:
        i.sort_num = False
    l.sort()
    print(l)

    x = [('a', 3), ('b', 2), ('c', 1)]
    x.sort()
    print(x)
    x.sort(key=lambda i: i[1])
    print(x)

    l = ['hello', "HELP", 'hALO']
    l.sort()
    print(l)
    l.sort(key=str.lower)
    print(l)
