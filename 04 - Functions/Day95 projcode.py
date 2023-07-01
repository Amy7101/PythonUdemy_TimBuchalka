import random
def get_integer(prompt):
    while True:
        temp=input(prompt)
        if temp.isnumeric():
            return int(temp)
        
highest=1000
answer=random.randint(1,highest)
print(answer)#todo: remove after testing
guess=0#intialize to any number that does not equal the answer
while guess!=answer:
    guess=get_integer(" :")
    if guess==0:
        break
    if guess==answer:
        print("well done, you guessed it")
        break
    else:
        if guess<answer:
            print("please guess higher")
        else:
            print("please guess lower")
