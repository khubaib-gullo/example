array = [1,21,[3,4,5],6,[8,9,[10,11,12],13],14,15]
#

# output
# [1,21,3,4,5,6,7,8,9,10,11,12,13,14,15]
# new = []
# def fun(array):
#     for i in array:
#         x = i
#         if isinstance(x, list):
            
#             print(x)
#             print(len(x))
# fun(array)            


import numpy 

data = numpy.asarray(array)
print(data)







# array = ['abc', ['d', 'ef'], 'r', ['o']]
# def fun1(array):
#     for d in array:
#         yield d

#         print(d)

# data = fun1(array)
# for d in data:
#     print(d)

# data = chain(array)
# for d in data:
#     print(d)
def from_iterable(iterables):
    # chain.from_iterable(['ABC', 'DEF']) → A B C D E F
    for iterable in iterables:
        yield from str(iterable)

# array = [1, [2, 3], 4]
array = ['1', '3', '6', '7', ['10','+','33'], '10']
# array = [1,21,[3,4,5],6,[8,9,[10,11,12],13],14,15]
data = list(from_iterable(array))
print(data)
# print(data)
ls = []
for d in data:
    try:
        d = int(d)
        ls.append(d)
        
    except:
        pass
print(ls)

# def prepend(value, iterable):
#     "Prepend a single value in front of an iterable."
#     # prepend(1, [2, 3, 4]) → 1 2 3 4
#     return chain([value], iterable)

# data = prepend([6, 7, 8], [1, 2, 4, 5])
# for d in data:
#     print(d)

            # for i in x:
        #     y = i
        #     if isinstance(y, list):
        #         print(y)
        
        #     else:
        #         print(y)
        # # print(f'index {array.index(i)}')
        # # print(x)
        # # return array
        # new.append(x)
        # array.remove(x)

# print(array)
# print(new)

    
        



        
# while True:
# for i in array:
#     # x = isinstance(5, list)
#     # print(type(i))
#     x = i
#     # print(type(x))
#     if isinstance(x, list):
#         print(f'list length {len(x)}')
#         for i in x:
#             if isinstance(x, list):
#                 print(i)
#             else:
#                 newarray.append(x)
#     else:
#         newarray.append(x)
# print(newarray)

            
# print(newarray)
    # try:
    #     x = Counter(i)
    #     print(len(x))
    #     print(f"list {x}")
    #     for i in x.elements():
    #         print(i)
    # except:
    #     print(f"singl {i}")
    # print(x)
    # if x:
    #     for d in i:
    #         print(x)

# for i in array:
       
#     print(i)
#     print(type(i))
#     try:
        
#         data = list(map(lambda x: x, i))
#         for d in data:
#             try:
#                 data = data = list(map(lambda x: x, d))
#                 print(data)
#             except:
#                 newarray.append(d)
#     except:
#         newarray.append(i)
        

# print(newarray)    
        

    # try:
    #     print(set(i))
    #     array = set(i)
    #     for i in array:
    #         newarray.append(i)
    #         # print(i)   
    # except:
    #     print(i)
    #     pass
# print(newarray)