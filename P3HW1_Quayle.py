# CTI - 110 Debugging Exercise
# Quayle 


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
numGrades = len(grades)
avg = total / numGrades

# determine letter grade for average
print(f'------------Results------------')
print(f'Lowest Grade:        {low:.2f}')
print(f'Highest Grade:       {high:.2f}')
print(f'Sum of Grades:       {total:.2f}')
print(f'Average:             {avg:.2f}')
print(f'-------------------------------------')


if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')






