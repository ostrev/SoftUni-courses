def positive(numb):
    return ', '.join([str(s) for s in numb if s >= 0])


def negative(numb):
    return ', '.join([str(s) for s in numb if s < 0])


def even(numb):
    return ', '.join([str(s) for s in numb if s % 2 == 0])


def odd(numb):
    return ', '.join([str(s) for s in numb if s % 2 != 0])


numbers = [int(number) for number in input().split(', ')]

print(f'Positive: {positive(numbers)}')
print(f'Negative: {negative(numbers)}')
print(f'Even: {even(numbers)}')
print(f'Odd: {odd(numbers)}')
