def Convert_money(val):
    Answer = {"Quarters": 0, "Dimes": 0, "Nickels": 0, "Pennies": 0}
    while val > 0:
        if val >= 25:
            Answer["Quarters"] += 1
            val -= 25
        elif val >= 10:
            Answer["Dimes"] += 1
            val -= 10
        elif val >= 5:
            Answer["Nickels"] += 1
            val -= 5
        elif val >= 1:
            Answer["Pennies"] += 1
            val -= 1

    return Answer


print(Convert_money(35))  
print(Convert_money(50))  
print(Convert_money(66)) 


def Age_to_days(age):
    year = 365
    conversion = age * year
    print(f"You are {conversion} days old!")


Age_to_days(32)

def perimeter_rectangle(len, width):
    perimeter = (len + width) *2
    print(f"The perimeter of your rectangle is {perimeter} units.")

perimeter_rectangle(10, 20)


def Convert_time(hour, min):
    min_amount = min * 60
    hour_amount = hour * 3600
    answer = min_amount + hour_amount

    print(f"There are {answer} seconds in your input!")


Convert_time(2, 2)


