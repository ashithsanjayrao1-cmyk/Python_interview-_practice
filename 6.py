class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            first_name = data.get("first_name",""),
            last_name = data.get("last_name","")
        )
    @staticmethod
    def is_valid_name(name: dict) -> bool:
        return bool(name) and name.isalpha()


user1 = User("Ashith","Sanjay Rao")

api_payload = {"first_name": "Abhay","last_name":"Karthik Rao"}

user2 = User.from_dict(api_payload)

print(user2.first_name, user2.last_name)
print(User.is_valid_name("Abhay"))
print(User.is_valid_name("Abhay123")) 
print(user1.first_name,user1.last_name)
print(user1.is_valid_name("ssramesh"))