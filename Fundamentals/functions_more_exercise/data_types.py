def data_types(type_d, data_t):
    if type_d == 'int':
        result = int(data_t) * 2
        return result
    elif type_d == 'real':
        result = f'{(float(data_t) * 1.5):.2f}'
        return result
    elif type_d == 'string':
        result = f'${data_t}$'
        return result


type_of_data = input()
data = input()
print(data_types(type_of_data, data))

