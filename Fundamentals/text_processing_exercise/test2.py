command = 'az sym na @Niki@ na #13*'
a = command.find('@')
b = command.find('@', a+1)

print(a)
print(b)