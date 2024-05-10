# Django Project with PostgreSQL (EthanAI)

This is a Django project configured to use PostgreSQL as its database backend.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python (>= 3.x)
- PostgreSQL
- pip (Python package manager)

## Setup

1. Clone this repository to your local machine:

    ```bash
     git clone https://github.com/Vivek-Soni-5/ethanai.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ethanai
    ```

3. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a PostgreSQL database for the project. You can do this via command line or a GUI tool like pgAdmin.

5. Update the database settings in `settings.py` located in the `projectname` directory:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

    Replace `'your_database_name'`, `'your_database_user'`, and `'your_database_password'` with your actual PostgreSQL database credentials.

6. Run database migrations to create necessary tables:

    ```bash
    python manage.py migrate
    ```

## Running the Project

Once you've completed the setup steps, you can run the Django development server:

```bash
python manage.py runserver
Visit : http://127.0.0.1:8000/financial
