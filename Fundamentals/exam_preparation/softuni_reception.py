first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
total_student = int(input())
time = 0
employees_per_hour = first_employee + second_employee + third_employee

while not total_student <= 0:
    time += 1
    total_student = total_student - employees_per_hour
    if time % 4 == 0:
        time += 1

print(f"Time needed: {time}h.")
