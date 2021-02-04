from random import randint
from python_functions.helper import save_list_to_file, print_list_values, size_of_list_values, read_list, list_unique_vals_only, only_values_of_length

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))

def mobile(amount_generated):
    mobile = []
    allowed_3rd_numbs = [1,2,3,4,5,7,8,9]
    per_choice = amount_generated / len(allowed_3rd_numbs)
    for i in range(0,len(allowed_3rd_numbs)):
        i = allowed_3rd_numbs[i]
        for j in range(0, int(per_choice)):
            k = f"07{i}{random_with_N_digits(9)}"
            mobile.append(k)
    return mobile

def landline(amount_generated, area_codes):
    landline = []
    per_choice = amount_generated / len(area_codes)
    for i in range(0,len(area_codes)):
        i = area_codes[i]
        for j in range(0, int(per_choice)):
            k = '0' + str(i) + ' ' + random_with_N_digits(6)
            landline.append(k)
    return landline

#mob = mobile(1000000)
mob = mobile(100)

landline_lst = read_list("phone_numbers/area_codes.txt", "UTF-8")
landline_numbers = landline(100, landline_lst)

mob = list_unique_vals_only(mob)
mob_lengths = size_of_list_values(mob)
print(mob_lengths)
print(f"unique mobiles: {len(mob)}")

# landline_numbers = list_unique_vals_only(landline_numbers)
# londline_lengths = size_of_list_values(landline_numbers)
# print(londline_lengths)
# print(f"unique landlines {len(landline_numbers)}")

# save_list_to_file("mobile_numbers.txt", mob)
# save_list_to_file("landline.txt", landline_numbers)