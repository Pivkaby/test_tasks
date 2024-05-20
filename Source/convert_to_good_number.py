import re

def convert_special_on_good(str_input):
    reg_spec = r'\b(?:\d{2,4}\\\d{2,5})\b'
    new_string = str_input.split()
    for string in new_string:
        special_numbers = re.findall(reg_spec, string)
        for special_number in special_numbers:
            good_numbers = formatting_good(special_number)
            print(good_numbers)
    return good_numbers

def formatting_good(numbers):
    parts = numbers.split('\\')
    good_numbers = parts[0].zfill(4) + '\\' + parts[1].zfill(5)
    return good_numbers

# str_input = r'1\1 11\11 111\111 1111\1111 11111\11111 111111\111111'
str_input = r'Адрес 5467\456. Номер 405\549'
convert_special_on_good(str_input)