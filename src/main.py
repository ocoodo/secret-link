from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database import create_tables

app = FastAPI(
    title="SecretLink API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
from src.links.router import router as link_router
app.include_router(link_router)


@app.on_event("startup")
async def startup() -> None:
    await create_tables()
