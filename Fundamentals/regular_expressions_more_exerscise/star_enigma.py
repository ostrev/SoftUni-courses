import re
number_of_message = int(input())
count = 0
decrypt_message = ""
attacked_planets = []
destroyed_planets = []

while number_of_message != 0:
    command = input()
    searched_letters = command.lower()
    count_letters = 0
    # count the letters and decrypt the message
    for letter in searched_letters:
        if letter == 's' or letter == 't' or letter == 'a' or letter == 'r':
            count_letters += 1
    for letter in command:
        decrypt_message += chr(ord(letter) - count_letters)

    pattern = r"@(?P<planet>[A-Za-z]+)([^@!:>-]+)?:(?P<population>\d+)([^@!:>-]+)?!(?P<attack>[AD])!([^@!:>-]+)?->(?P<solders>\d+)"
    matches = re.finditer(pattern, decrypt_message)
    for match in matches:
        attack_type = match.group('attack')
        planet_name = match.group('planet')
        if attack_type == 'A':
            attacked_planets.append(planet_name)
        else:
            destroyed_planets.append(planet_name)
    decrypt_message = ""
    number_of_message -= 1

print(f"Attacked planets: {len(attacked_planets)}")
for planet_a in sorted(attacked_planets):
    print(f"-> {planet_a}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet_d in sorted(destroyed_planets):
    print(f"-> {planet_d}")
