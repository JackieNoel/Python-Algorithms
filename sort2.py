def organized_list(lst):
    num_list = []
    char_list = []
    word_list = []
    characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    new_list = []
    for x in lst:
        for y in characters:
            if x == y:
                char_list.append(x)
        if type(x)== int:
            num_list.append(x)
        if type(x)== str and x not in char_list:
            word_list.append(x)
    print(num_list, char_list, word_list)

    

organized_list(['racket', 1,'!', 9, 45, 'lavender', "pizza-pie", '@'])
