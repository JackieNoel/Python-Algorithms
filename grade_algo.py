def calculate_grades(lst):
    sum = 0
    if len(lst)== 3:
        for x in lst:
            sum += x
            # sum/len(lst)
        print(f'Your final grade is: {sum/len(lst)}')
    if len(lst)==2:
        for y in lst:
            sum += y
        print(f'You missed one or more assignments which affected your final grade is: {sum/3}')
    if len(lst)<=1:
        for z in lst:
            sum += z
        print(f'You missed two or more assignments and failed the course, your final grade is: {sum/3}')

calculate_grades([100,92,83])
calculate_grades([100,92])
calculate_grades([100])

def another_grader(lst):
    final_grade = 0
    for x in lst:
        final_grade += x
    average = final_grade/len(lst)
    if average >= 90 and average < 101:
        print(f'You completed all required assignments! You earned an A and your final grade is %{average}')
    if average >= 80 and average < 90:
        print(f'You completed most of the required assignments! You earned a B and your final grade is %{average}')
    if average >= 70 and average < 80:
        print(f'You completed some of the required assignments! You earned a C and your final grade is %{average}')
    if average >= 60 and average < 70:
        print(f'You completed very few of the required assignments! You earned a D and your final grade is %{average}')
    if average < 60 :
        print(f'You completed almost none of the required assignments! You failed this course, your final grade is %{average}')


another_grader([100, 98,100,40])
print('------------------')
another_grader([20, 0, 98, 35])
print('------------------')

