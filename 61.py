def fetch_data():
    try:
        print("1. Connecting to database...")

    except ConnectionError:
        print("2. Connection failed!")

    else:
        print("3. Fetching user records...")

    finally:
        print("Closing connection")