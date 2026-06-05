# SQLite3 Database Python Script for 'Python Robo Reminder' app.
Version = 1.3
#-------------Imports--------------
import sqlite3             #Used for storing data relating to reminders
import os                  #Used to show filepath for database (testing purposes)

#-------------Functions------------
def main():
   print('Welcome to the Python Robo Reminder database management menu! This is currently a work in progress.')
def create_table():
    try:
        table_name = input('Enter the name of the table you want to create: (letters only)\n')
        #Input Sanitization
        table_name = table_name.strip()         #Used to remove leading and tailing whitespace (.strip())
        table_name = table_name.lower()         #Used to convert input to lowercase (.lower())
        final_table_name = ''.join(char for char in table_name if char.isalnum())
        # The rest of the information for table creation goes here
        conn = sqlite3.connect('reminders.db')
        cursor = conn.cursor()
        print('SQL Connection open')
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {final_table_name} (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   email TEXT UNIQUE
            )
        """)
    except sqlite3.Error as error:
        print('Error occured: ', error)
    finally:
        conn.commit()
        cursor.close()
        conn.close()
        print('SQL Connection closed')
def add_user():
    pass
def query_data():
    pass
def delete_user():
    pass
def reference_guide(do_not_call):
    try:
        conn = sqlite3.connect('reminders.db')    #Opens connection to database (Creates one if not initially found)
        cursor = conn.cursor()                    #Creates a connection to a cursor to execute SQlite3 commands
        print('SQLite Connection open')

        #--------SQLite3-commands-go-here-------
        #Creates table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   email TEXT UNIQUE
                )
            """)

        # #Insert data into table, Using placeholders (?) to prevent SQL injection
        user_data = ('Kody', 'email@gmail.com')
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", user_data)

        conn.commit()    #Saves the changes

        #Query data
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]} - Name: {row[1]} - Email: {row[2]}')

    except sqlite3.Error as error:
        print('Error ocurred: ', error)

    finally:
        cursor.close()    #Closes the connection to the cursor
        conn.close()    #Closes connection to database
        print('SQLite Connection closed')
#-------------Main-Code------------
if __name__ == "__main__":
    main()
#---------------Test-Code---------------------------
#print(f"Look for the file here: {os.path.abspath(db_name)}")    #Shows the filepath for the created test database