#CTI-110
#P3HW2 Salary Calculator
#10/25/2022
#Quayle Susanna

#this program will ask for employee name, hours worked, pay rate and calculate OT pay, regular pay, and gross pay


#get user info

name = input("Enter employee's name: ")
numHours = float(input("Enter number of hours worked: "))
payRate = float(input("Enter employee's pay rate: "))

#calculate overtime and pay

if numHours > 40:
    overTime = numHours - 40
else:
    overTime = 0.0
    

overTimePayRate = (payRate / 2) + payRate
overTimePay = overTime * overTimePayRate
regHourPay = numHours * payRate
grossPay = overTimePay + regHourPay

#display employee salary info

print(f'{"-"*35}')
print(f'Employee name:   {name}')
print()
print(f'Hours Worked   Pay Rate   OverTime   OverTime Pay     RegHour Pay     Gross Pay')
print(f'{"-"*100}')
print(f'{numHours}           {payRate}       {overTime}        {overTimePay}            ${regHourPay}        ${grossPay}')


#Program asks user for employee name, hours worked, and pay rate
#Calculate overtime from hours worked
#Calculate overtime pay, regular pay, and gross pay
#Display employee name, hours worked, pay rate, overtime, overtime pay, regular pay, and gross pay


