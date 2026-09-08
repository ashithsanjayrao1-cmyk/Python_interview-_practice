user_data = {"name":"Ashith","role":"Admin"}


if "age" in user_data:
    age = user_data["age"]

else:
    age = "Unknown"


try:
    age = user_data["age"]

except KeyError:
    age = "Unknown"
    print(user_data)

finally:
    print(user_data)
    print(age)