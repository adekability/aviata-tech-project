from extensions import Base
from uuid import uuid4
from sqlalchemy import *
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, JSON
import copy
from datetime import datetime


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

    def serialize(self):
        return dict(id=self.id,
                    fullname=self.fullname,
                    title=self.title,
                    description=self.description)

    @classmethod
    def convert(cls, from_: dict, to_: dict):
        from_currency = cls.query.filter_by(title=from_['currency'], date=datetime(2023, 1, 1).date()).first()
        from_price = from_['price']
        if to_['currency'] == 'KZT':
            to_currency = 1
        else:
            to_currency = cls.query.filter_by(title=to_['currency'], date=datetime(2021, 1, 1).date()).first()
            to_currency = to_currency.description

        from_total_kz = from_price * from_currency.description

        result = from_total_kz/to_currency
        return round(result, 2)


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

    def serialize_by_currency(self, currency):
        items = copy.deepcopy(self.items)
        for item in items:
            item['price'] = {"amount": CurrencyRate.convert(from_={"currency": item['pricing']['currency'],
                                                                   "price": float(item['pricing']['total'])},
                                                            to_={"currency": currency}),
                             "currency": currency}
        items = sorted(items, key=lambda x: x['price']['amount'])
        return dict(search_id=self.search_id,
                    status=self.status,
                    items=items)

