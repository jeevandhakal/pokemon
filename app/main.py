from app.api.endpoints import router as api_router
from app.db.seed import populate_database
from fastapi import FastAPI
from app.log.log_config import configure_logging

app = FastAPI()

# Configure logging settings
configure_logging()

@app.on_event("startup")
async def startup_event():
    await populate_database()  


app.include_router(api_router, prefix="/api/v1")
