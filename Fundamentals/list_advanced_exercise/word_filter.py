text = input().split()
even_word = [s for s in text if len(s) % 2 == 0]
print('\n'.join(even_word))
