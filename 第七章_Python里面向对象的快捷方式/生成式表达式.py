with open("第七章_Python里面向对象的快捷方式/test_1.txt", "r") as f:
    hellos = (l for l in f if "hello" in l)
    for i in hellos:
        print(i)
