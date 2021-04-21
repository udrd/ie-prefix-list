import csv
import string
from itertools import product


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
# print(reserved_prefixes)

available_prefixes = []
left_side = string.ascii_uppercase
right_side = string.ascii_uppercase + string.digits + '_!-#'

add_available(left_side, right_side, available_prefixes, reserved_prefixes)
add_available('#', right_side[:-1], available_prefixes, reserved_prefixes)

for row in available_prefixes:
    print(row)
