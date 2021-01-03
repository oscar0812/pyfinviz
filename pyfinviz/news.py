import pandas as pd

from pyfinviz.utils import WebScraper


class News:

    @staticmethod
    def __table_to_df__(table):
        trs = table.find_all('tr', recursive=False)
        info = []

        for tr in trs:
            tds = tr.find_all('td')
            td_a = tds[len(tds)-1].find('a')
            info.append({'Time': tds[1].text, 'Headline': td_a.text, 'URL': td_a['href']})

        return pd.DataFrame.from_dict(info)

    @staticmethod
    def fetch():
        main_url = 'https://finviz.com/news.ashx'
        div_ = WebScraper.get_soup(main_url).find('div', class_='news').find('table')
        trs_ = div_.find_all('tr', recursive=False)
        main_tables = trs_[len(trs_)-1].find_all('table')
        return News.__table_to_df__(main_tables[0]), News.__table_to_df__(main_tables[1])
