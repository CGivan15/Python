def num_teachers(dict):
    result = len(dict)
    print("Number of teachers: {}".format(result))
    return


def num_courses(teachers):
    print("Total courses: {}".format(sum(len(v) for v in teachers.values())) )
    return


def courses(teachers):
    output = []
    for courses in teachers.values():
        output +=courses
    print(output)
    return 
    

def most_courses(teachers):
    max_count = 0
    rockstar = ""
    for teacher, course_list in teachers.items():
        if len(course_list) > max_count:
            max_count = len(course_list)
            rockstar = teacher
    print(rockstar)
    return     


def stats(dict):
    outer_list = []
    for key in dict:
        inner_list = []
        inner_list.append(key)
        inner_list.append(len(dict[key]))
        outer_list.append(inner_list)
    print(outer_list)
    return 


teachers = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections', 'Made Up Course']}

num_teachers(teachers)
num_courses(teachers)
courses(teachers)
most_courses(teachers)
stats(teachers)
