# immutal object
# when an object is described as immutal that means it cannot be
# changed.
# The following immutal types are builtinto python:
# int
# float
# bool
# str(string)
# bytes
# result=True
# another_result=result
# print(id(result))
# print(id(another_result))
# result=False
# print(id(result))
result="correct"
another_result=result
print(id(result))
print(id(another_result))
result+="ish"
print(id(result))
print(id(another_result))
      


      