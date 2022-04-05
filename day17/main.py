class User:
    pass  # to avoid the indentation error for emptiness


user_1 = User()  # syntax to create an object from a class

# You can add attributes with dot notation
user_1.id = "001"
user_1.name = "Juan Perez"

print(user_1.name)
