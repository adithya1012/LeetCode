users = []

class User:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return f"Name: {self.name}, Email: {self.email}"
    def reset_password(self, new_password):
        self.password = new_password

def create_user(name, password, email):
    new_user = User(name, password, email)
    users.append(new_user)
    return new_user

def find_user(email):
    for user in users:
        if user.email == email:
            return user
    print("User not found !!!")
    return None

