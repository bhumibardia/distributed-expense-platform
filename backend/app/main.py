from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import engine, Base, get_db
from app.models import user  # Ensures SQLAlchemy registers the User table

# Creates tables in PostgreSQL if they do not exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Distributed Expense Management API")

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@app.get("/")
def root():
    return {"message": "Distributed Expense Management API is running", "docs": "/docs"}