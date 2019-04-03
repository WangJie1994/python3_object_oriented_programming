class Silly:
    def _get_silly(self):
        print("you are getting silly")
        return self._silly

    def _set_silly(self, value):
        print("you are making silly {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("you are delling silly")
        del self._silly

    silly = property(_get_silly, _set_silly, _del_silly, "this is a silly property")


if __name__ == '__main__':
    s = Silly()
    s.silly = 'funny'
    print(s.silly)
    del s.silly
