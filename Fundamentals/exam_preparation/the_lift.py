people = int(input())
lift_state = [int(s) for s in input().split()]

for index in range(len(lift_state)):
    wagon = lift_state[index]
    free_space_on_wagon = 4 - wagon

    if free_space_on_wagon > people:
        free_space_on_wagon = people

    if free_space_on_wagon > 0:

        lift_state[index] += free_space_on_wagon
        people -= free_space_on_wagon

    if people == 0:
        break

if (len(lift_state) * 4) == sum(lift_state) and people == 0:
    print(' '.join([str(s) for s in lift_state]))
elif (len(lift_state) * 4) == sum(lift_state) and people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(' '.join([str(s) for s in lift_state]))
else:
    print(f"The lift has empty spots!")
    print(' '.join([str(s) for s in lift_state]))

