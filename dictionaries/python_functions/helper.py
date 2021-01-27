def read_list(name, encode):
    with open(name, encoding = encode) as file:
        lines = [line.rstrip('\n') for line in file]
        return lines

def list_unique_vals_only(name):
    set_list = set(name)
    unique_list = list(set_list)
    return unique_list

def list2dict(name):
    largest = max(name, key=len)
    numbs = {}
    for k in range(1, len(largest)):
        if k not in numbs:
            numbs[k] = []
        numbs[k] = [x for x in name if len(x) == k]
    return numbs

def size_of_list_values(name):
    dict = list2dict(name)
    length_dict = {}
    for k, v in dict.items():
        if k not in length_dict:
            length_dict[k] = []
        count = len(v)
        length_dict[k].append(count)
    return length_dict

def print_list_values(dict, breakpoint):
    new_dict = {k:v for (k,v) in dict.items() if len(v) < breakpoint}
    print(new_dict)

def only_values_of_length(lst, min, max):
    output_lst = []
    for i in range(len(lst)):
        size = len(lst[i])
        if size >= min and size <= max:
            output_lst.append(lst[i])
    return output_lst        

def save_list_to_file(name,lst):
    with open(name, 'w') as f:
        for i in range(0,len(lst)):
            f.write("%s\n" % lst[i])



