
class Problem:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.is_solved = False

    def solve(self):
        self.is_solved = True

    def __str__(self):
        satus = "Solved" if self.is_solved else "Not solved"
        return f" {self.name} ({self.type.value}) - {satus}"

