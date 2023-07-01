# list=[2,4,6,8,10,12,14]
# seaeching list sequentially
def linear_search(list,n,key):
    for i in range(0,n):
        if(list[i]==key):
            return i
        return-1
list=[2,4,6,8,10,12] 
key=2
n=len(list)
key=4
n=len(list)
key=6
n=len(list)
key=8
n=len(list)
key=10
n=len(list)
key=12
n=len(list)
res= linear_search(list,n,key)
if(res==-1):
    print("WOW! element is found")
else:
    print("OOPS! element is not found")   
