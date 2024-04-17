**Django OEE Application- Project Overview**

This is a Django application that calculates Overall Equipment Effectiveness (OEE) for machines in a manufacturing environment. It uses a SQLite database to store data about machines and production logs and provides a REST API for accessing and manipulating the data.

**Features**

- Calculate OEE for each machine using the provided formula.
- REST API endpoints for accessing machine and production log data.
- Django admin interface for managing data.
- Filters for retrieving data by machine or date range.

**Installation**

1. Clone the repository:
    git clone https://github.com/GaneshSathiyamoorthi/Django-OEE-Application

2. Change into the project directory:
    cd oee-django-app
 
3. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate

4. Install dependencies:
     pip install -r requirements.txt
  
**Prerequisites**

- Python 3.8 or later
- Django 3.2 or later
- Other dependencies listed in `requirements.txt`

 **Running the Application**

1. Apply database migrations:
    python manage.py migrate

2. Create a superuser account for Django admin:
    python manage.py createsuperuser

3. Run the development server:
    python manage.py runserver

4. Visit `http://127.0.0.1:8000/` to access the application.

**API Usage**

- **Machines** endpoint: `http://127.0.0.1:8000/api/machines/`
    - `GET`: Retrieve a list of all machines.
    - `POST`: Create a new machine.

- **Production Logs** endpoint: `http://127.0.0.1:8000/api/production_logs/`
    - `GET`: Retrieve a list of all production logs.
    - `POST`: Create a new production log.
Refer to the codebase for more API details.

**Tests**

- To run the tests, execute the following command
    python manage.py test
