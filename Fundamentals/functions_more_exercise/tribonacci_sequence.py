def tribonacci(num):
    result = [1, 1, 2]
    last_result = []
    for i in range(3, num):
        sum_tr = result[i - 1] + result[i - 2] + result[i - 3]
        result.append(sum_tr)

    for n in range(0, num):
        last_result.append(result[n])
    last_result = list(map(str, last_result))
    return last_result


number = int(input())
print(' '.join(tribonacci(number)))


