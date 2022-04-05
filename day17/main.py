class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name


user_1 = User("001", "Juan Perez")  # initialize with constructor def, in order to avoid typo errors

print(user_1.name)
