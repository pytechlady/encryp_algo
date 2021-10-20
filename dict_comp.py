dict_item=[]
dict_steps = []
dict_set = {}
def dict_comp(stop, step):
    test = stop // step
    stop2 = step * test
    result = list(range(1, stop2+1))

    for i in range(0, len(result), step):
        dict_steps.append(result[i:i+step])
    for number in range(1,test+1):
        dict_item.append(f'item-{number}')
    i=0
    for item in dict_item:
        dict_set[item]= dict_steps[i]
        i+=1
    print(dict_set)

dict_comp(27, 5)
