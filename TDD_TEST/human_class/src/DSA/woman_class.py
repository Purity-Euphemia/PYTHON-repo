from Human_Being import Human_Being

class Woman(Human_Being):
    def speak(self):
        return f"My name is {self.get_name()}, and I am a woman"

    def work(self):
        return f"{self.get_name()}, is working as a doctor"

    def walk(self):
        return f"{self.get_name()}, is walking through the city"

    def sleep(self):
        return f"{self.get_name()}, is getting some sleep"

    def introduce(self):
        return f"Hello, I am {self.get_name()}, a{self.get_age()} years old"