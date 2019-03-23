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


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


c1 = Contact("john A", "johna@xxx.com")
c2 = Friend("john B", "johnb@xxx.com", "12754231")
c3 = Contact("janna C", "jannac@xxx.com")

print([c.name for c in Contact.all_contacts.search("john")])