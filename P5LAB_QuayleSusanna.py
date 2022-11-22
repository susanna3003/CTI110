def days_in_feb(user_year):
    is_leap_year = False
       #user_year = int(input())
   
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                is_leap_year = True
            else:
                is_leap_year = False
        else:
            is_leap_year = True
    else:
        is_leap_year = False

    if is_leap_year:
        days = 29
    else:
        days = 28
    
    return days

if __name__ == '__main__':
    user_input = int(input())
    days_print = days_in_feb(user_input)
    
    print(f'{user_input} has {days_print} days in February.')