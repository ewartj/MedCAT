import postcodes_io_api

api  = postcodes_io_api.Api(debug_http=False)
#data = api.get_postcode('SW112EF')

postcodes = []
with open('postcodes3.txt', 'w') as f:
    for i in range(0,200000):
#        print("Gettings postcode {}".format(i))
        data = api.get_random_postcode()
        postcodes.append(data["result"]["postcode"])
        f.write("%s\n" % postcodes[i])

number_of_unique_values = len(postcodes)
print(f"postcode3: {number_of_unique_values}")


        