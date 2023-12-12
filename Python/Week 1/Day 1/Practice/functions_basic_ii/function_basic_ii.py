# 1 
def countdown (num):
    for i in range(num,-1,-1):
        print(i)
    return i

# 2
my_list = []  
def print_and_return(items):
    my_list.append(items)
    for i in  range (0, len(my_list)):
        print(my_list[i])
print_and_return([1,2])
#3
def first_plus_length (items):
    x=0
    for el in items :
        x = items[0]+len(items)
    print(x)
    return x 
first_plus_length([4,5,5,7,9,7,8,9,10,22,47])
# 4 
def values_greater_than_second(lst):
    if len(lst) < 2:
        print(False)
        return False

    next_value = lst[1]
    new_list = []
    for i in range(0, len(lst)):
        if lst[i] > next_value:
            new_list.append(lst[i])

    print(new_list)
    return new_list
# 5 
def length_and_value (size , value):
    new_list = []
    for  i in range (0,size):
        new_list.append(value)
        print(new_list)

    x = length_and_value(5,77)
    print(x)







        








