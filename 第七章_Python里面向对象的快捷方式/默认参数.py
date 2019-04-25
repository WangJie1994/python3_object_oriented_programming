def default_arguments(x, y, z, a='some string', b=False):
    pass


variable = []
default_arguments("a string", variable, 8, "", True)
default_arguments("a string", variable, 8)
default_arguments("a string", variable, 8, b=True)
default_arguments(y=8, z="a string", x=variable, a="h")

number = 5


def funky_function(number=number):
    print(number)


number = 6
funky_function(8)
funky_function()
print(number)


def hello(b=[]):
    b.append('a')
    print(b)


hello()
hello()
hello([1, 2, 3])
hello()


def hello(b=None):
    if b is None:
        b = []
    b.append('a')
    print(b)


hello()
hello()
hello([1, 2, 3])
hello()
