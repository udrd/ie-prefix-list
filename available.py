import csv
import string


def add_available(a_chars, b_chars, available, reserved):
    for char_1 in a_chars:
        prefix_line = []
        for prefix in [char_1 + char_2 for char_2 in b_chars]:
            if prefix not in reserved:
                prefix_line.append(prefix)
        available.append(char_1 + ": " + " ".join(prefix_line))
    return available


reserved_prefixes = []

with open('table.txt', newline='') as table_file:
    prefix_list = csv.reader(table_file, delimiter='\t')
    for row in prefix_list:
        reserved_prefixes.append(row[0].strip().upper()[:2])


a_chars = string.ascii_uppercase
b_chars_part = {'1': string.ascii_uppercase,
                   '2': string.digits, '3': '_!-#'}
choice = 'not_q'

while(choice != 'q' and choice != 'Q'):
    available_prefixes = []
    b_chars = b_chars_part.get(choice, b_chars_part['1']
                                     + b_chars_part['2'] + b_chars_part['3'])

    add_available(a_chars, b_chars, available_prefixes, reserved_prefixes)
    add_available('#', b_chars.replace('#', ''),
                  available_prefixes, reserved_prefixes)

    for row in available_prefixes:
        print(row)
    choice = input("Enter [1]: letters, [2]: digits, "
                   "[3]: _!-#, [4/other]: all, [q]: quit > ")
