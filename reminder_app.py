# Reminder app that sends email/text/notification
#-------------Imports--------------
import datetime as dt   #Used for tracking when to send remind notifications
from smtplib import SMTP  #Used for emailing (Simple Mail Transfer Protocol)

#-------------Functions------------
def today_check(now):
    if now.day == 1:
        suffix = "st"
    elif now.day == 2:
        suffix = "nd"
    elif now.day == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return now.day, suffix
def month_check(current_month):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    name_of_month = months[current_month - 1]
    return name_of_month
def main():
    pass

#-------------Variables------------
now = dt.datetime.now()  #Assigns the current date and time to variable 'now'
today, suffix = today_check(now)   #Assigns the current day of the month to 'today' and the appropriate suffix to 'suffix'
month_num = now.month   #Assings 'month_num' to current number of month
curr_month = month_check(month_num)     #Assigns the name of the month to 'curr_month'

#-------------Main-Code------------
if __name__ == "__main__":
    main()

#------------Testing---------------
print(now)  #Prints the Date (YYYY-MM-DD) and Time (24:00:00.000000)
print(f"Current Day: {today}{suffix}")
print(f"Current Month: {curr_month} ({month_num})")