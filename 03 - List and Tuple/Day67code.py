data=[4,5,104,105,110,120,130,1390,150,
      160,170,183,187,188,191,350,360]
# del data[0:2]
# print(data)
# del data[16:]
# print(data)
min_valid=100
max_valid=200
for index, value in enumerate(data):
    if(value< min_valid)or (value>max_valid):
        del data[index]
        index-=1
        print(data)
