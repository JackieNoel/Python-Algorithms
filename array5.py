#REARRANGE ARRAYS
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


print(rearrange([9,5,2,4,-1]))
print(rearrange([8, 17, -2, 5]))


#AVERAGE
def average(arr):
    # average = 1
    sum = 0
    for x in arr:
        sum += x
        average = sum / len(arr)
    print(average)

average([10, 20, 30, 40, 50, 60])
average([305, 275, 450, 800])