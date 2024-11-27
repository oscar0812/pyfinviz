from enum import Enum

from pyfinviz.base_url import get_url
from pyfinviz.utils import WebScraper


class Groups:
    class OrderBy(Enum):
        NAME = "name"
        MARKET_CAPITALIZATION = "marketcap"
        PRICE_EARNINGS = "pe"
        FORWARD_PRICE_EARNINGS = "forwardpe"
        PEG_PRICE_EARNINGS_GROWTH = "peg"
        PRICE_SALES = "ps"
        PRICE_BOOK = "pb"
        PRICE_CASH = "pc"
        PRICE_FREE_CASH_FLOW = "pfcf"
        DIVIDEND_YIELD = "dividendyield"
        EPS_GROWTH_PAST_5_YEARS = "eps5years"
        EPS_GROWTH_NEXT_5_YEARS = "estltgrowth"
        SALES_GROWTH_PAST_5_YEARS = "sales5years"
        SHORT_INTEREST_SHARE = "shortinterestshare"
        ANALYST_RECOMMENDATION = "recom"
        PERFORMANCE_WEEK = "perf1w"
        PERFORMANCE_MONTH = "perf4w"
        PERFORMANCE_QUARTER = "perf13w"
        PERFORMANCE_HALF_YEAR = "perf26w"
        PERFORMANCE_YEAR = "perf52w"
        PERFORMANCE_YEAR_TO_DATE = "perfytd"
        AVERAGE_VOLUME_3_MONTH = "averagevolume"
        RELATIVE_VOLUME = "relativevolume"
        CHANGE = "change"
        VOLUME = "volume"
        NUMBER_OF_STOCKS = "count"

    class OrderDirection(Enum):
        ASC = ""
        DESC = "-"

    class GroupOption(Enum):
        SECTOR = 'g=sector'
        INDUSTRY = 'g=industry'
        INDUSTRY_BASIC_MATERIALS = f'{INDUSTRY}&sg=basicmaterials'
        INDUSTRY_COMMUNICATION_SERVICES = f'{INDUSTRY}&sg=communicationservices'
        INDUSTRY_CONSUMER_CYCLICAL = f'{INDUSTRY}&sg=consumercyclical'
        INDUSTRY_CONSUMER_DEFENSIVE = f'{INDUSTRY}&sg=consumerdefensive'
        INDUSTRY_ENERGY = f'{INDUSTRY}&sg=energy'
        INDUSTRY_FINANCIAL = f'{INDUSTRY}&sg=financial'
        INDUSTRY_HEALTHCARE = f'{INDUSTRY}&sg=healthcare'
        INDUSTRY_INDUSTRIALS = f'{INDUSTRY}&sg=industrials'
        INDUSTRY_REAL_ESTATE = f'{INDUSTRY}&sg=realestate'
        INDUSTRY_TECHNOLOGY = f'{INDUSTRY}&sg=technology'
        INDUSTRY_UTILITIES = f'{INDUSTRY}&sg=utilities'
        COUNTRY = 'g=country'
        CAPITALIZATION = 'g=capitalization'

    class ViewOption(Enum):
        OVERVIEW = "110"
        VALUATION = "120"
        PERFORMANCE = "140"
        CUSTOM = "150"

    def __init__(self, group_option: GroupOption = GroupOption.SECTOR,
                 view_option: ViewOption = ViewOption.OVERVIEW,
                 order_by: OrderBy = OrderBy.NAME, order_direction: OrderDirection = OrderDirection.ASC, api_key=None):
        order_str = order_direction.value + order_by.value
        self.main_url = f'{get_url(path="groups", api_key=api_key)}{group_option.value}&v={view_option.value}&o={order_str}'
        self.soup, self.table_df = WebScraper.get_single_table_pandas(self.main_url)
