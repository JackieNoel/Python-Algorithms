def merge_sort(input1, input2):
    new_array = []
    index1 = index2 = 0
    if len(input1) ==0:
        return input2
    if len(input2) == 0:
        return input1
    while len(new_array) < len(input1) + len(input2):
        if len(input1) <= len(input2):
            new_array.append(input1[index1])
            index1 +=1
        else:
            new_array.append(input2[index2])
            index2 +=1
        if index2 == len(input2):
            new_array += input1[index1:]
            break
        if index1 == len(input1):
            new_array += input2[index2:]
            break
    return new_array

print(merge_sort([5,4,3,2,1], [6,7,8,9,0]))

    