#calculator


from art import logo



#add
def add(n1,n2):
    return n1+n2

#subtract
def subtract(n1,n2):
    return n1-n2

#add
def multiply(n1,n2):
    return n1*n2

#add
def divide(n1,n2):
    return n1/n2


operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}


def calculator():
    print(logo)

    answer=None

    while True:
        if answer is not None:
            num1=answer
        else:
            num1=float(input("whats the first number ? :"))
        
        num2=float(input("whats the next number ? :"))
        

        operation_symbol=input("Which operation do you want to perform ? :")
        calcuting_function=operations[operation_symbol]
        answer=calcuting_function(num1,num2)


        print(f"{num1}{operation_symbol}{num2}={answer}")

        more=input("Do you want to continue this calculation: type y for continue, n for starting new calculation : ").lower()

        if more !="y":
            calculator()



calculator()

    