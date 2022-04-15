class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0  # default value
        self.following = 0

    # making a method
    def follow(self, user):  # methods always need self as first parameter
        user.followers += 1
        self.following += 1


user_1 = User("001", "Juan Perez")
user_2 = User("002", "Maria Martinez")

user_1.follow(user_2)

print(user_1.following)  # user 1 has a new following
print(user_2.followers)  # user 2 has a new follower
