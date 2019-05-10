import time


def log_calls(func):
    def wrapper(*args, **kwaargs):
        now = time.time()
        print('calling {} with {} and {}'.format(func.__name__, args, kwaargs))
        return_value = func(*args, **kwaargs)
        print('execute {} in {}ms'.format(func.__name__, time.time() - now))
        return return_value

    return wrapper


@log_calls
def test1(a, b, c):
    print("\ttest1 called")


def test2(a, b):
    print("\ttest2 called")


def test3(a, b):
    print("\ttest3 called")
    time.sleep(1)


# test1 = log_calls(test1)
test2 = log_calls(test2)
test3 = log_calls(test3)

test1(1, 2, 3)
test2(4, b=5)
test3(6, 7)
