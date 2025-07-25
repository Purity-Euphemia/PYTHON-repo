class Diary:
    def __init__(self, username: str, password: str):
        self.username = username
        self._password = password
        self._is_locked = True
        self._entries = []

    def is_locked(self) -> bool:
        return self._is_locked

    def unlock(self, password:str) -> bool:
        if password != self._password:
            raise ValueError("Wrong password")
        self._is_locked = False

    def is_empty(self) -> bool:
        return len(self._entries) == 0

    def add_entry(self, title:str, content:str) -> None:
        if self._is_locked:
            raise ValueError("Already locked")
        entry = {"title": title, "content": content}
        self._entries.append(entry)

    def get_entries(self):
        if self._is_locked:
            raise ValueError("Diary is locked")
        return self._entries





