class UserModel:
    def __init__(self):
        self.users = {
            "admin": "admin123",
            "user1": "password1"
        }

    def validate_user(self, username, password):
        return username in self.users and self.users[username] == password
