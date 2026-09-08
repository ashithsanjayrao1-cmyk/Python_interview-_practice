import time

def fetch_data(item_id: int):
    print(f"Starting fetch for {item_id}...")

    time.sleep(1)

    print(f"Finished fetch fo {item_id}")
    return f"Item {item_id}"

def main():

    results = [
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    ]

    print("All Results:",results)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"Total time taken: {time.time() - start_time:.2f} seconds")