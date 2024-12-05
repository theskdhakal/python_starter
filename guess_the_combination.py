combinations=[]
def guess_the_combination(setA,setB,odd):
    for item in setA:
        for thing in setB:
            if float(item)*float(thing)==odd:
                combinations.append((item,thing))
                print(f"Your probable combination may be {item},{thing}")


setA=input("provide the list of all probable odds in game A: ").split(',')
setB=input("provide the list of all probable odds in game B: ").split(',')
odd=float(input("whats the given odd? : "))

guess_the_combination(setA, setB, odd)

if combinations!=[]:
    print(f"your combinations are {combinations}")
else:
    print("this might not be correct game you are looking for")