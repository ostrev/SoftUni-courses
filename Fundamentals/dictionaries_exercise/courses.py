command = input()
courses = {}
while command != 'end':
    data = command.split(' : ')
    course_name, student_name = data[0], data[1]
    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)
    command = input()
sorted_courses = sorted(courses.items(), key=lambda x: len(x[1]), reverse=True)

for key, value in sorted_courses:
    print(f'{key}: {len(value)}')
    sort_value = sorted(value)
    for i in range(0, len(value)):
        print(f'-- {sort_value[i]}')
