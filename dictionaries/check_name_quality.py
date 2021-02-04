from python_functions.helper import save_list_to_file, list2dict, print_list_values, size_of_list_values, read_list, list_unique_vals_only
import collections

def count_string(string, breakpoint):
    d = {}
    for c in string:
        try:
            d[c] += 1
        except:
            d[c] = 1
    for v in d.items():
        if v[1] >= breakpoint:
            return False

def find_single_char_repeats(name_lst, breakpoint = 6):
    for i in range(0,len(name_lst)):
        real_name = count_string(name_lst[i], breakpoint)
        if real_name == False:
            print(name_lst[i])

def split_into_2_names(names_lst):
    """
    Splits names with / into 2 names e.g. ewart/jonny becomes ewart and jonny.

    """
    names_to_add = []
    output = []
    for i in range(0,len(names_lst) - 1):
        try:
            if "/" in names_lst[i]:
                temp_lst = names_lst[i].split("/")
                for i in range(0,len(temp_lst)):
                    names_to_add.append(temp_lst[i])
                names_lst.remove(names_lst[i])
            else:
                output.append(names_lst[i])
        except IndexError:
            continue
    for i in range(0,len(names_to_add)):
        output.append(names_to_add[i])
    return output

def remove_single_chars(names_lst):
    output = []
    for i in range(0,len(names_lst) -1):
        if len(names_lst[i]) > 1:
            output.append(names_lst[i])
    return output

lst = read_list("name-dataset/last_names.all.txt","UTF-8")
lst = remove_single_chars(lst)
uni_lst = list_unique_vals_only(lst)
# #print(uni_lst)
# dict = list2dict(uni_lst)
numb_dict = size_of_list_values(uni_lst)

# print("NAMES SPLIT")
# print("###########")
# test = [ "dsg","one/two","sahhgishgih"]
# # print(test)
test_lst = split_into_2_names(uni_lst)
lastname_lst = list_unique_vals_only(test_lst)
# numb_dict2 = size_of_list_values(uni_lst_2)
# print(numb_dict2)
#print(test_lst)
# dict = list2dict(test_lst)
# print_list_values(dict, 100)

lst = read_list("name-dataset/first_names.all.txt","UTF-8")
lst = remove_single_chars(lst)
uni_lst = list_unique_vals_only(lst)
test_lst = split_into_2_names(uni_lst)
firstname_lst = list_unique_vals_only(test_lst)

# NB: first and last names have same values: need to compare the lusts and print all 
# shared values 

test = set(lastname_lst).intersection(firstname_lst)
print(len(test))

test = list(test)

dict = list2dict(test)
#print_list_values(dict, 200)

# looking at the values it appears soem surnames have been added
# to both lists. Removing from first-name

trimmed_firstname_lst = [x for x in firstname_lst if x not in test]
#dict = list2dict(trimmed_firstname_lst)
numb_dict2 = size_of_list_values(trimmed_firstname_lst)
print(numb_dict2)
print(len(lastname_lst))
print(len(trimmed_firstname_lst))

#save files
save_list_to_file("cleaned_output/cleaned_first_name.txt", trimmed_firstname_lst)
save_list_to_file("cleaned_output/cleaned_last_name.txt", lastname_lst)