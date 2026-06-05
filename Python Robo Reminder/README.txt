README FOR PYTHON ROBO REMINDER APP
-------------------------------------
*Initially intended for personal use. No current plans for deployment to the commercial market*


The purpose of this program is to store and send the appropriate information for reminders. It checks the database and sends a reminder through email using a dedicated gmail account. A feature is being added that will be able to parse an incoming email to allow for management of reminders.

OPERATIONAL GUIDE
--------------------------------------

*What does this app do?
- The main script of this app, 'reminder.py', is to read reminders stored in a database and send an email with the information to the correct person's email address. The plans are currently to have the script run automatically once a day. In the future, more accessability will be added to include more options for customization for things like changing the frequency of the reminders and potentially the ability to change reminders through email for external users. This would allow for the user to have full control of the reminders through emails, with limitations of course.

* How do I make changes to the database that stores the reminders?
- You run the 'database.py' script to create, read, update and delete data from the database. This file is a work in progress.

*What does the 'scraper.py' file do?
- The purpose fo the 'scraper.py' file is to parse through incoming emails. This file is a work in progress.

*IN DEVELOPMENT, 2026*