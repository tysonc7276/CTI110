# P3HW1 - Debugging Homework
# Tyson

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 59
    

    
    score = int(input('Enter grade: '))

    if score > 89:
        print('Your grade is: A')
    elif score > 79:
        print('Your grade is: B')
    elif score > 69:
        print('Your grade is: C')
    elif score > 59:
        print('Your grade is: D')
    else:
        print('Your grade is: F')


# program start
main()
