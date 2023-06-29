numbers_sequence = [int(num) for num in input().split(', ')]
group = 10
result_list = []
count = 0
while count != len(numbers_sequence):

    for element in numbers_sequence:
        if group - 10 < element <= group:
            result_list.append(element)
            count += 1
    print(f"Group of {group}'s: {result_list}")
    result_list.clear()
    group += 10
