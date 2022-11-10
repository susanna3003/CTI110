# CTI-110
# PWHW1 - Score List
# Susanna Quayle
# 11/10/2022
#


print('How many scores do you want to enter?', end=' ')
numScores = int(input())
scoreNum = 1
score_list = []
print()
for scoreNum in range(numScores):
    print(f'Enter score #{scoreNum+1}:', end=' ')
    score = float(input())
    while score < 0 or score > 100:
        print()
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        print(f'Enter score #{scoreNum+1} again:', end=' ')
        score = float(input())
    score_list.append(score)
print()
print()

print(f'{"-"*15}Results{"-"*15}')
print(f'Lowest Score   :    {min(score_list)}')

score_list.remove(min(score_list))

avgGrade = sum(score_list) / len(score_list)

if avgGrade <= 100:
    grade = 'A'
    if avgGrade < 90:
        grade = 'B'
        if avgGrade < 80:
            grade = 'C'
            if avgGrade < 70:
                grade = 'D'
                if avgGrade < 60:
                    grade = 'F'

print(f'Modified List  :    {score_list}')
print(f'Scores Average :    {avgGrade:.2f}')
print(f'Grade          :    {grade}')
print(f'{"-"*40}')


#Get specific number of scores from user
#Use nested loop to get scores and save in list
#Find lowest grade and remove from list
#Get average and letter grade of scores
#Display Lowest score, list of scores, average score, and letter grade


        
    

        
    
    
