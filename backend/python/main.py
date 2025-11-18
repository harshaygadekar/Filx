from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
from config import settings
from database.db import init_db
from api import files, search, tags, duplicates, analytics

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    logger.info(f"{settings.app_name} API started")
    logger.info(f"Database: {settings.db_path}")
    yield
    # Shutdown
    logger.info("Application shutting down")

app = FastAPI(
    title=settings.app_name,
    description="Intelligent File Organization API",
    version="1.0.0",
    lifespan=lifespan
)

# SECURITY FIX: Restrict CORS to specific origins instead of allowing all
# For production, replace with actual frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

app.include_router(files.router)
app.include_router(search.router)
app.include_router(tags.router)
app.include_router(duplicates.router)
app.include_router(analytics.router)

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
