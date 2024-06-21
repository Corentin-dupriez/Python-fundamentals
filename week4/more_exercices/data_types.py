def transform_data(data_type, value):
    if data_type == 'int':
        result = int(value) * 2
        print(result)
    elif data_type == 'real':
        result = float(value) * 1.5
        print(f'{result:.2f}')
    elif data_type == 'string':
        print(f'${value}$')


type_of_value = input()
value_to_process = input()

transform_data(type_of_value, value_to_process)