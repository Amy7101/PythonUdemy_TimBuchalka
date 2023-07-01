pangram="The quick brown fox jumps over the lazy dog"
words=pangram.split()
print(words)
number="9,223,372,036,854,776,807"
print(number.split(" ,"))
# values="".join(char if char not in separators else"" for char in number).split()
generated_list=['9',''
                '2','2','3','',
                '3','7','2','',
                '0','3','6','',
                '7','7','4','',
                '8','0','7']
values="".join(generated_list).split()
print(values)
values_list=values.split()
print(values_list)
# replace the values in place
# for index in range(len(values_list)):
    # values_list[index]=str(values_list[index])
    # print(values_list)
# create a new list
integer_values=[]
for values in values_list:
    integer_values.append(int(values))
    print(integer_values)