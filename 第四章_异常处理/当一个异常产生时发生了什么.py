def no_return():
    print("i am about to raise an exception")
    raise Exception("this is always raised")
    print("this line will never execute")
    return "i won't be returned"


def call_exceptor():
    print("call exceptor starts here...")
    no_return()
    print("an exception was raised...")
    print("... so this line don't run")


if __name__ == '__main__':
    # no_return()
    call_exceptor()
