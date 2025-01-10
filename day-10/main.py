
#functions with output

# //single return value in function
def format_name(f_name,l_name):
    """ Take a first and last name and
      format it to return thr title case version of name"""
    
    name=f_name.title() + l_name.title()
   
    return name


final_name=format_name("shiva","dhakal")
print(final_name)




# //mutiple return value in function 
# mutiple return can be used in a function using if condition   