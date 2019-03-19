import datetime

last_id = 0


class Note:
    """
    笔记本中的一条笔记对象
    """

    def __init__(self, memo, tags=""):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=""):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        else:
            return False

    def modify_tags(self, note_id, tags):
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        else:
            return False

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]

    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

