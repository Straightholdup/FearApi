from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.models.entity import Entity

class BookDAL():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_book(self, name: str, author: str, release_year: int):
        new_book = Entity(name=name,author=author, release_year=release_year)
        self.db_session.add(new_book)
        await self.db_session.flush()

    async def get_all_entities(self) -> List[Entity]:
        q = await self.db_session.execute(select(Entity).order_by(Entity.uin))
        return q.scalars().all()

    async def update_book(self, book_id: int, name: Optional[str], author: Optional[str], release_year: Optional[int]):
        q = update(Entity).where(Entity.uin == book_id)
        if name:
            q = q.values(name=name)
        if author:
            q = q.values(author=author)
        if release_year:
            q = q.values(release_year=release_year)
        q.execution_options(synchronize_session="fetch")
        await  self.db_session.execute(q)