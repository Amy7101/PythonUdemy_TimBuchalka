def is_palidrome(string):
    # return string[::-1]
    # return backward==string
    return string[::-1].casefold()==string.casefold()
def palidrome_sentence(sentence):
    string=""
    for char in sentence:
        if char.isalnum():
            string+=char
word=input("please enter a word to check:")
if is_palidrome(word):  
    print("'{} is a palidrome". format(word))
else:
    print("''{} is nott a palidrome".format(word))          
