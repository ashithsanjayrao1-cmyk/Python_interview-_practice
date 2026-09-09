import time
from contextlib import contextmanager

@contextmanager
def time_block():

    print("Time started...")
    start_time = time.time()

    try:
        yield

    finally:
        end_time = time.time()
        print(f"Timer stopped. Block took {end_time - start_time:.3f} seconds.")

print("Doing some regular code")


with time_block():
    print("Processing heavy data...")
    time.sleep(1.5)
    print("Data processed")

print("Back to regular code.")
