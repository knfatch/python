# SQLite3 Database Python Script for 'Python Robo Reminder' app.
Version = 1.2
#-------------Imports--------------
import sqlite3             #Used for storing data relating to reminders

#-------------Functions------------

#-------------Main-Code------------
try:
    conn = sqlite3.connect('reminders.db')    #Opens connection to database (Creates one if not initially found)
    cursor = conn.cursor()    #Creates a connection to a cursor to execute SQlite3 commands
    print('SQLite Connection open')

    #SQLite3 commands go here

    conn.commit()    #Saves the changes

except sqlite3.Error as error:
    print('Error ocurred - ', error)

finally:
    cursor.close()    #Closes the connection to the cursor
    conn.close()    #Closes connection to database
    print('SQLite Connection closed')