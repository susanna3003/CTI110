#CTI-110
#P4HW2 - Salary Calculator
#11/15/2022
#Susanna Quayle

#this program will ask for employee name, hours worked, pay rate and calculate OT pay, regular pay, and gross pay, then loop until user stops program


#get user info

print("Enter employee's name or 'None' to terminate: ", end='')
user_input = input()
reg_pay = []
ot_pay = []
num = 0
while user_input != 'None':
    print(f"How many hours did {user_input} work? ", end='')
    numHours = float(input())
    print(f"What is {user_input}'s pay rate? ", end='')
    payRate = float(input())
   
    
#calculate overtime and pay

    if numHours > 40:
        overTime = numHours - 40
        numHours = numHours - overTime
    else:
        overTime = 0.0
    

    overTimePayRate = (payRate / 2) + payRate
    overTimePay = overTime * overTimePayRate
    regHourPay = numHours * payRate
    grossPay = overTimePay + regHourPay
    allHours = numHours + overTime

#display employee salary info

    print()
    print(f'Employee name: {user_input}')
    print()
    print(f'Hours Worked   Pay Rate   OverTime   OverTime Pay     RegHour Pay     Gross Pay')
    print(f'{"-"*100}')
    print(f'{allHours:<15.2f}{payRate:<11.2f}{overTime:<11.2f}{overTimePay:<17.2f}${regHourPay:<15.2f}${grossPay:<14.2f}')
    print()
    print("Enter employee's name or 'None' to terminate: ", end='')
    user_input = input()
    num += 1
    reg_pay.append(regHourPay)
    ot_pay.append(overTimePay)
    totalGross = sum(reg_pay) + sum(ot_pay)
    
print()
print(f"Total number of employees entered: {num}")
print(f"Total amount payed for overtime: ${sum(ot_pay)}")
print(f"Total amount payed for regular hours: ${sum(reg_pay)}")
print(f"Total amount payed in gross: ${totalGross}")


#Program asks user for employee name, hours worked, and pay rate
#Calculate overtime from hours worked
#Calculate overtime pay, regular pay, and gross pay
#Display employee name, hours worked, pay rate, overtime, overtime pay, regular pay, and gross pay
#Run loop until user stops program with 'None'
#When loop terminates display number employees entered, total OT pay, total regular pay, and total gross pay
