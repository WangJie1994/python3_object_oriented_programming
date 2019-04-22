contacts = []
with open("第七章_Python里面向对象的快捷方式/test_2.txt", 'r') as f:
    header = f.readline().strip().split("\t")
    for line in f:
        line = line.strip().split("\t")
        contact_map = zip(header, line)
        contacts.append(dict(contact_map))


for contact in contacts:
    print(("email: {email} -- {last}, {first}".format(**contact)))


list_one = ['a', 'b', 'c']
list_two = ['1', '2', '3']
ziped = zip(list_one, list_two)
ziped = list(ziped)
print(ziped)
unzipped = zip(*ziped)
print(list(unzipped))
