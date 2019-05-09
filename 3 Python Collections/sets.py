set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}
print("set1: {}\nset2: {}".format(set1,set2))

# print("The union of set1 and set2 using \"union\" is: {}".format(set1.union(set2)))
print("The union of set1 and set2 is (everything in both sets): {}".format(set1 | set2))

# print("The difference from set1 to set2 (In set1 but not set2) is: {}".format(set1.difference(set2)))
# print("The difference from set2 to set1 (In set2 but not set1) is: {}".format(set2.difference(set1)))
print("The difference from set1 to set2 (In set1 but not set2) is: {}".format(set1 - set2))
print("The difference from set2 to set1 (In set2 but not set1) is: {}".format(set2 - set1))

# print("Integers unique to each side (in one set but not the other): {}".format(set2.symmetric_difference(set1)))
print("Integers unique to each side (in one set but not the other): {}".format(set1 ^ set2))

# print("The intersection of set1 and set2 is (In both sets): {}".format(set1.intersection(set2)))
print("The intersection of set1 and set2 is (In both sets): {}".format(set1 & set2))


COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers (arg):
    hold = []
    for key, value in COURSES.items():
        if set(arg).issubset(value):
            hold.append(key)
    return print(hold)


def covers_all(topics):
    courses_list = []    
    for course, values in COURSES.items():
        if(values & topics)  == topics:
            courses_list.append(course)
    return print(courses_list)

covers({"Python"})
covers_all({"conditions", "input"})