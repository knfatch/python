# SQLite3 Database Python Script for 'Python Robo Reminder' app.
Version = 1.3
#-------------Imports--------------
import sqlite3             #Used for storing data relating to reminders
import os                  #Used to show filepath for database (testing purposes)

#-------------Functions------------
def main():
    try:
        print('Welcome to the Python Robo Reminder database management menu! This is currently a work in progress.')
        print('Create Table - 1    Delete User - 2')
        print('Add User - 3        Query Data - 4')
        print('Delete Table - 5    Show Tables - 6')
        print("Press 'q' or 'Q' to exit program.")
        user_input = int(input('Select your option.\n'))
        print('-----------------------------')
        while user_input != 'q' or user_input != 'Q':    
            if user_input == 1:
                create_table()
            elif user_input == 2:
                delete_user()
            elif user_input == 3:
                add_user()
            elif user_input == 4:
                query_table()
            elif user_input == 5:
                delete_table()
            elif user_input == 6:
                show_tables()
            else:
                print('Invalid Selection.')
            print('-----------------------------')
            print('Create Table - 1    Delete User - 2')
            print('Add User - 3        Query Data - 4')
            print('Delete Table - 5    Show Tables - 6')
            print("Press 'q' or 'Q' to exit program.")
            user_input = int(input('Select your option.\n'))
    except Exception as e:
        print(f'Something failed due to: {e}')
    finally:
        pass
def create_table():
    try:
        table_name = input('Enter the name of the table you want to create: (lowercase letters only)\n')
        #Input Sanitization
        stripped_table_name = table_name.strip()         #Used to remove leading and tailing whitespace (.strip())
        lower_table_name = stripped_table_name.lower()         #Used to convert input to lowercase (.lower())
        final_table_name = ''.join(char for char in lower_table_name if char.isalpha())
        # The rest of the information for table creation goes here
        conn = sqlite3.connect('reminders.db')
        cursor = conn.cursor()
        print('SQL Connection open')
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {final_table_name} (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   email TEXT UNIQUE
            )
        """)
    except sqlite3.Error as error:
        print('Error occured: ', error)
    finally:
        conn.commit()
        print(f'The table, {final_table_name}, was created.')
        cursor.close()
        conn.close()
        print('SQL Connection closed')
def add_user():
    try:
        conn = sqlite3.connect('reminders.db')
        cursor = conn.cursor()
        print('SQL Connection open')
        # Add user to database code goes here
        user_table = str(input('Enter the table the user is being added to:\n'))
        user_name = str(input("Enter the name of the user you're adding:\n"))
        user_email = str(input('Enter the email of the user being added:\n'))
        user_data = (user_name, user_email)
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", user_data)
    except Exception as e:
        print(f'Something failed due to: {e}')
    finally:
        conn.commit()
        print('Changes saved.')
        cursor.close()
        conn.close()
        print('SQL Connection closed')
def query_table():
    try:
        conn = sqlite3.connect('reminders.db')
        cursor = conn.cursor()
        print('SQL Connection open')

        user_input = str(input('Enter the name of the table you want to query:\n'))
        lower_user_input = user_input.lower()
        user_input_table = ''.join(char for char in lower_user_input if char.isalpha())
        # Query data from database code goes here
        cursor.execute(f"SELECT * FROM {user_input_table}")
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]} - Name: {row[1]} - Email: {row[2]}')
    except Exception as e:
        print(f'Something failed due to: {e}')
    finally:
        cursor.close()
        conn.close()
        print('SQL Connection closed')
def delete_user():
    try:
        conn = sqlite3.connect('reminders.db')
        cursor = conn.cursor()
        print('SQL Connection open')

        # This code queries the user table to show current users
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]} - Name: {row[1]} - Email: {row[2]}')

        # Delete a user code goes here
        sql_query = 'DELETE FROM users WHERE id = ?'
        target_id = int(input('Select the ID of the user you want to delete:\n'))
        cursor.execute(sql_query, (target_id,))
    except Exception as e:
        print(f'Something failed due to: {e}')
    finally:
        conn.commit()
        print(f'Rows deleted: {cursor.rowcount}')
        cursor.close()
        conn.close()
        print('SQL Connection closed')
def delete_table():
    try:
        conn = sqlite3.connect('reminders.db')
        cursor = conn.cursor()
        print('SQL Connection open')

        #Code to delete, or 'drop', a table from the database
        user_input = str(input('Enter the name of the table you want to delete:\n'))
        lower_user_input = user_input.lower()
        user_input_table = ''.join(char for char in lower_user_input if char.isalpha())
        cursor.execute(f'DROP TABLE IF EXISTS {user_input_table}')

    except Exception as e:
        print(f'Something failed due to: {e}')

    finally:
        conn.commit()
        print('Table Deleted Successfully.')
        cursor.close()
        conn.close()
        print('SQL Connection closed')
def show_tables():
    try:
        conn = sqlite3.connect('reminders.db')
        cursor = conn.cursor()
        print('SQL Connection open')

        #Code for showing all current tables goes here
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            print(table[0])

    except Exception as e:
        print(f'Something failed due to: {e}')
    finally:
        cursor.close()
        conn.close()
        print('SQL Connection closed')
def reference_guide(do_not_call):
    try:
        conn = sqlite3.connect('reminders.db')    #Opens connection to database (Creates one if not initially found)
        cursor = conn.cursor()                    #Creates a connection to a cursor to execute SQlite3 commands
        print('SQLite Connection open')

        #--------SQLite3-commands-go-here-------
        #Creates table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   email TEXT UNIQUE
                )
            """)

        # #Insert data into table, Using placeholders (?) to prevent SQL injection
        user_data = ('Kody', 'email@gmail.com')
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", user_data)

        #Query data
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]} - Name: {row[1]} - Email: {row[2]}')

    except sqlite3.Error as error:
        print('Error ocurred: ', error)

    finally:
        conn.commit()    #Saves the changes
        cursor.close()    #Closes the connection to the cursor
        conn.close()    #Closes connection to database
        print('SQLite Connection closed')
#-------------Main-Code------------
if __name__ == "__main__":
    main()
#---------------Test-Code---------------------------
#print(f"Look for the file here: {os.path.abspath(db_name)}")    #Shows the filepath for the created test database