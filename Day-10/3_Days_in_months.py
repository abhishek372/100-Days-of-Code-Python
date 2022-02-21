# Program to give the number of days in the months using function

leap = True

def is_leap(year):
    '''Checks whether the year is leap or not.
        And, return the leap.'''
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return leap
            else:
                return not leap
        else:
            return leap
    else:
        return not leap
    

# Gives days of month
def days_in_month(year, month):
    '''Takes year and month and returns the days in that month.'''
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        return 29               # In leap year, 29 days in February.
    total_days = month_days[month-1]
    return total_days


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)

print(days)


