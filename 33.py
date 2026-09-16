messy_data = "  apple  , banana,   cherry           "

clean_day = "-".join([fruit.strip() for fruit in messy_data.split(",")])

print(clean_day)