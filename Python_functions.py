# print the product of two numbers, unless it is greater than 1000, then print sum



def multiply(a, b):
    product = a*b
    sum = a+b
    if product <= 10000:
        print(product)
    else:
        print(sum)

multiply(300, 60)


# print sum of current number and previous number
def loops():
    sum = 0
    previous_num = 0
    for i in range(10):
        sum = previous_num + i
        previous_num = i
        print(f"The current number is {i} and the previous number is {previous_num} so their sum is equal to {sum}")

loops()

#print even indexes in a string
def even_index():
    word = input("Enter word ")
    print("Original string", word)
    size = len(word)

    for i in range(0, size-1, 2):
        print(f"the index is {i}, {word[i]} ")

even_index()

#display only numbers divisible by 5 from a list
def multiplesOfFive(lst):
    for i in lst:
        if i % 5 == 0:
            print(i)

multiplesOfFive([1,5,7,10,15,4,8])

#check if the first and last values in a list are the same
def checkFirstLast(lst):
    first_num = lst[0]
    last_num = lst[-1]
    if first_num == last_num:
        return True
    else:
        return False

print("The result is", checkFirstLast([10, 20, 30, 40, 10]))

#Print the pattern
def pattern():
    ptrn = "**"
    print(ptrn)
    for i in range(10):
        ptrn = ptrn + "**"
        print(ptrn)

pattern()


def increasingValues():
    for count in range(10):
        for i in range(count):
            print(count, end=" ")
        print("")

increasingValues()

#create a new list when given two lists
def newList(some_list):
    a = []
    b = []
    lngth = len(some_list)
    for i in range(lngth):
        if some_list[i] %2 == 0:
            a.append(some_list[i])
        else:
            b.append(some_list[i])
    print(a) 
    print(b)

newList([1,2,3,4,5,6,7,8])



