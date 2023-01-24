# Find the largest value in a list
def find_highest(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max


print(find_highest([6, 9, 100, 2, 45, 7]))


# Print Fizz, Buzz, or Fizzbuzz depending on whether a number passed is divisible by 3, 5, or both
def fizzbuzz(num):
    answer = "answer"
    if num % 3 == 0 and num % 5 == 0:
        answer = "Fizzbuzz"
    elif num % 3 == 0:
        answer = "Fizz"
    elif num % 5 == 0:
        answer = "Buzz"
    return answer


print(fizzbuzz(85))


# Given a list of numbers, return a new list with the first value being the sum of the even numbers and the second value being the sum of the odd numbers
def sumodd_even(lst):
    even_sum = 0
    odd_sum = 0
    new_list = []
    for i in lst:
        if i % 2 == 0:
            even_sum += i
        elif i % 2 != 0:
            odd_sum += i
    new_list.append(even_sum)
    new_list.append(odd_sum)
    return new_list


print(sumodd_even([1, 2, 3, 4, 7, 8, 9, 11, 45]))


# Find the count of values in a given string
def vowel_count(str):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    sum = 0
    for i in str:
        for x in vowels:
            if i == x:
                sum += 1
    return f"The total number of vowels is: {sum}"


print(vowel_count('Good morning!'))


# Create a list of multiples
def multiples(a, b):
    multiples_list = []
    for x in range(0, b+1):
        multiples_list.append(x*a)
    return multiples_list


print(multiples(5, 8))


# Scottish screaming
def screaming(str):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    for i in str:
        if i in vowels:
            str = str.replace(i, 'e')
    return str.upper()


print(screaming('Good morning!'))


#Calculate letters shared between two words
def letters_shared(word1, word2):
    count = 0
    for x in word1:
        if x in word2:
            count +=1
    return f'These words share {count} letters'

print(letters_shared('red', 'bed'))


#integer digit count
def integer(num):
    count = 0
    for x in str(num):
        count +=1
    return count

print(integer(8934))



