Version = 1.3
#-------------Imports--------------
import datetime as dt      #Used for tracking when to send remind notifications
import smtplib             #Used for emailing (Simple Mail Transfer Protocol)
import email.message       #Used to format an email message
import os                  #Used for environment variables for storing sensitive data
#-------------Functions------------
def date_check():
    now = dt.datetime.now()                   #Assigns the current date and time to variable 'now'
    today = now.day                           #Assigns the current day of the month to 'today' and the appropriate suffix to 'suffix'
    if today == 1:
        suffix = "st"
    elif today == 2:
        suffix = "nd"
    elif today == 3:
        suffix = "rd"
    else:
        suffix = "th"
    day_of_week = now.strftime('%a')          #Assigns 'day_of_week' to the day of the week. 'A' for full day. 'a' for abbreviated day.
    month_num = now.month                     #Assigns 'month_num' to current number of month
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    name_of_month = months[month_num - 1]     #Assigns the name of the month to 'name_of_month'
    return now, today, suffix, day_of_week, month_num, name_of_month
def check_reminders(day_of_week): #Needs finished
    try:
        #Code for checkng database for reminders should go here
        pass                      
    except Exception as e:
        print(f'Something failed due to: {e}')
    finally:
        print('Reminders have been checked.')
def format_email(sender, recipient, month, day, suffix, day_of_week, reminder):
    try:
        msg = email.message.EmailMessage()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = 'PYTHON ROBO REMINDER'
        msg.set_content('Today\'s Date:\n'           #Newline char such as '\n' are needed to go to next line.
                        f'{day_of_week}, {month} {day}{suffix}\n'
                        '\n'
                        'Reminders:\n'
                        f'{reminder}\n'
                        '\n'
                        'Upcoming Reminders:\n'
                        '*upcoming reminders go here*'
                        )
        print('Email formatted successfully.')
        return msg
    except Exception as e:
        print(f'Email failed to format due to {e}')
def send_email(sender, password, message, port, server):
    try:
        with smtplib.SMTP(server, port) as s:    #Using 'with' and 'as s:' ensures that the connection ends automatically.
            s.starttls()
            s.login(sender, password)
            s.send_message(message)
            print("Message Sent Successfully")
    except Exception as e:
        print(f'Failed to send: {e}')
#---------Server-Details-------------
SMTP_SERVER = 'smtp.gmail.com'
PORT = 587                           #PORT '587' for STARTTLS
#-----------Email-Details------------
app_pass = str(os.environ.get('GMAIL_APP_PASS'))        #Environment variable set in User Variables on OS
sender = str(os.environ.get('ROBO_SENDER'))             #Environment variable set in User Variables on OS
recipient = str(os.environ.get('TEST_RECIPIENT'))       #Environment variable set in User Variables on OS            
recipient2 = str(os.environ.get('ROBO_SENDER'))         #Assigned to same email as sender for testing purposes
#-------------Main-Code------------
if __name__ == "__main__":
    now, today, suffix, day_of_week, month_num, name_of_month = date_check()
    reminder = check_reminders(day_of_week)
    message = format_email(sender, recipient2, name_of_month, today, suffix, day_of_week, reminder)
    send_email(sender, app_pass, message, PORT, SMTP_SERVER)
#-------Testing-and-Debugging------
    # print(now)    #Prints the Date (YYYY-MM-DD) and Time (24:00:00.000000)
    # print(f"Current Day: {today}{suffix}")
    # print(f'Day of the Week: {day_of_week}')
    # print(f"Current Month: {name_of_month} ({month_num})")
    # print(f'Message: {reminder}')