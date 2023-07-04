def loading_bar(num):
    pass
    if num == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    else:
        num = num // 10
        return f'{num *10}% [{"%" * num}{"." * (10-num)}]\nStill loading...'


number = int(input())
print(loading_bar(number))
