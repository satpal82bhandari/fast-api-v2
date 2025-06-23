## 1. Environment Setup

### Install Conda and Requirements

-   **Conda Environment**: Create and activate a new Conda environment:
```
conda create --name ENV_NAME python=3.10 
conda activate ENV_NAME
```
-   **Dependencies**: Install all required packages using:
```
pip install -r requirements.txt
```
This step sets up a clean development environment with all necessary Python packages.

## 2. Database Setup and Migrations

### Create PostgreSQL Database and Table

-   **Database Creation**: Create your PostgreSQL database manually using a tool like `psql` or PgAdmin.
-   **Table and Extensions**: Create necessary tables and enable required extensions (e.g., UUID generation):
```
CREATE EXTENSION postgis;
```

### Alembic Configuration

-   **Configure Alembic**: Edit the `alembic.ini` file by specifying your database connection URL:
```
sqlalchemy.url = postgresql://username:password@localhost/dbname
```
-   **.env File**: Create a `.env` file to securely store your database credentials:
```
DATABASE_URL= postgresql://username:password@localhost/dbname
```
-   **Run Migrations**: Generate an initial migration and apply the changes:
```
alembic revision --autogenerate -m "Initial migration" 
alembic upgrade head
```
This step ensures your database schema is version-controlled and in sync with your data models.

## 3. Running the Application

### Launch your FastAPI application with Uvicorn:
```
uvicorn main:app --reload
```
-   **Uvicorn**: The `--reload` parameter restarts the server upon code changes, ideal for development.