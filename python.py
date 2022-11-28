def add_it_up(val):
    sum = 0
    for num in range(val +1):
        sum = sum + num
    return sum

print(add_it_up(6))

def name_check(name):
    if name == "Bond" or name == "bond":
        print("Welcome on board 007")
    elif name != "Bond" or name != "bond":
        print(f"Good morning, {name}")

name_check("Bond")
name_check("Eric")
name_check("Bert")


def evens(val):
    if val%2 == 0:
        print(f"WOW, {val} is even!")
    else:
        print(f"Ahh, {val} is odd!")

evens(12)
evens(15) 


def count_words(str):
    count = 0
    for i in range(len(str)):
        if str[i] == "a":
            count = count +1
    print(f"This statement has {count} a's!")
        

count_words("My name is Jackie")
