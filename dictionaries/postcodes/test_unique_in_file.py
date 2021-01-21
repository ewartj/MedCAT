with open('all_postcodes.txt') as file:
    lines = [line.rstrip('\n') for line in file]

length_list = len(lines)
set_list = set(lines)
set_list_length = len(set_list)

print(f"List is {length_list} and has {set_list_length} unique values")

unique_list = list(set_list)

with open('final_postcode_list.txt', 'w') as f:
    for i in range(0,len(unique_list)):
        f.write("%s\n" % unique_list[i])

