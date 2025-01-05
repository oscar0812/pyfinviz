import enum

from pyfinviz.base_url import get_url
from pyfinviz.utils import WebScraper


class Crypto:
    class RelativePerformanceOption(enum.Enum):
        ONE_DAY = "1"
        ONE_WEEK = "2"
        ONE_MONTH = "3"
        MONTH_TO_DATE = "8"
        THREE_MONTH = "4"
        HALF_YEAR = "5"
        ONE_YEAR = "6"
        YEAR_TO_DATE = "7"

    class CurrencyOption(enum.Enum):
        USD = "USD"
        USDT = "USDT"
        EUR = "EUR"
        BTC = "BTC"

    def __init__(self, relative_performance_option: RelativePerformanceOption = RelativePerformanceOption.ONE_DAY,
                 currency_option: CurrencyOption = CurrencyOption.USD,
                 api_key=None):
        self.main_url = f'{get_url(path="crypto_performance", api_key=api_key)}' \
                        f'v={relative_performance_option.value}' \
                        f'&C={currency_option.value}'
        self.soup, self.table_df = WebScraper.get_single_table_pandas(self.main_url)
