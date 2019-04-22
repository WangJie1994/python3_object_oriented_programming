with open("第七章_Python里面向对象的快捷方式/test_1.txt", "r") as f:
    for index, line in enumerate(f):
        print("{0}: {1}".format(index+1, line), end="")

