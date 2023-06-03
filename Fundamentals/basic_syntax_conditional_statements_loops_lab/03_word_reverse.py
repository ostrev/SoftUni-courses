word = input()
word_len = len(word)

reverse_word = ''
for i in range(word_len - 1, -1, -1):
    reverse_word += word[i]
print(reverse_word)
