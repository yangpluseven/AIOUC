DEFUALT_TOTAL_COINS = 100

SAVE_PATH = "./save"

DIALOGUE_PATH = "dialogues"

ALLOCATION_PATH = "allocations"

EPISODES = 5

MAX_RETRY = 3

STRATEGY_EACH_MAJOR = 3

MAX_NOISE = -1

COURSE_SELECTION_RULE: str = (
    """
My university has a course selection system: all students need to pay virtual coins to select courses. Students pay a certain number of coins (which can be 0) for each course they wish to choose according to their own decisions. Each student starts with """
    + str(DEFUALT_TOTAL_COINS)
    + """ coins to use. Each course has a limit on the number of students, and if the actual number of students choosing a course is less than the course limit, then everyone will successfully enroll (even if the student paid 0 coins). If the actual number of students choosing the course exceeds the limit, then all students who chosed that course are sorted by the amount of coins paid, excluding those who paid the least coins, and only retaining the top ones.
For example, if a course is limited to 100 people but 150 people have chosen it, then the bottom 50 in terms of coin payment should be excluded, retaining only 100 people.
"""
)

NOTE: str = (
    """
Note: After my decision, there will be other students selecting courses, which means courses that are not popular now may also have many new people choosing them later. Please, keep the answer simple and short, and do remember to gave out an array of integer reprensenting the coins you want to use on each course in the same order as the courses I provided above """
)

TEST_PROMPT_ONE: str = (
    """
    I am a researcher in the field of human behavior, and I would like you to play a role, think empathetically, consider the thoughts and intellectual level of that role, and make corresponding decisions.
    Assume you are a college student, and your university has a course selection system: all students need to pay virtual coins to select courses. Students pay a certain number of coins (which can be 0) for each course they wish to choose according to their own decisions. Each student starts with 100 coins to use. Each course has a limit on the number of students, and if the actual number of students choosing a course is less than the course limit, then everyone will successfully enroll (even if the student paid 0 coins). If the actual number of students choosing the course exceeds the limit, then all students who paid coins for that course are sorted by the amount of coins paid, excluding those who paid the least coins, and only retaining the top ones.
    For example, if a course is limited to 100 people but 150 people have chosen it, then the bottom 50 in terms of coin payment should be excluded, retaining only 100 people.
    Now, you wish to choose the following courses:
    1. Software Development: limited to 80 people, and 75 people have chosen it (93.75%).
    2. Artificial Intelligence: limited to 50 people, and 100 people have chosen it (200%).
    3. Robotics: limited to 30 people, and 31 people have chosen it (103.33%).
    Like other students, you also have 100 coins all together, how would you allocate them? Note: After your decision, there will be other students selecting courses, which means courses that are not popular now may also have many new people choosing them later. Please, keep the answer simple and short, and do remember to gave out an array of integer reprensenting the coins you want to use on each course in the same order as the courses I provided above (In the order of 1. Software Development, 2. Artificial Intelligence, 3. Robotics, this is important for me to parse your answer) at the end clearly wrapped in square brackets.
    """
)

TEST_PROMPT_TWO: str = (
    """
    You are a college student, and your university has a course selection system: all students need to pay virtual coins to select courses. Students pay a certain number of coins (which can be 0) for each course they wish to choose according to their own decisions. Each student starts with 100 coins to use. Each course has a limit on the number of students, and if the actual number of students choosing a course is less than the course limit, then everyone will successfully enroll (even if the student paid 0 coins). If the actual number of students choosing the course exceeds the limit, then all students who chosed that course are sorted by the amount of coins paid, excluding those who paid the least coins, and only retaining the top ones.
    For example, if a course is limited to 100 people but 150 people have chosen it, then the bottom 50 in terms of coin payment should be excluded, retaining only 100 people.
    Now, you wish to choose the following courses:
    1. Software Development: limited to 80 people, and 75 people have chosen it (93.75%).
    2. Artificial Intelligence: limited to 50 people, and 100 people have chosen it (200%).
    3. Robotics: limited to 30 people, and 31 people have chosen it (103.33%).
    Like other students, you also have 100 coins all together, how would you allocate them? Note: After your decision, there will be other students selecting courses, which means courses that are not popular now may also have many new people choosing them later. Please, keep the answer simple and short, and do remember to gave out an array of integer reprensenting the coins you want to use on each course in the same order as the courses I provided above (In the order of 1. Software Development, 2. Artificial Intelligence, 3. Robotics, this is important for me to parse your answer) at the end clearly wrapped in square brackets.
    """
)

