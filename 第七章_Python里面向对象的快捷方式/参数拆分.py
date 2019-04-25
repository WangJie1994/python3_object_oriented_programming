def show_args(arg1, arg2, arg3="three"):
    print(arg1, arg2, arg3)


some_args = range(3)
more_args = {
    "arg1": 'one',
    "arg2": 'two'
}

print('unpacking a sequence')
show_args(*some_args)
print('unpacking a dict')
show_args(**more_args)
