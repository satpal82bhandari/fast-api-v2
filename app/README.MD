1. Create a .env file in the root directory and copy format from .env.example (if not available)
```
DATABASE_URL=postgresql://<username>:<password>@localhost/<database_name>
```
5. Start the FastAPI application using Uvicorn
```
uvicorn app.main:app --reload