import time

def retry(max_attempts = 3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    if attempts == max_attempts:
                        print("Max attempts reached. Failing.")
                        raise 
                    time.sleep(1)

        return wrapper
    return decorator

@retry(max_attempts = 3)
def unstable_api_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network timeout!")
    return "Data fetched successfully!"

print(unstable_api_call())