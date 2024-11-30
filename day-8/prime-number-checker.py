

def prime_checker(number):
    is_prime=True
    for divider in range(2,number):
        if number % divider==0:
            is_prime=False
    
    if is_prime:
        print("Its a prime number")
    else:
        print("It is not a prime number")
    
          


n=int(input("check this number: "))


prime_checker(number=n)