with open('test_all.txt') as file:
    lines = [line.rstrip('\n') for line in file]

length_list = len(lines)
set_list = set(lines)
set_list_length = len(set_list)

print(f"List is {length_list} and has {set_list_length} unique values")
