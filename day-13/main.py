# #describe Problem
# def my_function():
#     for i in range(1,20):
#         if i==20:
#             print("You got it")

    
# my_function()


from random import randint


dice_imgs=["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num=randint(1,5)   #include both points a andd b
print(dice_num)
# dice_num=6 #when num is 6, it produced bugs
print(dice_imgs[dice_num])