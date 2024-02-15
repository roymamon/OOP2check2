from User import User


# implemented as a singleton design pattern
class SocialNetwork:
    _instance = None

    def __new__(cls, name):
        if not cls._instance:
            cls._instance = super(SocialNetwork, cls).__new__(cls)
            cls._instance._name = name
            cls._instance.users = []  # Initialize users list
            print(f"The social network {name} was created!")
        return cls._instance

    def __init__(self, name):
        pass

    def sign_up(self, username, password):
        # check if the username is already taken
        if any(user.username == username for user in self.users):
            pass  # username is already taken, do nothing
        # check if the password is valid
        elif 4 <= len(password) <= 8:
            user = User(username, password)
            self.users.append(user)
            return user

    def __str__(self):
        network_info = f"{self._name} social network:\n"
        user_info = "\n".join(str(user) for user in self.users)
        return network_info + user_info + "\n"

    def log_in(self, username, password):
        for user in self.users:
            if (user.username == username) and (user.password == password):
                user.isConnected = True
                print(f"{username} connected")

    def log_out(self, username):
        for user in self.users:
            if user.username == username:
                user.isConnected = False
                print(f"{username} disconnected")

