# creating a class
class User:
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.followers=0  #a default value can be provided to an attribute , for eg follower count of instagram initially




# creating an object , instance of above class
user_1=User("001","shiva")
print(user_1.username)

# # adding attribute
# user_1.id="001"
# user_1.name="Shiva"

