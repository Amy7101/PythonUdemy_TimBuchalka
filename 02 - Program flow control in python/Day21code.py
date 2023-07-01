# if statement
name=input("please enter your name:")
age=int(input("How old are you,{0}?".format(name)))
print(age)
if age>=18:
    print("you are old enough to vote")
    print("please put an x in the box")
else:
    print("please come back in{0} years". format(18-age))
    if age>18:
        print("please come back in{0} years".format(18-age))
    else:
        print("you are old enough to vote")
        print("please put an x in the box")