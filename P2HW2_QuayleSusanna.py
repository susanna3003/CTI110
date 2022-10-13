# CTI-110
# P2HW2 - List
# Susanna Quayle
# 10/13/2022
#

print ('Enter grade for Module 1: ')
mod1 = float(input())
print ('Enter grade for Module 2: ')
mod2 = float(input())
print ('Enter grade for Module 3: ')
mod3 = float(input())
print ('Enter grade for Module 4: ')
mod4 = float(input())
print ('Enter grade for Module 5: ')
mod5 = float(input())
print ('Enter grade for Module 6: ')
mod6 = float(input())
print()
gradeList = [mod1, mod2, mod3, mod4, mod5, mod6]
avgGrade = sum(gradeList) / len(gradeList)
print('------------Results------------')
print(f'Lowest Grade:      {min(gradeList)}')
print(f'Highest Grade:     {max(gradeList)}')
print(f'Sum of Grades:     {sum(gradeList)}')
print(f'Average:           {avgGrade:.2f}')
print(f'{"-"*50}')

# get info from user for grades for modules 1 - 6
# sort grades into list
# get min, max, sum, and avg from grade list
# display results

