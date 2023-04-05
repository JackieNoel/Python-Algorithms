# REVERSE
def reverse(arr):
    for i in range((len(arr))//2):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    print(arr)
reverse([10, 20, 30, 45, 50, 65, 70])


#FILTER RANGE
def filterminmax(arr, min, max):
    new_arr = []
    for i in range(len(arr)):
        # print(arr[i], max, min)
        if arr[i] < max and arr[i] > min:
            new_arr.append(arr[i])
    print(new_arr)

filterminmax([24, 25, 45, 30, 55, 2], 23, 36)


#CONCAT
def come_together(arr1, arr2):
    new_arr = []
    for i in range(len(arr1)):
        new_arr.append(arr1[i])
    for x in range(len(arr2)):
        new_arr.append(arr2[x])
    return new_arr

print(come_together(["a", "b", "c"], [1, 2, 3]))



