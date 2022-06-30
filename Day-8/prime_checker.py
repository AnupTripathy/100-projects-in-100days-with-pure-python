#Write your code below this line 👇

def prime_checker(number):
    factors = 0
    for i in range(1, number+1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        print("Prime Number")
    else:
        print("Composite")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)