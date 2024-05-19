from models.user import User
from data.data_manager import UserDataManager

class UserService:
    def __init__(self, data_manager=None):
        self.data_manager = data_manager or UserDataManager()
        self.users = [User(**user) for user in self.data_manager.load_data()]

    def add_user(self, user):
        self.users.append(user)
        self.data_manager.save_data([user.__dict__ for user in self.users])

    def get_user(self, username):
        return next((user for user in self.users if user.username == username), None)

    def authenticate_user(self, username, password):
        user = self.get_user(username)
        return user if user and user.password == password else None
