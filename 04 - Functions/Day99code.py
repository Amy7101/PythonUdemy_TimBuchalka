def banner_text(text):
    screen_width=50
    if len(text)>screen_width-4:
        raise valueError("string {0} is larger then specified width{1}"
                         .format(text,screen_width))
    if text=="*":
        print("*"* screen_width)
    else:
        centred_text=text.centre(screen_width-4)
        output_string="**{0}**".format(centred_text) 
banner_text("*")
banner_text("Always look on the bright side of life...")          
banner_text("if life seems jolly rotten")
banner_text("There is something you have forgetten")
banner_text("And that to laugh and smile and dance and sing")
banner_text(" ")
banner_text("when you are feeling in the dumps,")
banner_text("*")

banner_text("*")
banner_text("*")

banner_text("*")
