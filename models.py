from extensions import db
from extensions import Base
from sqlalchemy.dialects.postgresql import JSON
from uuid import uuid4


class CurrencyRate(db.Model, Base):
    __tablename__ = "currency_rates"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fullname = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.Float)
    date = db.Column(db.DateTime)

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


class SearchResult(db.Model, Base):
    __tablename__ = 'search_results'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    search_id = db.Column(db.String)
    status = db.Column(db.String)
    items = db.Column(JSON)

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
