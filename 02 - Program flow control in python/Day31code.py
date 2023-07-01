age=int(input())
if 16<=age<=65:
    print("Have a great day at work")
else:
    print("Enjoy your free time")
print("_"*80) 
if age<16 or age>65:
    print("Enjoy your free time")       