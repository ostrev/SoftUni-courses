first = input()
second = input()
mutate_str = ''
previous_str = first
for i in range(len(first)):
    for j in range(i + 1):
        mutate_str += second[j]
    for k in range(i + 1, len(second)):
        mutate_str += first[k]
    if mutate_str != previous_str:
        print(mutate_str)
    previous_str = mutate_str
    mutate_str = ''
