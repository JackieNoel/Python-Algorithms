#print 1-255
def all_nums(val):
    for i in range(1, val+1):
        print(i)


all_nums(255)

#print sum of 0-255
def sum_of_all_nums(val):
    sum = 0
    for i in range(1, val+1):
        sum = sum + i
    return sum


print(sum_of_all_nums(255))

#find and print max
def find_max(lst):
    max = lst[0]
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max


print(find_max([40, 5, 2, 8, 9, 9777]))

#array with odds
def odds_only(lst):
    new_list = []
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            new_list.append(lst[i])
    return new_list


print(odds_only([6, 4, 9, 2, 1, 5, 10, 99, 3, 7]))


#greater than Y
def greater_than_y(lst, y):
    sum = 0
    for i in range(len(lst)):
        if lst[i] > y:
            sum = sum + 1
    print(f"There are {sum} numbers greater than Y!")


greater_than_y([5, 3, 7, 9, 11, 66, 9], 9)

#print max, min, average
def max_min_avg(lst):
    min = lst[0]
    max = lst[0]
    sum = 0

    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]
        if lst[i] > max:
            max = lst[i]
        sum = sum + lst[i]
    print(max)
    print(min)
    return sum/len(lst)


print(max_min_avg([4,9,1,3,88,9,4,6]))


#swap string for negative values
def swap_for_string(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = "Dojo"
    return lst

print(swap_for_string([1,2,3,-7, 29,8, 0, -2]))


#print odds 1-255
def odds_only_still(lst):
    odd_list = []
    for i in range(len(lst)):
        if lst[i]%2 != 0:
            odd_list.append(lst[i])

    return odd_list

print(odds_only_still([1,2,3,4,5,6,7,8,9]))


#iterate and print array
def print_lst(lst):
    for i in range(len(lst)):
        print(lst[i])

print_lst(["hello", 4,5, "world!", 9, 8])


#get and print average
def find_avg(lst):
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i]

    return sum / len(lst)

print(find_avg([1,2,3,4,5]))


#square the values
def squares_only(lst):
    squares = []
    for i in range(len(lst)):
        lst[i] = lst[i] * lst[i]
        squares.append(lst[i])

    return squares

print(squares_only([1,2,3,4,5]))


#zero out negative values
def no_negatives(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = 0
    return lst

print(no_negatives([1,9,2,8,-3, -5, 1, -7, 9, 0, -5]))

#shift array values
def shift_forward(lst):
    x = len(lst)-1
    for i, elem in enumerate(lst):
        lst[i] = elem + 1
        lst[x] = 0
    print(x)
    print(lst)

shift_forward([1,2,3,4,5,6,7])
shift_forward([4,5,6,7,8,9,10]) 
