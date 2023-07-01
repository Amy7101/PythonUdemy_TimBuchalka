# positional argument
# During a function call, values passed through arguments should be in the order of parameters in the function definition.
# keyboard argument
# values thar when passed into function are identifiable by specific parameter names.
def is_palidrome(string):
    backwards=string[::-1]
    return backwards==string
    return string[::-1]==string

word=input("please enter a word to check:")
if is_palidrome(word):
    print("'{}' is a palidrome". format(word))
else:
    print("'{}' is not a palidrome".format(word))
