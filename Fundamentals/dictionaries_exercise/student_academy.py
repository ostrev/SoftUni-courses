count = int(input())
grade_dic = {}
for _ in range(count):
    student_name = input()
    student_grade = float(input())

    if student_name not in grade_dic:
        grade_dic[student_name] = []
    grade_dic[student_name].append(student_grade)
filtered_students = {}
for key, value in grade_dic.items():
    average_grade = sum(value) / len(value)
    if average_grade >= 4.5:
        filtered_students[key] = average_grade
sorted_students = sorted(filtered_students.items(), key=lambda kvp: kvp[1], reverse=True)
for student, avr_grade in sorted_students:
    print(f'{student} -> {avr_grade:.2f}')
