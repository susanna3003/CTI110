#This program calculates and displays travel expenses
#09/22/2022
#CTI-110 P1HW2 - Travel Expense
#Susanna Quayle
print ('This program calculates and displays travel expenses.')
print ()
print ('Enter Budget:' , end=' ')
budget = float(input())
print ()
print ('Enter your travel destination:' , end=' ')
destination = input()
print ()
print ('How much do you think you will spend on gas?' , end=' ')
gasMoney = float(input())
print ()
print ('Approximately, how much will you need for accomodation/hotel?' , end=' ')
hotel = float(input())
print ()
print ('Last, how much do you need for food?' , end=' ')
food = float(input())
print ()
print ('----------Travel Expenses------------')
print ('Location:' , destination)
print ('Initial Budget:' , budget)
print ()
print ('Fuel:' , gasMoney)
print ('Accomodation:' , hotel)
print ('Food:' , food)
remainingBalance = budget - (gasMoney + hotel + food)
print ()
print ('Remaining Balance:' , remainingBalance)

#Declare Real budget, gasMoney, hotel, food, remainingBalance
#Declare String destination
#Display "Enter Budget:" , budget
#Display "Enter destination:" , destination
#Display "How much spent on gas?" , gasMoney
#Display "How much spent on hotel?" , hotel
#Display "How much spent on food?" , food
#set remainingBalance = budget - (gasMoney + hotel + food)
#Display "Remaining Balance:" , remainingBalance */
