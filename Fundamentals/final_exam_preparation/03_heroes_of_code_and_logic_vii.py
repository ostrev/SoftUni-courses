def cast_spell(heroes_dic, hero_name_cast, mp_need_cast, spell_name_cast):
    if heroes_dic[hero_name_cast]['MP'] >= mp_need_cast:
        heroes_dic[hero_name_cast]['MP'] -= mp_need_cast
        print(f'{hero_name_cast} has successfully cast {spell_name_cast} and now has {heroes_dic[hero_name_cast]["MP"]} MP!')
    else:
        print(f'{hero_name_cast} does not have enough MP to cast {spell_name_cast}!')
    return


def take_damage(heroes_dic, hero_name_take, damage_take, attacker_take):
    if heroes_dic[hero_name_take]['HP'] - damage_take > 0:
        heroes_dic[hero_name_take]['HP'] -= damage_take
        print(f"{hero_name_take} was hit for {damage} HP by {attacker_take} and now has {heroes_dic[hero_name_take]['HP']} HP left!")
    else:
        del heroes_dic[hero_name_take]
        print(f"{hero_name_take} has been killed by {attacker_take}!")
    return


def recharge(heroes_dic, hero_name_re, amount_re):
    if heroes_dic[hero_name_re]['MP'] + amount_re > 200:
        amount_recover = abs(amount_re - ((heroes_dic[hero_name_re]['MP'] + amount_re) - 200))
        heroes_dic[hero_name_re]['MP'] = 200
        print(f"{hero_name_re} recharged for {amount_recover} MP!")
    else:
        heroes_dic[hero_name_re]['MP'] += amount_re
        print(f"{hero_name_re} recharged for {amount_re} MP!")
    return


def heal(heroes_dic, hero_name_he, amount_he):
    if heroes_dic[hero_name_he]['HP'] + amount_he > 100:
        amount_recover = abs(amount_he - ((heroes_dic[hero_name_he]['HP'] + amount_he) - 100))
        heroes_dic[hero_name_he]['HP'] = 100
        print(f"{hero_name_he} healed for {amount_recover} HP!")
    else:
        heroes_dic[hero_name_he]['HP'] += amount_he
        print(f"{hero_name_he} healed for {amount_he} HP!")
    return


number_of_heroes = int(input())
heroes = {}

for _ in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    heroes[hero_name] = {}
    heroes[hero_name]['HP'] = hp
    heroes[hero_name]['MP'] = mp

command = input()
while command != 'End':
    data = command.split(' - ')
    if data[0] == 'CastSpell':
        hero_name, mp_need, spell_name = data[1:]
        mp_need = int(mp_need)
        cast_spell(heroes, hero_name, mp_need, spell_name)
    elif data[0] == 'TakeDamage':
        hero_name, damage, attacker = data[1:]
        damage = int(damage)
        take_damage(heroes, hero_name, damage, attacker)
    elif data[0] == 'Recharge':
        hero_name, amount = data[1:]
        amount = int(amount)
        recharge(heroes, hero_name, amount)
    elif data[0] == 'Heal':
        hero_name, amount = data[1:]
        amount = int(amount)
        heal(heroes, hero_name, amount)
    command = input()

sorted_heroes = sorted(heroes.items(), key=lambda kvpt: (-kvpt[1]['HP'], kvpt[0]))

for k, v in sorted_heroes:
    print(f'{k}')
    print(f'  HP: {v["HP"]}')
    print(f'  MP: {v["MP"]}')



