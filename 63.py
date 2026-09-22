default_config = {"theme":"light","notifications":True,"timezone":"UTC"}


user_config = {"theme":"dark","language":"en"}


final_config = default_config | user_config

print(final_config)