import os

project_structure = {
    "course_platform": [
        "manage.py",
        {"config": ["settings.py", "urls.py", "wsgi.py", "asgi.py"]},
        {"videos": []},
        {"courses": ["models.py", "views.py", "serializers.py", "urls.py"]},
        {"users": ["models.py", "views.py", "serializers.py", "urls.py"]},
        {"payments": ["models.py", "views.py", "serializers.py", "urls.py"]},
        {"chatbot": ["models.py", "views.py", "serializers.py", "urls.py"]},
        {"support": ["models.py", "views.py", "serializers.py", "urls.py"]},
        {"frontend": [
            {"public": []},
            {"src": [
                {"components": []},
                {"pages": []},
                "App.js",
                "index.js",
                "api.js"
            ]},
            "package.json",
            ".env"
        ]}
    ]
}

def create_structure(base_path, structure):
    for item in structure:
        if isinstance(item, str):
            open(os.path.join(base_path, item), 'w').close()
        elif isinstance(item, dict):
            for folder, subitems in item.items():
                folder_path = os.path.join(base_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                create_structure(folder_path, subitems)

base_path = os.getcwd()
create_structure(base_path, project_structure["course_platform"])

print("✅ Project structure created successfully!")
