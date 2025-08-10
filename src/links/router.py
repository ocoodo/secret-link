from fastapi import APIRouter, HTTPException

from src.database import DbSession
from .schemas import NewLink
from .service import new_link, get_link
from .models import Link


router = APIRouter()


@router.post("/links")
async def new_link_handler(
    link: NewLink,
    db_session: DbSession,
):
    link = await new_link(db_session, link.content)
    return {"token": link.token}


@router.get("/s/{token}")
async def get_link_handler(
    token: str,
    db_session: DbSession,
):
    link = await get_link(db_session, token)
    if not link or not link.is_active:
        raise HTTPException(
            status_code=404,
            detail="Link not found"
        )
    link.is_consumed = True
    db_session.add(link)
    await db_session.commit()
    return {"content": link.content}