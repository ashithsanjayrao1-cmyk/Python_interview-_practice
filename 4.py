class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to {self.db_name}..")

    def __exit__(self, exc_type, exc, tb):
        print(f"Connect to {self.db_name} closed")

        return False

try:
    with DatabaseConnection("userDB") as db:
        print("Executing quesry SELECT* FROM users")

        raise ValueError("Database timeout error..!!")

except ValueError as e:
    print(f"Caught error: {e}")
