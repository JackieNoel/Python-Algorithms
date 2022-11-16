#sum of all numbers in a list
def sum_of_all_nums(lst):
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i]
    return sum

print(sum_of_all_nums([4,5,9,2]))


#product of all numbers in a list
def multiply_nums(lst):
    product = 1
    for i in range(len(lst)):
        product = product * lst[i]
    return product

print(multiply_nums([1,2,3,4,5]))


#check if number is within a certain range
def range_check(num):
    min = 0
    max = 10
    if num > min and num < max:
        print(f"The number {num} is within the range!")
    else:
        print(f"I'm sorry, {num} is not within this range...")

range_check(2)
range_check(22)

def in_range(num2):
    if num2 in range(3,10):
        print(f"boom, the number {num2} is within range!")
    else:
        print(f"yikes, the number {num2} is not within range...")

in_range(4)
in_range(45)


#print all even numbers in a given list
def evens_only(lst):
    new_list = []
    for i in lst:
        if i%2 == 0 and i != 0:
            new_list.append(i)
    return new_list

print(evens_only([9,78,4,0,11,12,3,6]))


