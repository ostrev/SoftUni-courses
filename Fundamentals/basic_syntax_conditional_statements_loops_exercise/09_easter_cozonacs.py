budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
cozoncs_count = 0
price_one_cozonacs = flour_price + eggs_price + milk_price
color_eggs = 0
while True:
    if budget >= price_one_cozonacs:
        budget -= price_one_cozonacs
        cozoncs_count += 1
        color_eggs += 3
        if cozoncs_count % 3 == 0:
            color_eggs = color_eggs - (cozoncs_count - 2)
    else:
        print(f'You made {cozoncs_count} loaves of Easter bread! Now you have {color_eggs} eggs and {budget:.2f}BGN left.')
        break
