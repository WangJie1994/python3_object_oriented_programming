class OneOnly:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)
        return cls._singleton


if __name__ == '__main__':
    o1 = OneOnly()
    o2 = OneOnly()
    print(o1 == o2)
   