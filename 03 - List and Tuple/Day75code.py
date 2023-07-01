menu=[ 
[["eggs","bacon"],
      ["eggs","sausage","bacon"],
      "eggs","bacon","spam"],
["eggs","bacon","spam","sausage"],
["spam","eggs","spam","spam","bacon","spam"],
["spam","sausag","spam","bacon","spam","tomato","spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)
    else:
        print("{0} has a spam scpre of{1}".format(meal,meal.count("spam")))