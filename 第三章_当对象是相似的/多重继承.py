class MailSender:
    def send_mail(self, message):
        print("sending {} to {}".format(message, self.email))
        pass


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


class EmailableContact(Contact, MailSender):
    pass


e = EmailableContact("john smith", "john@xxx.com")
print(Contact.all_contacts)
e.send_mail("hello world")


class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code

