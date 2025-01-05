from fastapi import FastAPI
from mongoengine import connect
from app.config import settings
from app.api.routes import auth, projects

# Create FastAPI app
app = FastAPI(title="FastAPI JWT RBAC")

# Connect to MongoDB
connect(host=settings.mongodb_uri)

# Include routers
app.include_router(auth.router, tags=["auth"])
app.include_router(projects.router, prefix="/projects", tags=["projects"])

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI JWT RBAC API"}