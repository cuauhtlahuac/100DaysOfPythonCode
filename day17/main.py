class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0  # default value

    # making a method
    def follow(self):  # methods always need self as first parameter
        pass


user_1 = User("001", "Juan Perez")  # initialize with constructor def, in order to avoid typo errors

user_1.follow()
