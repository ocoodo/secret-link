from fastapi import FastAPI

from src.database import create_tables


app = FastAPI(
    title="SecretLink API"
)


# Include 
from src.links.router import router as link_router
app.include_router(link_router)


@app.on_event("startup")
async def startup() -> None:
    await create_tables()