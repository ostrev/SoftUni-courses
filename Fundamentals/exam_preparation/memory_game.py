memory = input().split()
command = input()
move = 0
is_win = False
while command != 'end':
    data_indexes = command.split()
    index_one = int(data_indexes[0])
    index_two = int(data_indexes[1])
    move += 1
    if index_one == index_two \
            or index_one >= len(memory) or index_one < 0 \
            or index_two >= len(memory) or index_two < 0:
        middle = int(len(memory)/2)
        element = f'-{move}a'
        memory.insert(middle, element)
        memory.insert(middle, element)
        print("Invalid input! Adding additional elements to the board")
    else:
        if memory[index_one] == memory[index_two]:
            twin = memory[index_one]
            print(f"Congrats! You have found matching elements - {memory[index_one]}!")
            memory.remove(twin)
            memory.remove(twin)
        else:
            print("Try again!")

    if len(memory) == 0:
        is_win = True
        break

    command = input()


if is_win:
    print(f"You have won in {move} turns!")
else:
    print(f"Sorry you lose :(")
    print(f"{' '.join(memory)}")
