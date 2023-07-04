number = int(input())
pieces = {}

for _ in range(number):
    piece, composer, key = input().split('|')
    pieces[piece] = {}
    pieces[piece]['composer'] = composer
    pieces[piece]['key'] = key


command = input()

while command != 'Stop':
    data = command.split('|')
    if data[0] == 'Add':
        piece = data[1]
        composer = data[2]
        key = data[3]
        if piece not in pieces:
            pieces[piece] = {}
            pieces[piece]['composer'] = composer
            pieces[piece]['key'] = key
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')
    elif data[0] == 'Remove':
        piece = data[1]
        if piece in pieces:
            del pieces[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif data[0] == 'ChangeKey':
        piece = data[1]
        new_key = data[2]
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    command = input()

sort_pieces = sorted(pieces.items(), key=lambda kvpt: kvpt[0])
for piece, value in sort_pieces:
    print(f'{piece} -> Composer: {value["composer"]}, Key: {value["key"]}')