data_path = input()
file_name = ''
extension = ''
point_index = 0
slash_index = 0
for index in range((len(data_path) - 1), -1, -1):
    if data_path[index] == '.':
        point_index = index
    elif data_path[index] == '\\':
        slash_index = index
        break

for i in range(point_index + 1, len(data_path), 1):
    extension += data_path[i]
for i in range(point_index - 1, slash_index, -1):
    file_name += data_path[i]

file_name = file_name[::-1]

print(f'File name: {file_name}')
print(f'File extension: {extension}')