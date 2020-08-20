# User Activity Periods: FullThrottle Labs

### Introduction:
The _**User Activity Periods**_ application is an API service that provides the list of users along with their timezones and active period(start time and end time) in the application.

### Follow the steps to _run the application_:

1. Install all the required packages(python modules):

    ```pip install -r requirements.txt```

2. Migrate all the models to the database(Assuming that the DB used is sqlite3)
 
    ```python manage.py migrate```
    
3. When the migrations are successfully completed, we can run the server:

    ```python manage.py runserver```
    
    If the steps are followed correctly, the server will be up and running.
 
 4. To gather all static files(not necessary as of now, as the application does not serve ant static contents):
   
    ```python manage.py collectstatic```
    
 5. Populating dummy data in the Database(this will create 100 random users and their respective activity periods in DB):
    
    ```python manage.py populate_db``` [NB: ignore the timezone warnings]
 
 ## API Documentation:
 ### API Endpoints:
  - ```<base_url>/user/user_activity_periods/``` [GET], retrieves the list of all user and their respective activity periods.
 
 ## Heroku:
 Heroku instance: ```https://ftl-user-activity.herokuapp.com/user/user_activity_periods/``` [GET]
