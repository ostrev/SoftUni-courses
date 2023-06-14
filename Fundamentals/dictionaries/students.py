students = input()
courses = {}
while ':' in students:
    name, id, course_name = students.split(':')
    if course_name not in courses:
        courses[course_name] = {}
    courses[course_name][id] = name

    students = input()

search = students.split('_')
searched = ' '.join(search)

for i in courses:
    if i == searched:
        for id, name in courses[i].items():
            print(f'{name} - {id}')


