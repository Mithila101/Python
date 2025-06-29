my_dict = {'a': 10, 'b': 20, 'c': 15}
max_key = max(my_dict, key=my_dict.get)
print("maximum value:", max_key)