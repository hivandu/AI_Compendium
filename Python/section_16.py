'''
Author: Hivan Du
mail: doo@hivan.me
LastEditors: Hivan Du
LastEditTime: 2024-08-01 15:54:40
'''
import time
import os
import calendar

def showdate(year, month):
    res = calendar.monthrange(year, month)
    days = res[1]  # Number of days in the current month
    week = res[0] + 1  # The first day of the month is which weekday

    print(f'========= {year} Year {month} Month =========')
    print('Mon   Tue   Wed   Thu   Fri   Sat   Sun')
    print('='*39)
    
    # Print the calendar
    d = 1
    while d <= days:
        # Loop through the week
        for i in range(1, 8):
            # Check if it should print
            if d > days or (d == 1 and i < week):
                print('      ', end='')
            else:
                print('{:0>2d}'.format(d), end="    ")
                d += 1
        print()

# Get the current time
dd = time.localtime()
year = dd.tm_year
month = dd.tm_mon

while True:
    os.system('clear')  # Clear the screen (use 'cls' for Windows)
    showdate(year, month)
    print(' < Previous Month     Next Month > ')
    c = input('Enter your choice "<" for previous month or ">" for next month, or "exit" to quit: ')
    
    # Handle user input
    if c == '<':
        month -= 1
        if month < 1:
            month = 12
            year -= 1
    elif c == '>':
        month += 1
        if month > 12:
            month = 1
            year += 1
    elif c.lower() == 'exit':
        break
    else:
        print('Invalid input. Please enter "<" for previous month, ">" for next month, or "exit" to quit.')
        time.sleep(2)  # Wait for 2 seconds before continuing to let the user see the message