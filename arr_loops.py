#BIGIE SIZE
def big(arr):
    for x in range(len(arr)):
        if arr[x] < 0:
            arr[x] = 'BIG'
    return arr



print(big([-4,6,8,12,-9,0,2]))


#PRINT LOW RETURN HIGH
def low_high(arr):
    min = 0
    max = arr[0]
    for x in range(len(arr)):
        if arr[x] < min:
            min = arr[x]
        elif arr[x] > max:
            max = arr[x]
    print(min)
    return max

print(low_high([90, 54, 75, 24, 12, 0]))


#PRINT ONE, RETURN ANOTHER
def print_one_return_another(arr):
    new_arr = []
    print('----------------------')
    print(f'This is the second to last value in the given array: {arr[len(arr)-2]}')
    for x in range(len(arr)):
        if arr[x]%2 != 0:
            new_arr.append(arr[x])
    return f'This is the first odd value in the given array: {new_arr[0]}'

    

print(print_one_return_another([10,8,9,2,6,-1]))
print(print_one_return_another([45, 0, 3, 88, 11, -7]))


#DOUBLE VISION
def double_vision(arr):
    new_arr = []
    for x in range(len(arr)):
        new_arr.append(2*arr[x])
    return new_arr

print(double_vision([1,2,3,4]))

