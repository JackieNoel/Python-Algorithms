# A Narcissistic Number is a positive number which is the sum of
# its own digits, each raised to the power of the number of digits in a given number
# For example, take 153 (3 digits), which is narcisstic:
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

def narc_num(num):
    sum = 0
    for i in str(num):
        sum += (int(i) ** len(str(num)))
    return sum == num #this will return True or False

print(narc_num(153))
print(narc_num(455))
print(narc_num(0))



# # Given two strings, the second string contains characters that must be removed from the first. Return the
# resultant string.

def two_numbs(str1, str2):
    new_word = ""
    for x in str1:
        if x not in str2:
            new_word += x
    return new_word
        

print(two_numbs('word', "door"))
print(two_numbs('second', "felcon"))
    
