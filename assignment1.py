#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2024
Program: assignment1.py 
Author: "Rafien Mohammed"
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    ...

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    #The below code splits input date into year month and day strings with - as a separater
    str_year, str_month, str_day = date.split('-')  

    #converst year month and day strings to integers 
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    #This adds 1 day to calculate the next day
    tmp_day = day + 1  # next day


    #Checks if day exceeds the maximum days at the current month
    if tmp_day > mon_max(month, year): #If tmp_day exceeds it resets the day to the start of the next month
        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day #if day is valid it keeps the entered day
        tmp_month = month + 0 #and the month remains unchanged

    if tmp_month > 12: #this checks if month exceeds beyond 12
        to_month = 1 #if month exceeds then it resets to one
        year = year + 1 #and a year is added
    else:
        to_month = tmp_month + 0  #if month is valid under 12 then it keeps the month

    next_date = f"{year}-{to_month:02}-{to_day:02}" #This formats the calculated entry into the YYYY-MM-DD format

    return next_date


def usage():
    '''
    Print program usage message to the user and exit the program

    '''
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    if year % 4==0:
        if year % 100 != 0 or year % 400 == 0;
        return True
    return False


def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    ...

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    ...

if __name__ == "__main__":
    ...
