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


def funny_division(anumber):
    try:
        return 100 / anumber
    except ZeroDivisionError:
        return "can't divided by zero"


def funny_division2(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 is not a lucky number")
        return 100 / anumber
    except (ZeroDivisionError, TypeError):
        return "enter a number other than zero"


def funny_division3(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 is not a lucky number")
        return 100 / anumber
    except ZeroDivisionError:
        return "enter a number other than zero"
    except TypeError:
        return "enter a numerical value"
    except ValueError:
        print("NO NO NO 13!")
        raise


try:
    raise ValueError("this is an argument")
except ValueError as e:
    print("the arguments are", e.args)

if __name__ == '__main__':
    pass
    # no_return()
    # call_exceptor()

    # try:
    #     no_return()
    # except:
    #     print("i caught an exception")
    # print("execute after the exception")

    # print(funny_division(0))
    # print(funny_division(50.0))
    # print(funny_division("hello"))

    # for val in (0, "hello", 50.0, 13):
    #     print("testing {}".format(val), end=" ")
    #     print(funny_division2(val))

    # for val in (0, "hello", 50.0, 13):
    #     print("testing {}".format(val), end=" ")
    #     print(funny_division3(val))
