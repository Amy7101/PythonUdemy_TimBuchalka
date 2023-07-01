data=[4,5,104,105,110,120,130,1390,150,
      160,170,183,187,188,191,350,360]
min_valid=100
max_vlaid=200
# process the low values in the list
stop=0
for index, value in enumerate(data):
    if value>=min_valid:
        stop=index
        break
    print(stop)
    del data[:stop]
    print(data)
    # process the high values in the list
    start=0
    for index in range(len(data)-1,-1,-1):
        if data[index]<=
            start=index