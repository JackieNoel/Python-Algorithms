#convert Roman numerals
def roman_ints(str):
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
    }
    sum = 0
    for i in range(len(str)-1):  # this will allow me to access more than just the one index
        if romans[str[i]] < romans[str[i+1]]:
            # roman_ints['X']        roman_ints['X']
            sum -= romans[str[i]]
        else:
            sum += romans[str[i]]
    sum += romans[str[len(str)-1]]
    return sum


print(roman_ints('XXIV'))
print(roman_ints('LXXXVII'))
print(roman_ints('CXI'))
print(roman_ints('CXLVIII'))



#Fibonnaci numbers
def fib_nums(num):
    one = 1
    if num == 0:
        fib = []
    elif num == one:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while one < (num -1):
            fib.append(fib[one] + fib[one-1])
            one +=1
    return fib


print(fib_nums(3))
print(fib_nums(6))
print(fib_nums(10))


#Print less than 10
def less_than_10(lst):
    new_list = []
    for x in lst:
        if type(x) == int and x < 10:
            new_list.append(x)
    return f"This is the new list: {new_list}"


print(less_than_10([7,6,4,9,"hello", -1, 'frank']))


#Divisors
def divisors(num):
    divisor_list = []
    for x in range(num+1):
        divisor_list.append(num * x)

    return divisor_list

print(divisors(12))
print(divisors(4))


