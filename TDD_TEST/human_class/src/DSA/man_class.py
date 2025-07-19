from Human_Being import Human_Being

class Man(Human_Being):
    def speak(self):
        return f"My name is {self.get_name()}, and I am a man"

    def work(self):
        return f"My name is {self.get_name()}, is working as an engineer"

    def walk(self):
        return f"My name is {self.get_name()}, is walking to the park"

    def sleep(self):
        return f"My name is {self.get_name()}, is sleeping"

    def introduce(self):
        return f"Hello, i am {self.get_name()}, a{self.get_age()} years old"