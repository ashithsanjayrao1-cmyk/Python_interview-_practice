user_data = {"name":"RAJU","age": 25}

#email = user_data["email"]

email = user_data.get("email","No Email Provided")


print(f"User Email: {email}")

print(user_data.get("name"))

print(user_data.get("phno","No ph no"))