def process_data(*args, ** kwargs):
    print("Positional arguments(Tuple):",args)
    print("Keyword arguments(Dictionary):",kwargs)


process_data(10,20,30, action = "save", debug = True)


dict1 = {"a":1,"b":2}
dict2 = {"b":99, "c":3}

merged = {**dict1,**dict2}

mer = (*dict1,*dict2)

print(merged)
print(mer)