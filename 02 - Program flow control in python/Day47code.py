available_exits=["north","south","east","west"]
chosen_exits=["north","south","east","west"]
while chosen_exits not in available_exits:
    chosen_exit=input("please choose a direction :")
    if chosen_exit=="quit":
        print("Game over")
        break
    print("are n't you glad you got out of there")