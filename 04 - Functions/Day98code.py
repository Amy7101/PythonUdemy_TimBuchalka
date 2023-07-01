def banner_text(text):
    screen_width = 80
    if len(text) > screen_width-4:
        print("EEK!!")
        print("ThE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width-4)
        output_string = "**{0}**".format(text.center(screen_width-4))
        print(output_string)


banner_text("*")
banner_text("Always lok on the bright side of life")
banner_text("If life seems jolly rotten")
banner_text("There's something you've forgetten")
banner_text("And thats to laugh and smile and dance and sing")
banner_text(" ")
banner_text("when you are feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("just purse your lips and whistle- thats the things!")
banner_text("And...aleays looks on the brigjht side of the life....")
banner_text("*")

result = banner_text("Nothing is returned")
print(result)

numbers = [4, 2, 7, 3, 5, 6, 8, 9, 1]
print(numbers.sort())
