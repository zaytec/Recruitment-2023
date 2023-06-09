'''GUESS THE NUMBER'''
print("GAME RULES")
print("You have to guess the random number, at the starting of the game you'll have 100 points, for every wrong guess you'll lose 5 points, ALL THE BEST")
import random
Name = input("Enter Your Name:")
LL = int(input("Enter The lower limit of the game:"))
UL = int(input("Enter the upper limit of the game:"))
if (UL<LL):
    print ("enter a valid range")
ans = random.choice(range(LL,UL+1))
points=100
guess=0
while (guess != ans) or (points == 0):
    guess=int(input("enter your guess:"))
    if points==0:
        print("Sorry! you're out of tokens to play")
        break
    if guess!=ans:
        points-=5
        print("wrong guess you are left with",points,"tokens")
    if guess==ans:
        print(Name,"you've guessed it right and your score is",points)
        break

    if guess not in range(LL,UL+1):
        print("You've to guess a number between the range",UL,"and",LL)
    elif guess < ans:
        print("You've guessed too low!")
    elif guess > ans:
        print("You've guessed too high!")






    
