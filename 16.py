columns = ["id","name","role"]
user_data = [101,"Alice","Admin"]


user_data = dict(zip(columns,user_data))

user_dict1 = {k: v for k,v in zip(columns,user_data)}
print(user_data)
print(user_dict1)