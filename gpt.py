def flatten(lst):
    flattened_list = []
    for item in lst:
        if isinstance(item, list):
            print(item)
            flattened_list.extend(flatten(item))
            print(flattened_list)
        else:
            # print(item)
            flattened_list.append(item)
        # print(flattened_list)            
    return flattened_list


array = [1,21,[3,4,5],6,[8,9,[10,11,12],13],14,15]

print(array(21))
print(flatten(array))
# a1 = [3, 4, 5]
# a2 = [6, 7, 8, [10, 11]]
# data = a1+a2
# print(data)