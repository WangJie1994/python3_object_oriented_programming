import sys
from .notebook import Note, Notebook


class Menu:
    """
    显示一个菜单
    """

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    @staticmethod
    def display_menu():
        print(
            """
            Notebook menu:
            
            1. show all notes
            2. search notes
            3. add note
            4. modify note
            5. quit
            """
        )

    def run(self):
        while True:
            self.display_menu()
            choice = input("enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{} {}\n{}".format(
                note.id, note.tags, note.memo
            ))

    def search_notes(self):
        filter = input("search for: ")
        note = self.notebook.search(filter)
        self.show_notes(note)

    def add_note(self):
        memo = input("enter a memo: ")
        self.notebook.new_note(memo)
        print("your note has been added.")

    def modify_note(self):
        id = input("enter a note id: ")
        memo = input("enter a memo: ")
        tags = input("enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("thank you for using.")
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()
