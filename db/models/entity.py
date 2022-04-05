from sqlalchemy import Column, BigInteger

from db.config import Base


class Entity(Base):
    __tablename__ = 'entities'
    __table_args__ = {'schema': 'office_sud'}

    uin = Column(BigInteger, primary_key=True)
