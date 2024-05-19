class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f"User({self.user_id}, {self.username}, {self.role})"
