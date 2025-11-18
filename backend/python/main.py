from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from database.db import init_db
from api import files, search, tags, duplicates, analytics

app = FastAPI(
    title=settings.app_name,
    description="Intelligent File Organization API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(files.router)
app.include_router(search.router)
app.include_router(tags.router)
app.include_router(duplicates.router)
app.include_router(analytics.router)

@app.on_event("startup")
async def startup_event():
    init_db()
    print(f"{settings.app_name} API started")
    print(f"Database: {settings.db_path}")

@app.get("/")
async def root():
    return {
        "message": f"Welcome to {settings.app_name} API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    return {"status": "running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=True
    )
