from python_functions.helper import save_list_to_file, list2dict, print_list_values, size_of_list_values, read_list, list_unique_vals_only, only_values_of_length
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))

# NHS numbers
lst = read_list("nhsNumber/nhs_numbers.txt","UTF-8")
uni_lst = list_unique_vals_only(lst)
print(f"unique numbers: {len(uni_lst)}")
save_list_to_file("cleaned_output/nhs_numbers.txt", uni_lst)

# Hospital numbers

hosp_number = h_num(50000000)
uni_lst = list_unique_vals_only(hosp_number)
print(f"unique numbers: {len(uni_lst)}")
save_list_to_file("cleaned_output/hosp_number.txt", uni_lst)

