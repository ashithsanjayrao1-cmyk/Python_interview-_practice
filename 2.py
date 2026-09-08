import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"TIme taken:{end_time - start_time} seconds")

        return result

    return wrapper

@timer
def process_data():
    time.sleep(3)
    return "Data Processed!"

print(process_data())