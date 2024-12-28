from course import Course
from student import Student
from major import Major
from constants import *
from chat import chat_decision, chat_with_model
import random
import os


courses = []
majors = []


def random_allocation(size, sum=DEFUALT_TOTAL_COINS, order=0):
    if size <= 1:
        return [sum]

    allocation = []
    current_sum = 0
    for i in range(size - 1):
        rand = random.randint(0, sum - current_sum)
        allocation.append(rand)
        current_sum += rand
    allocation.append(sum - current_sum)
    if order == 1:
        allocation.sort()
    elif order == -1:
        allocation.sort(reverse=True)
    return allocation


def add_slight_noise(allocation, max_noise=-1):
    if max_noise == -1:
        max_noise = min(allocation)
    if max_noise <= 0:
        return allocation.copy()

    result = allocation.copy()

    for i in range(len(allocation) - 1):
        if random.randint(0, 1) == 0:
            continue
        ub = min(
            result[i],
            result[i + 1],
            abs(result[i] - result[i + 1]),
            max_noise,
        )
        noise = random.randint(-ub, ub)
        result[i] += noise
        result[i + 1] -= noise

    return result


def create_prompt(major: Major):
    prompt = "I'm a college student. " + COURSE_SELECTION_RULE
    prompt += "Now I wish to choose the following courses:\n"
    courses_needed_str = ""
    courses_occupied_capacity = []

    sorted_courses = sorted(
        major.courses, key=lambda course: course.get_occupied_capacity(), reverse=True
    )

    i = 1
    for course in sorted_courses:
        prompt += str(i) + ". " + course.name
        courses_needed_str += str(i) + ". " + course.name + " "
        occupied_capacity = course.get_occupied_capacity()
        courses_occupied_capacity.append(occupied_capacity)
        prompt += (
            ": limited to "
            + str(course.limit)
            + " people, and "
            + str(course.cur_num)
            + " people have chosen it ("
            + format(occupied_capacity, ".2f")
            + "%).\n"
        )
        i += 1
    prompt += (
        "Like other students, I also have "
        + str(major.total_coins)
        + " coins all together, how should I allocate them?\n"
    )
    prompt += (
        "There are different ways to allocate the "
        + str(major.total_coins)
        + " coins by different strategies, here are some examples (in the same order, "
    )
    prompt += courses_needed_str + "): \n"
    prompt += (
        str(random_allocation(len(courses_occupied_capacity), major.total_coins)) + ", "
    )
    prompt += (
        str(
            random_allocation(
                len(courses_occupied_capacity), major.total_coins, order=1
            )
        )
        + ", "
    )
    prompt += (
        str(
            random_allocation(
                len(courses_occupied_capacity), major.total_coins, order=-1
            )
        )
        + "......"
    )

    prompt += NOTE
    prompt += (
        "("
        + courses_needed_str
        + ", this is important for me to parse your answer) at the end clearly wrapped in square brackets."
    )

    return prompt, sorted_courses


def get_allocation(prompt, iter, model="llama3.1", num_predict=700):
    if iter > MAX_RETRY:
        return [], ""
    try:
        response = chat_with_model(prompt, model="llama3.1", num_predict=num_predict)
        json_str = chat_decision(response, num_predict=70)
        allocation = eval(json_str).get("coins allocated")
        return allocation, response
    except:
        return get_allocation(
            prompt, iter + 1, model="llama3.1", num_predict=num_predict
        )


def main(display_setup=False):
    with open("setup.json") as f:
        data = f.read()
    setup = eval(data)

    if display_setup:
        print("Courses: ")
    i = 0
    for course in setup["courses"]:
        courses.append(
            Course(i, course["name"], course["limit"], course.get("init_num", 0))
        )
        if display_setup:
            print(courses[i])
        i += 1

    if display_setup:
        print("\nStudents: ")
    i = 0
    for major in setup["majors"]:
        majors.append(
            Major(
                i,
                major["num"],
                [courses[j] for j in major["courses"]],
                major.get("coins", DEFUALT_TOTAL_COINS),
            )
        )
        if display_setup:
            print(majors[i])
        i += 1

    print()
    dialogue_path = os.path.join(SAVE_PATH, DIALOGUE_PATH)
    allocation_path = os.path.join(SAVE_PATH, ALLOCATION_PATH)

    if not os.path.exists(dialogue_path):
        os.makedirs(dialogue_path)

    if not os.path.exists(allocation_path):
        os.makedirs(allocation_path)

    for epi in range(EPISODES):
        print("Episode " + str(epi) + " started")
        for major in majors:
            separate_num = random_allocation(STRATEGY_EACH_MAJOR, major.num)
            start_idx = 0

            for num in separate_num:
                prompt, sorted_courses = create_prompt(major)
                allocation, response = get_allocation(prompt, 1)

                if len(allocation) == 0:
                    print(
                        "Failed to get allocation at episode "
                        + str(epi)
                        + " for major "
                        + str(major.id)
                    )
                    allocation = random_allocation(
                        len(sorted_courses), major.total_coins
                    )

                if sum(allocation) != major.total_coins or len(allocation) != len(
                    sorted_courses
                ):
                    for i in range(len(allocation)):
                        allocation[i] = int(
                            major.total_coins * allocation[i] / sum(allocation)
                        )

                with open(
                    os.path.join(
                        allocation_path, str(major.id) + "_" + str(epi) + ".md"
                    ),
                    "w",
                ) as f:
                    for i in range(num):
                        allocation_with_noise = add_slight_noise(allocation, MAX_NOISE)

                        f.write("student " + str(start_idx + i) + ": ")
                        f.write(str(allocation_with_noise) + "\n")

                        for j in range(len(allocation_with_noise)):
                            if allocation_with_noise[j] == 0:
                                continue
                            student = major.students[start_idx + i]
                            course = sorted_courses[j]
                            course.add_student(student, allocation_with_noise[j])

                start_idx += num

                with open(
                    os.path.join(dialogue_path, str(major.id) + "_" + str(epi) + ".md"),
                    "w",
                ) as f:
                    f.write("## Prompt\n")
                    f.write(prompt)
                    f.write("\n## Response\n")
                    f.write(response)
                    f.write("\n## Courses:\n")
                    for course in sorted_courses:
                        f.write(
                            str(course) + ", minimum coins to enroll if ended now: "
                        )
                        f.write(str(course.minimum_coins_to_enroll()) + "\n")


if __name__ == "__main__":
    main(display_setup=True)
