# Movie Mania


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python [Install](https://www.python.org/)


## Installation

To set up the project, follow these steps:


1. Clone the repository ssh:
   ```bash
   git clone git@github.com:sufi-an/movie-mania.git
   ```
   Clone the repository https:
   ```bash
    git clone https://github.com/sufi-an/movie-mania.git
   ```

2. Navigate to the project directory:
    ```bash
    cd movie-mania
    ```
3. Create a python virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate python virtual environment: (mac/linux)
    ```bash
    source venv/bin/activate
    ```
    windows
    ```bash
    venv\Scripts\activate
     ```
5. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
6. Create Superuser:
    ```bash
    python manage.py createsuperuser
    ```
7. Seed Initial data:
    ```bash
    python manage.py seed
    ```
8. Run migrations:
    ```bash
    python manage.py migrate
    ```
9. Run:
    ```bash
    python manage.py runserver
    ```

9. Access the base Application
    ```
    http://localhost:8000
    ```