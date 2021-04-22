import csv
import string


def add_available(left_side, right_side, available, reserved):
    for char_1 in left_side:
        prefix_line = []
        for prefix in [char_1 + char_2 for char_2 in right_side]:
            if prefix not in reserved:
                prefix_line.append(prefix)
        available.append(char_1 + ": " + " ".join(prefix_line))
    return available


reserved_prefixes = []

with open('table.txt', newline='') as table_file:
    prefix_list = csv.reader(table_file, delimiter='\t')
    for row in prefix_list:
        reserved_prefixes.append(row[0].strip().upper()[:2])


left_side = string.ascii_uppercase
right_side_part = {'1': string.ascii_uppercase,
                   '2': string.digits, '3': '_!-#'}
choice = 'not_q'

while(choice != 'q' and choice != 'Q'):
    available_prefixes = []
    right_side = right_side_part.get(choice, list_part['1']
                                     + list_part['2'] + list_part['3'])

    add_available(left_side, right_side, available_prefixes, reserved_prefixes)
    add_available('#', right_side.replace('#', ''),
                  available_prefixes, reserved_prefixes)

    for row in available_prefixes:
        print(row)
    choice = input("Enter [1]: letters, [2]: digits, "
                   "[3]: _!-#, [4/other]: all, [q]: quit > ")
