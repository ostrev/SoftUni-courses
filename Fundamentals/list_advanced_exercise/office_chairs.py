numbers_of_room = int(input())
chairs_left = 0
case_two = True
for room_number in range(1, numbers_of_room + 1):
    info_chair_visitor = input().split()
    chair_of_room = len(info_chair_visitor[0])
    visitor_in_room = int(info_chair_visitor[1])

    if chair_of_room < visitor_in_room:
        case_two = False
        print(f"{visitor_in_room - chair_of_room} more chairs needed in room {room_number}")
    else:
        chairs_left += chair_of_room - visitor_in_room

if case_two:
    print(f"Game On, {chairs_left} free chairs left")
