import random
#ONLY KEEP THE LAST FEW
def one_last_few(arr, x):
    new_arr = []
    while x <= (len(arr)-1):
        print(arr[(len(arr)-x)]) #pick up here
        new_arr.append(arr[(len(arr)-x)])
        x +=1
    return new_arr 



print(one_last_few([10,8,4,3,6,1,7], 3)) 


#POOR KENNY
def whatHappensToday():
    random_weather = ["Tornado", "Flood", "Hurricane", "Mudslide", "Blizzard", "Drought", "Wildfire", "Thunderstorm", "Hail", "Lockdown"]
    randomNumber = random.randint(0,100)
    if randomNumber%5 == 0:
        print(randomNumber)
        print(random_weather[random.randint(0, len(random_weather)-1)])
    else:
        print(randomNumber)
        print("It's a beautiful sunny day!")


whatHappensToday()


#LETTER GRADE
def letter_grade(int):
    A_phrase = f"Score {int}, Grade A"
    B_phrase = f"Score {int}, Grade B"
    C_phrase = f"Score {int}, Grade C"
    D_phrase = f"Score {int}, Grade D"
    F_phrase = f"Score {int}, Grade F"
    if int <=100 and int > 89:
        return A_phrase
    elif int <=89 and int > 80:
        return B_phrase
    elif int <=79 and int > 70:
        return C_phrase
    elif int <=69 and int > 60:
        return D_phrase
    elif int <= 60:
        return F_phrase
    
print(letter_grade(65)) #D
print(letter_grade(95)) #A
print(letter_grade(75)) #C
print(letter_grade(85)) #B
print(letter_grade(25)) #F