TEST_PROMPT_THREE: str = (
    """
    I'm a college student. My university has a course selection system: all students need to pay virtual coins to select courses. Students pay a certain number of coins (which can be 0) for each course they wish to choose according to their own decisions. Each student starts with 100 coins to use. Each course has a limit on the number of students, and if the actual number of students choosing a course is less than the course limit, then everyone will successfully enroll (even if the student paid 0 coins). If the actual number of students choosing the course exceeds the limit, then all students who chosed that course are sorted by the amount of coins paid, excluding those who paid the least coins, and only retaining the top ones.
    For example, if a course is limited to 100 people but 150 people have chosen it, then the bottom 50 in terms of coin payment should be excluded, retaining only 100 people.
    Now, I wish to choose the following courses:
    1. Software Development: limited to 80 people, and 75 people have chosen it (93.75%).
    2. Artificial Intelligence: limited to 50 people, and 100 people have chosen it (200%).
    3. Robotics: limited to 30 people, and 31 people have chosen it (103.33%).
    Like other students, I also have 100 coins all together, how should I allocate them? Note: After my decision, there will be other students selecting courses, which means courses that are not popular now may also have many new people choosing them later. Please, keep the answer simple and short, and do remember to gave out an array of integer reprensenting the coins you want to use on each course in the same order as the courses I provided above (In the order of 1. Software Development, 2. Artificial Intelligence, 3. Robotics, this is important for me to parse your answer) at the end clearly wrapped in square brackets.
    """
)

TEST_PROMPT_FOUR: str = (
    """
    I'm a college student. My university has a course selection system: all students need to pay virtual coins to select courses. Students pay a certain number of coins (which can be 0) for each course they wish to choose according to their own decisions. Each student starts with 100 coins to use. Each course has a limit on the number of students, and if the actual number of students choosing a course is less than the course limit, then everyone will successfully enroll (even if the student paid 0 coins). If the actual number of students choosing the course exceeds the limit, then all students who chosed that course are sorted by the amount of coins paid, excluding those who paid the least coins, and only retaining the top ones.
    For example, if a course is limited to 100 people but 150 people have chosen it, then the bottom 50 in terms of coin payment should be excluded, retaining only 100 people.
    Now, I wish to choose the following courses:
    1. Software Development: limited to 80 people, and 75 people have chosen it (93.75%).
    2. Artificial Intelligence: limited to 50 people, and 100 people have chosen it (200%).
    3. Robotics: limited to 30 people, and 31 people have chosen it (103.33%).
    Like other students, I also have 100 coins all together. How should I allocate them? 
    There are different ways to allocate the 100 coins, here are some examples (in the same order, 1. Software Development, 2. Artificial Intelligence, 3. Robotics):
    [80, 0, 20], [30, 60, 10], [31, 59, 10], [5, 94, 1].
    Note: After my decision, there will be other students selecting courses, which means courses that are not popular now may also have many new people choosing them later. Please, keep the answer simple and short, and do remember to gave out an array of integer reprensenting the coins you want to use on each course in the same order as the courses I provided above (In the order of 1. Software Development, 2. Artificial Intelligence, 3. Robotics, this is important for me to parse your answer) at the end clearly wrapped in square brackets.
    """
)
