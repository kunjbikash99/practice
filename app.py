import random
x=0
counter=1
print("this is a guessing a number game,you will 5 chances to try until you guess it right")
while counter<=5:
    print("this is your",counter,"try")
    b=random.randint(1,99)
    guess=int(input("enter your guess from 1 to 99"))
    if guess==b:
        print("good guess!")
        x+=1
        break
    else:
        print("try again!")
    counter+=1
if x==0:
    print("sorry but that was not very successful")
print("game over!")