def calculate_total_letters(str):
    sum = 0
    for i in range(len(str)):
        sum = sum + 1
    print(sum)


#calculate_total_letters("Hello world!")


def new_list(lst):
    unique = []
    for i in range(len(lst)):
        if lst[i] not in unique:
            unique.append(lst[i])
    return unique


print(new_list([6, 9, 2, 0, 5]))
print(new_list([6, 9, 2, 0, 5, 6, 9, 2, 0, 5, 6, 9, 2, 0, 5]))
print(new_list([4,4,4,5,4,4,4,5,4,4,4,5,1]))


def even_only(lst):
    even = []
    for i in range(len(lst)):
        if lst[i]%2 == 0:
            even.append(lst[i])
    return even

print(even_only([3,4,8,12,7,88,0,3,7]))
