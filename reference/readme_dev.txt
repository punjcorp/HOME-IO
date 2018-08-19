# Activate Virtual Env
C:\Users\MY\Envs\HOME-IO\Scripts\activate.ps1

# Start Application at localhost:8000
python .\manage.py runserver


# Step 1 -  Make Model migrations 
#           The app name has been defined in settings.py
python manage.py makemigrations HOME_IO_UI


# Step 2 -  Make migrations sql file for execution in DB
#           The file name is generated based on the step 1
#           These sqls are for reference purposes
python manage.py sqlmigrate HOME_IO_UI 0003

# Step 3 -  Migrate all the database changes which has been 
#           created as part of Step 1
python manage.py migrate

# To explore the DB shell to CRUD in models
python manage.py shell