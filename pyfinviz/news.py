from enum import Enum

import pandas as pd

from pyfinviz.base_url import get_url
from pyfinviz.utils import WebScraper


class News:
    class ViewOption(Enum):
        MARKET_NEWS = "1"
        STOCKS_NEWS = "3"
        ETF_NEWS = "4"
        CRYPTO_NEWS = "5"

    @staticmethod
    def __table_to_df__(table):
        trs = table.find_all('tr', recursive=False)
        info = []

        for tr in trs:
            tds = tr.find_all('td')
            td_a = tds[len(tds) - 1].find('a')
            if td_a is None:
                continue

            time_td = tr.find('td', class_='news_date-cell')
            time = time_td.text

            info.append({'Time': time, 'Headline': td_a.text, 'URL': td_a['href']})

        return pd.DataFrame(info)

    def __init__(self, api_key=None, view_option: ViewOption = ViewOption.MARKET_NEWS):

        self.main_url = f'{get_url(path="news", api_key=api_key)}' + f"v={view_option.value}"
        self.soup = WebScraper.get_soup(self.main_url)

        # handle multi tables presents on MARKET NEWS page
        if view_option == News.ViewOption.MARKET_NEWS:
            div_ = self.soup.find('div', class_='news').find('table')
            trs_ = div_.find_all('tr', recursive=False)
            main_tables = trs_[len(trs_) - 1].find_all('table')

            self.news_df = News.__table_to_df__(main_tables[0])
            self.blogs_df = News.__table_to_df__(main_tables[1])

        else:
            main_tables = self.soup.find('div', class_='news').find_all('table')
            self.news_df = News.__table_to_df__(main_tables[0])
            self.blogs_df = None
