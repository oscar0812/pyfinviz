from pyfinviz.utils import WebScraper
import enum


class Groups:
    class GroupOption(enum.Enum):
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

    class ViewOption(enum.Enum):
        OVERVIEW = "110"
        VALUATION = "120"
        PERFORMANCE = "140"
        CUSTOM = "150"

    def __init__(self, group_option: GroupOption = GroupOption.SECTOR,
                 view_option: ViewOption = ViewOption.OVERVIEW):
        self.main_url = f'https://finviz.com/groups.ashx?{group_option.value}&v={view_option.value}'
        self.soup, self.table_df = WebScraper.get_single_table_pandas(self.main_url)
