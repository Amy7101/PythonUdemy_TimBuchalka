menu=[ 
[["eggs","bacon"],
      ["eggs","sausage","bacon"],
      "eggs","bacon","spam"],
["eggs","bacon","spam","sausage"],
["spam","eggs","spam","spam","bacon","spam"],
["spam","sausag","spam","bacon","spam","tomato","spam"],
]
for index in range(len(meal)-1,-1,-1): 
 if meal[index]=="spam":
  del meal[index]
  print(meal)
  