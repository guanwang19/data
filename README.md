            course_platform/
            │── manage.py
            │── config/
            │   ├── settings.py
            │   ├── urls.py
            │   ├── wsgi.py
            │   ├── asgi.py
            │── videos/ (Stores video files: data01.mp4, data02.mp4, ..., data32.mp4)
            │── courses/
            │   ├── models.py
            │   ├── views.py
            │   ├── serializers.py
            │   ├── urls.py
            │── users/
            │   ├── models.py
            │   ├── views.py
            │   ├── serializers.py
            │   ├── urls.py
            │── payments/
            │   ├── models.py
            │   ├── views.py
            │   ├── serializers.py
            │   ├── urls.py
            │── chatbot/
            │   ├── models.py
            │   ├── views.py
            │   ├── serializers.py
            │   ├── urls.py
            │── support/
            │   ├── models.py
            │   ├── views.py
            │   ├── serializers.py
            │   ├── urls.py
            │── frontend/
            │   ├── public/
            │   ├── src/
            │   │   ├── components/
            │   │   ├── pages/
            │   │   ├── App.js
            │   │   ├── index.js
            │   │   ├── api.js
            │   ├── package.json
            │   ├── .env
        
## Summary of Folder Assignments

Table Name	    Django Model Class	        File
users	        User	                    users/models.py
courses	        Course	                    courses/models.py
videos	        Video	                    courses/models.py
user_progress	UserProgress	            courses/models.py
payments	    Payment	                    payments/models.py
video_access	VideoAccess	                courses/models.py
chatbot_queries	ChatbotQuery	            chatbot/models.py
support_emails	SupportEmail	            support/models.py

## To run:
rm -rf */migrations/*.py
python manage.py makemigrations
python manage.py migrate

## Use manage.py for various Django tasks:

# Start the Django development server
python manage.py runserver

# Create a new database migration
python manage.py makemigrations

# Apply migrations to the database
python manage.py migrate

# Create a superuser for Django admin
python manage.py createsuperuser

# Check for project issues
python manage.py check

## create SECRET_KEY, saved in .env
python -c "import secrets; print(secrets.token_urlsafe(50))"