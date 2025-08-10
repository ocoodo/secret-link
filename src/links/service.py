from sqlalchemy import select

from .models import Link
from .utils import generate_link_id
from src.database import AsyncSession


async def new_link(
    db_session: AsyncSession,
    content: str,
) -> Link:
    link = Link(
        content=content
    )
    db_session.add(link)
    await db_session.flush()
    
    token = generate_link_id(link.id)
    link.token = token
    db_session.add(link)
    await db_session.commit()
    return link


async def get_link(
    db_session: AsyncSession,
    token: str,
) -> Link:
    query = await db_session.execute(
        select(Link)
        .where(Link.token == token)
    )
    return query.scalar_one_or_none()
