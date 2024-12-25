from constants import *
from student import Student


class Major:
    def __init__(self, id, num, courses=None, coins=DEFUALT_TOTAL_COINS):
        self.id = id
        self.num = num
        self.courses = courses if courses is not None else []
        self.total_coins = coins
        self.students = []
        for i in range(num):
            self.students.append(Student(id * 1000000 +i, self))

    def __str__(self) -> str:
        return f"{self.num} students who need: [{', '.join(c.name for c in self.courses)}]"
