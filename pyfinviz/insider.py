import enum

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

    @staticmethod
    def fetch(filter_option: FilterOption = FilterOption.ALL,
              view_option: ViewOption = ViewOption.LATEST):
        main_url = 'https://finviz.com/insidertrading.ashx?tc=' + filter_option.value + view_option.value
        return WebScraper.get_single_table_pandas(main_url)
