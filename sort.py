def bubble_sort(arr):
    for x in range(len(arr)-1):
        if arr[x] > arr[x+1]:
            arr[x], arr[x+1] = arr[x+1], arr[x]
            for y in range(len(arr)-1):
                if arr[y] > arr[y+1]:
                    arr[y], arr[y+1]= arr[y+1], arr[y]
    print(arr)
        

bubble_sort([4,3,7,1,9,10,15])
bubble_sort([94, 13, 17, 50, 61, 48])