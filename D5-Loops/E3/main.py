#All I have to do is write a program that calclulates the sum of all the even numbers from 1 to 100

total = 0

for number in range(1,101):
    if(number%2==0):
        total += number

print(total)