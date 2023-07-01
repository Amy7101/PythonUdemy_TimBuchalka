import timeit
max_value=100
min_value=97
data_list1=list(range(max_value))
data_list2=list(range(max_value))
data_list3=list(range(max_value))
def sanitise_1(data):
    stop=0
    for index, value in enumerate(data):
        if value>=min_value:
            stop=index
            break
        del data[::stop]
start=0    
        