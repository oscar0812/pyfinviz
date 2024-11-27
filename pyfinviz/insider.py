import enum

from pyfinviz.base_url import get_url
from pyfinviz.utils import WebScraper


class Insider:
    class ViewOption(enum.Enum):
        LATEST = ""
        TOP_INSIDER_TRADING_RECENT_WEEK = "&or=-10&tv=100000&o=-transactionValue"
        TOP_10_PERCENT_OWNER_TRADING_RECENT_WEEK = "&or=10&tv=1000000&o=-transactionValue"

    class FilterOption(enum.Enum):
        ALL = "7"
        BUY = "1"
        SELL = "2"

    def __init__(self, filter_option: FilterOption = FilterOption.ALL,
                 view_option: ViewOption = ViewOption.LATEST, api_key=None):
        self.main_url = f'{get_url(path="insidertrading", api_key=api_key)}tc={filter_option.value}{view_option.value}'
        self.soup, self.table_df = WebScraper.get_single_table_pandas(self.main_url)
