# REMOVE NEGATIVES
def remove_negatives(arr):
    new_arr = []
    pos_arr = []
    index = 0
    while index <= len(arr):
        if arr[index] < 0:
            print(f'This is the element, {arr[index]}, this is index {index}')
            arr.remove(arr[index])
        index +=1
    print(arr)



remove_negatives([6, -1, 0, -8, 7.5, 4, -3])


#SECOND TO LAST
def second_to_last(arr):
    if len(arr) > 2:
        print(arr[len(arr)-2])
    else:
        print('Null')

second_to_last([9,8,6,3,9,1])
second_to_last([12, 45, 78, 34, 88, 90])
second_to_last([0, 1, 2, 3, 6, 8, 4, 5]) 
second_to_last([9,1])

#Nth TO LAST
def nth_to_last(arr, num):
    if len(arr) > 2:
        print(arr[len(arr)-num])
    else:
        print("Null")

nth_to_last([1,9,2,8,3,7], 2)