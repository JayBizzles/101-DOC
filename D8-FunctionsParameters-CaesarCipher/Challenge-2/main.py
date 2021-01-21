#Write your code below this line 👇

#My solution to the challenge:

def prime_checker(number):
        for i in range(2,number):
            if number % i == 0:
                print(f"{number} is not a prime number")
                break
        if number % i != 0:
            print(f'{number} is a prime number')
    
#Teacher's solution to the challenge:

# def prime_checker(number):
#     isPrime = False
#     for i in range(2,number):
#         if number % 2 == 0:
#             isPrime = True
#     if isPrime:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



