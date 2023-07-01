import random
highest=1000
answer=random.randint(1,highest)
print("please guess number between 1 and{}:".format(highest))
while guess!=answer:
    guess=int(input())
    if guess==0:
        break
    if guess==answer:
        print("wll done! you guessed it")