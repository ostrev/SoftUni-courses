import math

number_of_students = int(input())
lectures_num = int(input())
additional_bonus = int(input())


total_bonus = 0
max_total = 0
attendance_max = 0
while number_of_students != 0:
    attendance = int(input())
    number_of_students -= 1
    total_bonus = attendance / lectures_num * (5 + additional_bonus)
    if total_bonus > max_total:
        max_total = total_bonus
        attendance_max = attendance

print(f"Max Bonus: {math.ceil(max_total)}.")
print(f"The student has attended {attendance_max} lectures.")