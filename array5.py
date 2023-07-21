# REARRANGE ARRAYS
import random


def rearrange(arr):
    max = 0
    min = 0
    for x in range(len(arr)-1):
        for y in range(len(arr)-1-x):
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]

        # num = arr[x+1]
        # if num > arr[x]:
        #     arr[x], num = num, arr[x]
    return arr


print(rearrange([9, 5, 2, 4, -1]))
print(rearrange([8, 17, -2, 5]))


# AVERAGE
def average(arr):
    # average = 1
    sum = 0
    for x in arr:
        sum += x
        average = sum / len(arr)
    print(average)


average([10, 20, 30, 40, 50, 60])
average([305, 275, 450, 800])


# REVERSE STRING
def reversestr(str):
    num = len(str)-1
    new_str = ''
    while num >= 0:
        new_str += str[num]
        num -= 1
    return new_str


print(reversestr('Hello World'))
print(reversestr('This is backwards'))
print(reversestr('leoN eikcaJ'))


# REMOVE EVEN LENGHT STRINGS
def remove_evens(arr):
    for x in arr:
        print(x)
        if len(x) % 2 == 0:
            arr.remove(x)
    return arr


print(remove_evens(
    ['Kids', 'potatoes', 'fingertips', 'eyelids', 'tomatoes', 'hippy']))
print(remove_evens(['even', 'odd', 'even', 'odd', 'even', 'odd']))

# BINARY SEARCH


def binary_search(str, num):
    for x in str:
        if x == num:
            return 'True!'
        else:
            return 'False!'


print(binary_search(" &-0379DEFXZ[abcz|", "6"))
print(binary_search("980-6[abcd]559016", "8"))
print(binary_search("56565656565647676767487878787444", "4"))


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
print(flatten([[], [6,5,4], 3, 2, [1,0]]))

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

print(flatten_again([1,[2,3],4,[]]))


#REMOVE DUPLICATES
def remove_duplicates(arr):
    new_arr = []
    for x in arr:
        if x not in new_arr:
            new_arr.append(x)
    return new_arr


print(remove_duplicates([1,2,2,3,4,5,5,6,7,3,10]))
print(remove_duplicates([5,7,4,5,7,9,4,5,6,7,8,9,1,4,5,5,5,8,9]))
