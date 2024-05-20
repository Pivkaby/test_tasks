def max_concatenated_number(str_list):
    str_list.sort(key=lambda x: x * 3, reverse=True)
    return ''.join(str_list)

input_list = ["11", "234", "005", "87", "8"]
result = max_concatenated_number(input_list)
print(result)