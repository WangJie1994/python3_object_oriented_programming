class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(self, name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(street, city, state, code)
        self.phone = phone


# another example

# class BaseClass:
#     num_base_calls = 0
#
#     def call_me(self):
#         print("call method on base class")
#         self.num_base_calls += 1
#
#
# class Left_Subclass(BaseClass):
#     num_left_calls = 0
#
#     def call_me(self):
#         BaseClass.call_me(self)
#         print("call method on left subclass")
#         self.num_left_calls += 1
#
#
# class Right_Subclass(BaseClass):
#     num_right_calls = 0
#
#     def call_me(self):
#         BaseClass.call_me(self)
#         print("call method on right subclass")
#         self.num_right_calls += 1
#
#
# class Subclass(Left_Subclass, Right_Subclass):
#     num_sub_calls = 0
#
#     def call_me(self):
#         Left_Subclass.call_me(self)
#         Right_Subclass.call_me(self)
#         print("call method on subclass")
#         self.num_sub_calls += 1
#
#
# s = Subclass()
# s.call_me()
# print(s.num_base_calls, s.num_left_calls, s.num_right_calls, s.num_sub_calls)


class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print("call method on base class")
        self.num_base_calls += 1


class Left_Subclass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        super().call_me()
        print("call method on left subclass")
        self.num_left_calls += 1


class Right_Subclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        super().call_me()
        print("call method on right subclass")
        self.num_right_calls += 1


class Subclass(Left_Subclass, Right_Subclass):
    num_sub_calls = 0

    def call_me(self):
        super().call_me()
        print("call method on subclass")
        self.num_sub_calls += 1


s = Subclass()
s.call_me()
print(s.num_base_calls, s.num_left_calls, s.num_right_calls, s.num_sub_calls)