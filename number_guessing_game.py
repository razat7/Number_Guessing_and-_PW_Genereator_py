import random

numbers = [0,1,2,3,4,5,6,7,8,9]
result = random.choice(numbers)
guess = int(input("Enter the number : "))

count = 0
while guess != result:
    if guess +1 > result:
        print("Try again, You guessed Higher Number")
    elif guess +1 == result:
        print("Try again, Too Close But Small")
    elif guess -1< result:
        print("Try Again, You Guessed Very Smaller Number")
    elif guess -1 == result:
          print("Try again, Too Close But High")
    guess = int(input("Enter the number : "))
    count += 1
else:
    print("Congratulations, You guesssed the right number")
    print(f"total number of attempts : {count}" )