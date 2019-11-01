
all_students = []
winter_16 = []
spring_16 = []
summer_16 = []
fall_15 = []
ghosts = []

school_info = open("cohort_data.txt")

for item in school_info:
    item = item.rstrip()
    student = item.split("|")
    print(student)
    if student[4] != "I":
        name = student[0] + student[1]
        if student[4] == "G":
            ghosts.append(name)
        elif student[4] == "Winter 2016":
            winter_16.append(name)
        elif student[4] == "Spring 2016":
            spring_16.append(name)
        elif student[4] == "Summer 2016":
            summer_16.append(name)
        elif student[4] == "Fall 2015":
            fall_15.append(name)

print(winter_16)
all_students = [winter_16, spring_16, fall_15, ghosts]

print(all_students)