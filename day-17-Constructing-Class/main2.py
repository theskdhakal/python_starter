# creating a class
class User:
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.followers=0  #a default value can be provided to an attribute , for eg follower count of instagram initially
        self.following=0

    def follow(self, user):
        user.followers +=1
        self.following +=1





# creating an object , instance of above class
user_1=User("001","shiva")
user_2=User("002","Mona Lisa")


# # adding attribute
# user_1.id="001"
# user_1.name="Shiva"

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)

