answer=5
print("please guess number between 1 and 10:")
guess=int(input())
if guess<answer:
    print("please guess higher")
    guess=int(input())
    if guess==answer:
        print("well done, you guessed it")
    elif guess >answer:
        print("please guess lower")
        guess=int(input())
        if guess==answer:
         print("well done, you guessed it")   
    else:
        print("you got it first time")       