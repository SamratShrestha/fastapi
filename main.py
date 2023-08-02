from fastapi import FastAPI
from app.core.config import settings
from app.app import api_router

app = FastAPI(title="API", openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", log_level="info" )
