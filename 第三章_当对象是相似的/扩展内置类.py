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


c1 = Contact("john A", "johna@xxx.com")
c2 = Contact("john B", "johnb@xxx.com")
c3 = Contact("janna C", "jannac@xxx.com")

print([c.name for c in Contact.all_contacts.search("john")])


class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


longkeys = LongNameDict()
longkeys['Hello'] = 1
longkeys['haha'] = 2
longkeys['hello world'] = 3
print(longkeys.longest_key())