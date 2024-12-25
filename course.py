class Course:

    def __init__(self, code, name, limit, init_num=0):
        self.code = code
        self.name = name
        self.limit = limit
        self.cur_num = init_num
        self.occupied_capacity = 0.0
        self.students = {}

    def __str__(self) -> str:
        return f"{self.name}: {self.cur_num}/{self.limit}"

    def get_occupied_capacity(self):
        self.occupied_capacity = self.cur_num / self.limit * 100.0
        return self.occupied_capacity

    def add_student(self, student, coins):
        if self.students.get(student) is not None:
            if coins == 0:
                self.remove_student(student)
            else:
                self.students[student] = coins
            return
        if coins == 0:
            return
        self.cur_num += 1
        self.students[student] = coins
        
    def remove_student(self, student):
        self.cur_num -= 1
        self.students.pop(student, None)

    def minimum_coins_to_enroll(self):
        if self.cur_num <= self.limit:
            return 0
        coins_list = list(self.students.values())
        coins_list.sort(reverse=True)
        return coins_list[self.limit - 1]
