from python_functions.helper import save_list_to_file, list2dict, print_list_values, size_of_list_values, read_list, list_unique_vals_only, only_values_of_length
import random
from random import randint

random.seed(42)

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))

def h_num(amount_generated):
    alpha_used = ['V','M','P','D','F','R','K','A','Q','E','Z','C','N','B','O','S','G','X','H','J',
            'T','I','W','U','L']
    per_choice = amount_generated / len(alpha_used)
    h_num = []
    for i in (0,len(alpha_used) - 1):
        alpha = alpha_used[i]
        for j in range(0, int(per_choice)):
            k = alpha + random_with_N_digits(6)
            h_num.append(k)
    return h_num

# NHS numbers
lst = read_list("nhsNumber/nhs_numbers.txt","UTF-8")
uni_lst = list_unique_vals_only(lst)
numb_dict = size_of_list_values(uni_lst)
print(f"unique numbers: {len(uni_lst)}")
print(numb_dict)
save_list_to_file("cleaned_output/nhs_numbers.txt", uni_lst)

# Hospital numbers

hosp_number = h_num(20000000)
uni_lst = list_unique_vals_only(hosp_number)
numb_dict = size_of_list_values(uni_lst)
print(f"unique numbers: {len(uni_lst)}")
print(numb_dict)
save_list_to_file("cleaned_output/hosp_number.txt", uni_lst)

