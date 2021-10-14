class User:
    def __init__(self,user_id,name):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0
        print("new user being created ...")

    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "jamal")
user_2 = User("002","angela")

print(user_1.name)
user_1.follow(user_2)

print(f"User's Following: {user_1.following}")