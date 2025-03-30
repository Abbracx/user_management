# User Management Application

This is a Django-based user management application with Docker support for local development. Below are the detailed steps to start the application.

---

## Prerequisites

Ensure you have the following installed on your system:

1. **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
2. **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
3. **Python 3.12.0**: [Install Python](https://www.python.org/downloads/)
4. **Make** (optional): For using the provided `makefile` commands.

---

## Environment Setup

1. **Clone the Repository**:

   ```bash
   git clone git@github.com:Abbracx/user_management.git
   cd user-management
   ```

2. **Set Up Python Environment with pyenv**:
   [Check Out Pyenv](https://github.com/pyenv/pyenv#installation)

   Install and set up Python 3.12.0 using `pyenv`:
   

   ```bash
   pyenv install 3.12.0
   pyenv virtualenv 3.12.0 user-venv
   pyenv activate user-venv
   ```

   Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Copy the `.env` file if it doesn't exist:
     ```bash
     cp .env.example .env
     ```
   - Update the `.env` file with your desired configurations (e.g., database credentials, email settings).

---

## Starting the Application

### Using `makefile` (Recommended)

1. **Build and Start Services**:

   ```bash
   make build
   ```

2. **Access the Application**:

   - The web application will be available at [http://0.0.0.0:8000](http://0.0.0.0:8000).
   - Mailhog (for email testing) will be available at [http://0.0.0.0:8025](http://0.0.0.0:8025).

3. **Stop Services**:

   ```bash
   make down
   ```

4. **View Logs**:
   - General logs:
     ```bash
     make show-logs
     ```
   - Database logs:
     ```bash
     make show-logs-db
     ```
   - API application logs:
     ```bash
     make show-logs-web
     ```

---

### Using Docker Compose Directly

1. **Build and Start Services**:

   ```bash
   docker compose -f docker-compose.yml up --build -d
   ```

2. **Access the Application**:

   - The web application will be available at [http://0.0.0.0:8000](http://0.0.0.0:8000).
   - Mailhog (for email testing) will be available at [http://0.0.0.0:8025](http://0.0.0.0:8025).

3. **Stop Services**:

   ```bash
   docker compose -f docker-compose.yml down
   ```

4. **View Logs**:
   - General logs:
     ```bash
     docker compose -f docker-compose.yml logs
     ```
   - Database logs:
     ```bash
     docker compose -f docker-compose.yml logs postgres
     ```
   - Web application logs:
     ```bash
     docker compose -f docker-compose.yml logs web
     ```

---

## Running Migrations and Collecting Static Files

1. **Run Migrations**:

   ```bash
   make migrate
   ```

2. **Collect Static Files**:
   ```bash
   make collectstatic
   ```

---

## Creating a Superuser

To create a superuser for accessing the Django admin panel:

1. **Run the Command**:

   ```bash
   make superuser
   ```

2. **Access the Admin Panel**:

   - Navigate to [http://0.0.0.0:8000/superadmin/](http://0.0.0.0:8000/superadmin/).

3. **Access the Docs**:
   - Navigate to [http://0.0.0.0:8000/api/v1/auth/redoc/](http://0.0.0.0:8000/api/v1/auth/redoc/).

---

## Running Tests

1. **Run All Tests**:

   ```bash
   make cov
   ```

2. **Generate HTML Coverage Report**:
   ```bash
   make cov-html
   ```

---

## Additional Notes

- **Database**: The application uses PostgreSQL as the database. Ensure the database service is running before starting the application.
- **Redis**: Redis is used as the Celery broker for background tasks.
- **Mailhog**: Mailhog is used for testing email functionality locally.
