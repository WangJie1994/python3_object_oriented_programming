# class Foo:
#     @property
#     def foo(self):
#         return self._foo
#
#     @foo.setter
#     def foo(self, value):
#         self._foo = value


class Silly:
    @property
    def silly(self):
        "this is silly property"
        print("you are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print("you are making silly {}".format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print("you are delling silly")
        del self._silly


if __name__ == '__main__':
    # foo = Foo()
    # print(foo.foo)
    # foo.foo = 1
    # print(foo.foo)

    s = Silly()
    s.silly = 'funny'
    print(s.silly)
    del s.silly
