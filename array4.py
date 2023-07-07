# SHUFFLE
# import numpy as np
import math
import array
import random



def shuffle(arr, n):
    for x in range(n-1, 0, -1):
        j = random.randint(0, x+1)
        arr[x], arr[j] = arr[j], arr[x]
    return arr


print(shuffle([5, 4, 3, 2, 1, 0], 6))


# WORK IN PROGRESS

    # num = random.randrange(0, len(arr))
    # const = new_arr[len(new_arr)-1]
    # new_arr = []
    # final_arr = []
    # # index = new_arr[0]
    # max = 0

    # arr = np.array([5, 4, 3, 2, 1, 0])
    # random.shuffle(arr)
    # print(arr)
# for x in arr:
#     # x = arr[random.randint(0, len(arr)-1)]
#     # new_arr.append(x)
#     print(x)
# NEED CONDITIONAL TO CHECK THAT ELEMENT ISN'T ALREADY IN NEW ARRAY
# for y in new_arr:
#     print(f'This is new array {new_arr}')
#     print(f'This is y {y}, this is const {new_arr[len(new_arr)-1]}')
#     if  y == new_arr[len(new_arr)-1]:
#         new_arr.remove(y)
    # return arr

print('-------------------')

# STATS UNTIL DOUBLES
def random_nums():
    max = 0
    min = 1
    sum = 0
    average = 1
    rolls = 0
    previous_value = None
    current_value = random.randint(0, 21)

    while previous_value != current_value:
        print(current_value)
        if current_value > max:
            max = current_value
        if current_value <= min:
            min = current_value
        sum += current_value
        rolls +=1
        average = sum / rolls
        previous_value = current_value
        current_value = random.randint(0, 21)
    return f'Current Value: {current_value}, Number of rolls: {rolls}, Maximum: {max}, Minimum: {min}, Average: {average}'

print(random_nums())