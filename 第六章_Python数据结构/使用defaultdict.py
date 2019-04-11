# def letter_frequency(sentence):
#     frequencies = {}
#     for letter in sentence:
#         frequency = frequencies.setdefault(letter, 0)
#         frequencies[letter] = frequency + 1
#     return frequencies


from collections import defaultdict

# def letter_frequency(sentence):
#     frequencies = defaultdict(int)
#     for letter in sentence:
#         frequencies[letter] += 1
#     return frequencies
#
#
# sentence = "hello world hello python"
# print(letter_frequency(sentence))


num_items = 0


def tuple_counter():
    global num_items
    num_items += 1
    return num_items, []


d = defaultdict(tuple_counter)
d['a'][1].append('hello')
d['b'][1].append('world')
print(d)
