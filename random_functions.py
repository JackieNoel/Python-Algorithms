def lesser_value(a,b):
    if a < b:
        print("The lesser value is:", a)
        return

    else:
        print("The lesser value is:", b)
        return

lesser_value(2,6)
lesser_value(9,0)



def make_twenty(c,d):
    sum = c + d
    if sum == 20:
        return True
    else:
        return False

print(make_twenty(19,1)) 
print(make_twenty(3,2)) 


def almost_there(n):
    if 100 - n <= 10:
        return True
    elif 200 - n <= 10:
        return True
    else:
        return False

print("********")
print(almost_there(99)) 
print(almost_there(190))
print(almost_there(7)) 
print(almost_there(25)) 
print(almost_there(-20)) 


def area_computer(len, wdth):
    area = len * wdth
    print(f"The area of the rectangle is,", area, "square units")

area_computer(10,10)
area_computer(15, 6) 


def most_common(str):
    for x in str:
        print(x)



