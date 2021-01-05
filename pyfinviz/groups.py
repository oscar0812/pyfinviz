from pyfinviz.utils import WebScraper
import enum


class Groups:
    class GroupOption(enum.Enum):
        SECTOR = 'g=sector'
        INDUSTRY = 'g=industry'
        INDUSTRY_BASIC_MATERIALS = INDUSTRY + '&sg=basicmaterials'
        INDUSTRY_COMMUNICATION_SERVICES = INDUSTRY + '&sg=communicationservices'
        INDUSTRY_CONSUMER_CYCLICAL = INDUSTRY + '&sg=consumercyclical'
        INDUSTRY_ENERGY = INDUSTRY + '&sg=energy'
        INDUSTRY_FINANCIAL = INDUSTRY + '&sg=financial'
        INDUSTRY_HEALTHCARE = INDUSTRY + '&sg=healthcare'
        INDUSTRY_INDUSTRIALS = INDUSTRY + '&sg=industrials'
        INDUSTRY_REAL_ESTATE = INDUSTRY + '&sg=realestate'
        INDUSTRY_TECHNOLOGY = INDUSTRY + '&sg=technology'
        INDUSTRY_UTILITIES = INDUSTRY + '&sg=utilities'
        COUNTRY = 'g=country'
        CAPITALIZATION = 'g=capitalization'

    class ViewOption(enum.Enum):
        OVERVIEW = "110"
        VALUATION = "120"
        PERFORMANCE = "140"
        CUSTOM = "150"

    def __init__(self, group_option: GroupOption = GroupOption.SECTOR,
                 view_option: ViewOption = ViewOption.OVERVIEW):
        self.main_url = 'https://finviz.com/groups.ashx?' + group_option.value + '&v=' + view_option.value
        self.soup, self.table_df = WebScraper.get_single_table_pandas(self.main_url)
