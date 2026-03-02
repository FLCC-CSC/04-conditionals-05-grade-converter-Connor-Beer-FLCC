# FILE NAME - grade_converter.py
# NAME: Connor Beer
# DATE: March 2, 2026
# BRIEF DESCRIPTION: Converts a number into a grade 

########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    grade_converter()

def grade_converter():
    print('===== Grade Converter =====')

    percent = int(input('Enter a numerical grade (1-100): '))

    if percent > 100:
        print('A+')
    elif percent >= 90:
        print('A')
    elif percent >= 80:
        print('B')
    elif percent >= 70:
        print('C')
    elif percent >= 65:
        print('D')
    else:
        print('F')

main()

########### END YER CODE ABOVE THIS LINE ###########

########################################
#          REFLECTION QUESTIONS
########################################

'''
1. What is something you would tell a future student to be careful about when
   doing this lab?
Be careful to use elif and not else until the last code block
'''