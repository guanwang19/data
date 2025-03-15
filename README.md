            20250315 version of course_platform:
            course_platform/
│── manage.py
│── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│── videos/  # Directory to store video files
│   ├── course1/
│   │   ├── jamesdata01.mp4
│   │   ├── jamesdata02.mp4
│   │   └── ...
│   ├── course2/
│   │   ├── jamesdata01.mp4
│   │   ├── jamesdata02.mp4
│   │   └── ...
│   └── ...
├── courses/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── templates/
│   │   └── courses/
│   │       ├── course_list.html
│   │       ├── course_detail.html
│   │       └── ...
│   └── migrations/
│       └── ...
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── templates/
│   │   └── users/
│   │       ├── login.html
│   │       ├── signup.html
│   │       └── ...
│   └── migrations/
│       └── ...
├── payments/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── templates/
│   │   └── payments/
│   │       ├── checkout.html
│   │       ├── invoice.html
│   │       └── ...
│   └── migrations/
│       └── ...
├── cart/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── templates/
│   │   └── cart/
│   │       ├── cart_detail.html
│   │       └── ...
│   └── migrations/
│       └── ...
├── chatbot/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── templates/
│   │   └── chatbot/
│   │       └── ...
│   └── migrations/
│       └── ...
├── support/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── templates/
│   │   └── support/
│   │       └── ...
│   └── migrations/
│       └── ...
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/
│       └── pages/
│           ├── Home.js
│           └── ...
└── templates/
    ├── base.html
    └── ...

            20250301 version of course_platform:
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
            │   ├── tempelates
            │   │  │── users/
            │   │  │   ├── tempelates
            │   ├── views.py
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
        │   │   │   ├── Home.js
        │   │   │   ├── Signup.js
        │   │   │   ├── Login.js
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

##
Go to Node.js official site (https://nodejs.org/)
Download LTS (Long-Term Support) version (recommended for stability).
Run the installer and check the box for "Add to PATH" during installation.

## Initialize a New package.json
 npm init -y

##
1️⃣ Learn Express.js (handling routes, middleware, JWT authentication)
2️⃣ Learn React Components (props, state, hooks, context)
3️⃣ Connect PostgreSQL with Node.js
4️⃣ Build a Full-Stack App (Course Platform) 

##
Use Django Rest Framework (DRF) for API
Use Django’s AbstractBaseUser for custom user models
Use rest_framework_simplejwt for token-based authentication
Do NOT expose sensitive endpoints (use CSRF protection & validation)
Frontend should handle API calls (React for sign-up & sign-in)
Use Email Verification for Activation
Follow RESTful principles (return JSON responses)

##
CREATE USER django_user WITH PASSWORD 'post2025';
GRANT CONNECT ON DATABASE course_db TO django_user;
GRANT USAGE ON SCHEMA public TO django_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO django_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO django_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO django_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO django_user;
