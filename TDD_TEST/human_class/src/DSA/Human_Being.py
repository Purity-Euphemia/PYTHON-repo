class Human_Being:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self, name):
        if isinstance(name, str) and name.strip():
            self._name = name
        else:
            self._name = None

    def get_name(self):
        return self._name

    def set_age(self, age):
        if isinstance(age,int) and age >= 0:
            self._age = age
        else:
            self._age = None

    def get_age(self):
        return self._age