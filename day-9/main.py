# programming_dictionary={
#
#     "Bug":"An error in program that prevent it from running as expected" ,
#     "Function":"A piece of code that you can easily call over and over again"
#
# }
#
# # retrieving item from dictionary
# print(programming_dictionary["Bug"])
#
#
# # adding new itms to dictionary
# programming_dictionary["Loop"]="The action of doing something over and over again"
#
#
# #creat an empty_dictionary
# empty_dictionary={}
#
# #wipe an exisitng dictionary
# # programming_dictionary={}
#
#
# #edit an dictionary
# programming_dictionary ["Bug"]="kira"
#
# # loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#
#
# # _____________________________________Nesting__________________________________________________
#
# travel_log=[
#     {
#     "Country":"France",
#     "cities_visited":["Paris","Dijon","Lile"],
#     },
#
#
#    {
#        "Country":"Germany",
#        "cities_visited":["Berlin","Hamburg","Stuttgart"],
#    },
#
#     # list nested inside dictionary, which in itself nested in another dictionary
#    {"Country":"Australia",
#     "cities_visited":{
#         "cities_visited": ["Sydney", "Melbourne", "Perth"]
#         },
#    }
#
#     # nesting  a dictionary in list
# ]


def a_function(a_parameter):
    a_variable = 15
    return a_parameter


a_function(10)
