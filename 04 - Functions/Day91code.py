# functions
# A function thats bound to an instance of a class is called method
# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.
def multiply(x,y):
    result=x*y
    return result

answer=multiply(10.5,4)
print(answer)
forty_two=multiply(6,7)
print()
for val in range(1,5):
    two_times=multiply(2,val)
    print(two_times)

