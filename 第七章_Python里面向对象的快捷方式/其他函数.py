list_one = [1,3,2]

print(sorted(list_one))

def min_max_indexes(seq):
    minimum = min(enumerate(seq), key=lambda s: s[1])
    maximum = max(enumerate(seq), key=lambda s: s[1])
    return minimum[0], maximum[0]

print(min_max_indexes(list_one))

# all, any
# eval, exec, compile
# hasattr, getattr, setattr, delattr