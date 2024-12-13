# ✍️ Form Builder 

This project is a form builder that allows you to create forms through an admin panel powered by Jazzmin. Once created, users can fill out the forms by answering the questions. The system also includes various validations to ensure that responses are accurate and complete. ✅

## ⚙️ Installation and Setup 

### Step 1: Clone the Repository

```bash
git clone git@github.com:MahsaRah99/Form-Builder.git
cd Form-Builder/backend
````

### 📦 Step 2: Install Dependencies 
Ensure you have pip and python3 installed, then install the required Python packages:
````bash
pip install -r requirements.txt
````

#### 🗄️ Step 3: Configure the Database
Open your Django settings file and configure the database settings according to your environment. The default is SQLite, but you can use PostgreSQL of your choice.
Apply migrations to set up the database schema:
````bash
python manage.py migrate
````

### 🚀 Step 4: Start the server
````bash
python manage.py runserver
````

## 🐳 Run with Docker
This project can also be run using Docker. Follow these steps:

### Step 1: Database Configuration
Ensure your database is set up and running. If you're using PostgreSQL locally, configure the DATABASES settings in settings.py:
```bash
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "your_db_name",
        "USER": "your_db_user",
        "PASSWORD": "your_db_password",
        "HOST": "db",
        "PORT": "5432",
    }
}
````

### Step 2: Build the Docker image
````bash
docker-compose build
````
### Step 3: Run the container
````bash
docker-compose up
````
This will start the application in a Docker container. The app will be accessible at http://localhost:8000.

## 🧪 Running Tests 
To run the tests, use the following command:
````bash
python manage.py test
````

Or, if you're using Docker, you can run the tests inside the container:
````bash
docker-compose exec web python manage.py test
````

### Thank You 🙏
Thank you for taking the time to check out this project! I appreciate your support and look forward to collaborating with you!

