web: gunicorn FTL_activity_periods.wsgi:application
release: python manage.py collectstatic --noinput && python manage.py migrate && python manage.py populate_db
