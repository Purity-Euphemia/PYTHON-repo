from Human_Being import Human_Being

class Man(Human_Being):
    def speak(self):
        return f"My name is {self.get_name()}, and I am a man"
