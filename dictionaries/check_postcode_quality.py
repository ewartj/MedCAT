from python_functions.helper import save_list_to_file, list2dict, print_list_values, size_of_list_values, read_list, list_unique_vals_only, only_values_of_length


lst = read_list("postcodes/all_postcodes.txt","UTF-8")
uni_lst = list_unique_vals_only(lst)
print(f"unique postcodes: {len(uni_lst)}")
dict = list2dict(uni_lst)
numb_dict = size_of_list_values(uni_lst)
print_list_values(dict, 100)
print(numb_dict)
new_lst = only_values_of_length(uni_lst, 6,9)


save_list_to_file("cleaned_output/postcodes.txt", new_lst)

