from extensions import db
from extensions import Base


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
