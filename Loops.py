num = 1
for i in range(1, 11):
    for x in range(1, i+1):
        print(x, end=" ")
    print("")


def sum_of_nums(val):
    sum = 0
    for a in range(0, val+1):
        sum += a
    return sum

print(sum_of_nums(88))

int = 2
for i in range(0, 10):
    product = i * int
    print(product)

def num_loop(lst):
    new_list = []
    for i in range(len(lst)):
        if lst[i]%5 == 0:
            if lst[i] < 150:
                new_list.append(lst[i])
    return new_list

print(num_loop([12, 75, 150, 180, 145, 525, 50]))
