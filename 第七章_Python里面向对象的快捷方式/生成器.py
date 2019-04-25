# method 1
with open("第七章_Python里面向对象的快捷方式/test_1.txt", "r") as f_input:
    with open("第七章_Python里面向对象的快捷方式/test_3.txt", "w") as f_output:
        heos = (l.replace("ll", "") for l in f_input if "hello" in l)
        for i in heos:
            f_output.write(i)


# method 2
class WarningFile:
    def __init__(self, insequence):
        self.insequence = insequence

    def __iter__(self):
        return self

    def __next__(self):
        l = self.insequence.readline()
        while l and 'hello' not in l:
            l = self.insequence.readline()
        if not l:
            raise StopIteration
        return l.replace("ll", "")


with open("第七章_Python里面向对象的快捷方式/test_1.txt", "r") as f_input:
    with open("第七章_Python里面向对象的快捷方式/test_4.txt", "w") as f_output:
        f_filter = WarningFile(f_input)
        for l in f_filter:
            f_output.write(l)


# method 3
def warning_filter(insequence):
    for l in insequence:
        if 'hello' in l:
            yield l.replace("ll", "")


with open("第七章_Python里面向对象的快捷方式/test_1.txt", "r") as f_input:
    with open("第七章_Python里面向对象的快捷方式/test_5.txt", "w") as f_output:
        f_filter = warning_filter(f_input)
        for l in f_filter:
            f_output.write(l)

print(warning_filter([]))
