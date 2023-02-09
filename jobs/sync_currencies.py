from datetime import datetime
import requests
import xml.etree.ElementTree as ET
from models import CurrencyRate
from extensions import db
from calendar import monthrange


class SyncCurrency:

    @classmethod
    def daily_sync(cls):
        today = datetime.now().date()
        cls.sync_currency_by_day(today)

    @classmethod
    def sync_last_five_years(cls):
        current_year = datetime.now().year
        for iter_year in range(current_year, current_year-6, -1):
            for year, month, day in cls.all_dates_in_year(iter_year):
                check_date = datetime(year, month, day)
                cls.sync_currency_by_day(check_date)

    @classmethod
    def sync_currency_by_day(cls, date):
        if CurrencyRate.query.filter_by(date=date).first(): return
        currency_tree = cls.fetch_currency_tree(date)
        for elem in currency_tree:
            if elem.tag == 'item':
                currency = elem.iter()
                currency_rate = CurrencyRate(date=date)
                for cur in currency:
                    match cur.tag:
                        case 'fullname':
                            currency_rate.fullname = cur.text
                        case 'title':
                            currency_rate.title = cur.text
                        case 'description':
                            currency_rate.description = cur.text
                db.session.add(currency_rate)
        db.session.commit()
        return

    @staticmethod
    def all_dates_in_year(year=2019):
        for month in range(1, 13):
            for day in range(1, monthrange(year, month)[1] + 1):
                yield year, month, day

    @staticmethod
    def fetch_currency_tree(date):
        fetch_currency_url = f"https://www.nationalbank.kz/rss/get_rates.cfm?fdate={date.strftime('%d.%m.%Y')}"
        currencies = requests.get(fetch_currency_url)
        tree = ET.ElementTree(ET.fromstring(currencies.text))
        root_tree = tree.getroot()
        return root_tree
