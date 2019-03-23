class MySubClass(object):
    pass


class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print("if this were as real system we would send {} order to {}".format(order, self.name))


c = Contact("some body", "somebody@example.com")
s = Supplier("sup", "sup@example.com")

print(c.name, c.email, s.name, s.email)

print(c.all_contacts)
s.order("i need pliers")
print(s.all_contacts)

