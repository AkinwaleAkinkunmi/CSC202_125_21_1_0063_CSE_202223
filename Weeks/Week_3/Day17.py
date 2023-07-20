# Creating Classes
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self,user):
        user.follower += 1
        self.following += 1

        
# The pass keyword is used when you want the computer to ignore that particular indent.
 

user_1 = User("001", "wale")
user_2 = User("002", "yemi")
user_1.follow(user_2)

print(user_2.follower)