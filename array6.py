from statistics import mode
import math


# FLATTEN
def flatten(arr):
    new_list = []
    for x in arr:
        if type(x) == list:
            for y in x:
                # print(f'This is one element in the list {y}')
                new_list.append(y)
        else:
            new_list.append(x)
    return new_list


print(flatten([1, [2, 3], 4, []]))
print(flatten([[], [6, 5, 4], 3, 2, [1, 0]]))


def flatten_again(arr):
    for x in arr:
        if type(x) != int:
            arr.pop()
        if type(x) == list:
            for y in x:
                arr.append(y)
        if type(x) != int:
            arr.remove(x)
    return arr


print(flatten_again([1, [2, 3], 4, []]))


# REMOVE DUPLICATES
def remove_duplicates(arr):
    new_arr = []
    for x in arr:
        if x not in new_arr:
            new_arr.append(x)
    return new_arr


print(remove_duplicates([1, 2, 2, 3, 4, 5, 5, 6, 7, 3, 10]))
print(remove_duplicates(
    [5, 7, 4, 5, 7, 9, 4, 5, 6, 7, 8, 9, 1, 4, 5, 5, 5, 8, 9]))


# BALANCE INDEX
def balance_point(arr):
    if len(arr) % 2 != 0:
        print('Midpoint:', arr[math.floor(len(arr)/2)])
    else:
        print('This array has no midpoint')


balance_point([10, 3, 7, -5, 6, 1, 67])
balance_point([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
balance_point([6, 19, 23, 5, 1])


# BALANCE POINT
def find_center(arr):
    if len(arr) % 2 != 0:
        print('True')
    else:
        print('False')


find_center([0, 4, 87, 1, 33, -2])
find_center([5, 4, 5, 4, 5, 4, 5])


# MODE
print(mode([1, 2, 3, 1, 2, 3, 3, 1, 3, 1, 2, 4, 3]))


# SMARTER SUM
def sum_to_num(num):
    sum = 0
    for x in range(0, num+1):
        sum += x
    return sum


print(sum_to_num(10))
print(sum_to_num(4))
