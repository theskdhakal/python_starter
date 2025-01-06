# # file=open("my_file.txt")
# # contents=file.read()
# #
# # print(contents)
# #
# # file.close()
# #
# # _____________read only mode____________________
# with open("my_file.txt") as file:
#     contents=file.read()
#
#     print(contents)
#
# # if there is no file,it will create one
# # +++++++++++++++write mode+++++++++++++
# with open("my_file.txt",mode="w") as file:
#    file.write("NEW text")
#
# # +++++++++++++++append mode+++++++++++++
# with open("my_file.txt",mode="a") as file:
#    file.write("appending her")



with open ("./Input/Letters/starting_letter.txt") as document:
    letter=document.read()


with open("./Input/Names/invited_names.txt",'r')as file:
    for line in file:
        name=line.strip()
        personalised_letter= letter.replace("first", name)
        print(personalised_letter)
        with open(f"./Output/Ready_To_Send/invitation_for_{name}.txt",mode='w') as output_file:
            output_file.write(personalised_letter)



