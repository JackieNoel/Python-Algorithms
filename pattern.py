#Print half diamond pattern
def pattern(num):
    for i in range(num):
        for x in range(0, i+1):
            print("*", end="")
        print()
    for i in range(1, num):
        for x in range(i, num):
            print("*", end="")
        print()

pattern(7)
pattern(12)


#Remove items from list
def ordering(lst):
    while lst:
        lst.pop()
        print(lst)

ordering([6,4,9,10,17,3,-2,0])
