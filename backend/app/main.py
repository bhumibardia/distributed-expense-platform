from fastapi import FastAPI, Depends, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import engine, Base, get_db
from app.models import user
from app.api import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Distributed Expense Management API", docs_url=None)

app.include_router(auth.router)

@app.get("/docs", include_in_schema=False)
def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Docs",
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )

@app.get("/")
def root():
    return {"message": "Distributed Expense Management API is running", "docs": "/docs"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")