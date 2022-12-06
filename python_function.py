def difference(lst):
    diff = 0
    min = lst[0]
    max = lst[0]
    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]
        if lst[i] > max:
            max = lst[i]
        diff = max - min
    return f"The difference between the largest number and smallest number is {diff}"

print(difference([9,8,7,6,5,4,3])) 
print(difference([0,6,99,102,-2,4,8])) 


def less_than_100(num1, num2):
    sum = num1 + num2
    if sum < 100:
        return f"The sum of these values is less than 100: True"
    elif sum > 100:
        return f"The sum of these values is greater than 100: False"

print(less_than_100(10,99))
print(less_than_100(1,9)) 


def hello_name(name):
    return f"Hello, {name}!"

print(hello_name("Jackie"))


def last_one(lst):
    x = len(lst)-1
    print(lst[x])

last_one([0,9,8,7,6,5]) 
last_one([0,9,8,7,6,5,99]) 
last_one([0,9,8,7,6,5,0,8,7]) 


def divisible(lst):
    new_lst = []
    for i in range(len(lst)):
        if lst[i]%2 ==0:
            new_lst.append(lst[i])
    return new_lst

print(divisible([1,2,3,4,5,5,7,8,10]))