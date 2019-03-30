class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("only integers can be added")
        if integer % 2:
            raise ValueError("only even numbers can be added")
        super().append(integer)


if __name__ == '__main__':
    e = EvenOnly()
    e.append("a string")
    e.append(3)
    e.append(2)
