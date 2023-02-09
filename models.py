from extensions import Base
from uuid import uuid4
from sqlalchemy import *
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, JSON


class CurrencyRate(Base):
    __tablename__ = "currency_rates"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime, default='now()')
    updated_at = Column(DateTime, onupdate='now()')
    fullname = Column(String)
    title = Column(String)
    description = Column(DOUBLE_PRECISION)
    date = Column(DateTime)

    def __init__(self, fullname=None, title=None, description=None, date=None):
        self.fullname = fullname
        self.title = title
        self.description = description
        self.date = date

    @property
    def serialize(self):
        return dict(id=self.id,
                    fullname=self.fullname,
                    title=self.title,
                    description=self.description)


class SearchResult(Base):
    __tablename__ = 'search_results'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(DateTime, default='now()')
    updated_at = Column(DateTime, onupdate='now()')

    search_id = Column(String)
    status = Column(String)
    items = Column(JSON)

    def __init__(self, search_id=None, status=None, items=None):
        self.search_id = search_id if search_id else str(uuid4())
        self.status = status
        self.items = items

    @property
    def serialize(self):
        return dict(id=self.id,
                    search_id=self.search_id,
                    status=self.status,
                    items=self.items)
