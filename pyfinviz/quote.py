from collections import Counter
from datetime import datetime

import bs4
import pandas as pd

from pyfinviz.base_url import get_url
from pyfinviz.utils import WebScraper


class Quote:

    @staticmethod
    def __get_fundamental_df__(soup):
        # fundament table (the table with index, market cap, etc.)
        fundamental_tds = soup.find('table', class_='snapshot-table2').find_all('td')

        '''
            Add hover data-boxover attr to title IF title repeats, for example
            Old key (Just inner text) = 'EPS next Y'
            New key (inner text + hover text) = 'EPS next Y - EPS estimate for next year'
        '''
        fundamental_info = dict()
        counter = Counter([x.text for x in fundamental_tds])
        for index in range(0, len(fundamental_tds) - 1, 2):
            key_td, value_td = fundamental_tds[index], fundamental_tds[index + 1]
            key: str = key_td.text
            if counter[key_td.text] > 1:
                # ... cssheader=[tooltip_short_hdr] body=[EPS estimate for next year] offsetx=[10] ...
                boxover_attr: str = bs4.BeautifulSoup(key_td.attrs['data-boxover'].replace('<br>', ' '), 'lxml').text
                open_index = boxover_attr.index(' body=', 0) + 7
                close_index = boxover_attr.index(']', open_index)
                key = f'{key} - {boxover_attr[open_index: close_index]}'
            fundamental_info[key] = [value_td.text]

        return pd.DataFrame.from_dict(fundamental_info)

    @staticmethod
    def __get_outer_ratings_df__(soup):
        outer_ratings_table = soup.find('table', class_='js-table-ratings')
        # might not have outer ratings
        if outer_ratings_table is None:
            return None

        outer_ratings_trs = outer_ratings_table.find_all('tr', recursive=False)

        outer_ratings_info = []
        tags__ = ['Date', 'Status', 'Outer', 'Rating', 'Price']
        for tr in outer_ratings_trs:
            o_tds_text = [td.text for td in tr.find_all('td')]
            if len(o_tds_text) == len(tags__):
                outer_ratings_info.append({tags__[i]: o_tds_text[i] for i in range(0, len(tags__))})

        return pd.DataFrame(outer_ratings_info)

    @staticmethod
    def __get_outer_news_df__(soup):
        outer_news_table = soup.find('table', class_='fullview-news-outer')
        # might not have news
        if outer_news_table is None:
            return None

        outer_news_trs = outer_news_table.find_all('tr', recursive=False)

        outer_news_info = []
        tags__ = ['Date', 'Headline', 'URL', 'From']
        prev_date = None
        for tr_ in outer_news_trs:
            o_tds = tr_.find_all('td', recursive=False)
            if len(o_tds) < 2:
                continue
            news_a = o_tds[1].find('a')
            if news_a is None:
                # broken news
                continue

            news_from = o_tds[1].find('span')
            date_ = o_tds[0].text.strip()
            if date_.startswith('Today '):
                date_ = f"{datetime.today().strftime('%m-%d-%Y')} {date_.split(' ')[1]}"
            elif '-' not in date_ and prev_date is not None:
                date_ = f"{prev_date.split(' ')[0]} {date_}"

            prev_date = date_
            info_ = [date_, news_a.text, news_a['href'], news_from.text]
            outer_news_info.append({tags__[i]: info_[i] for i in range(0, len(tags__))})

        return pd.DataFrame(outer_news_info)

    @staticmethod
    def __get_XHR_requests__(ticker, api_key=None):
        s_u = f'{get_url(path="api/statement", api_key=api_key)}t={ticker}&s='
        statement_dicts = {'income_statement': WebScraper.get_json(f'{s_u}IA'),
                           'balance_sheet': WebScraper.get_json(f'{s_u}BA'),
                           'cash_flow': WebScraper.get_json(f'{s_u}CA'),
                           'reuters_income_statement': WebScraper.get_json(f'{s_u}IA&so=R'),
                           'reuters_balance_sheet': WebScraper.get_json(f'{s_u}BA&so=R'),
                            'reuters_cash_flow': WebScraper.get_json(f'{s_u}CA&so=R')}

        # convert dict to dataframes&so=R
        # issue 2: KeyError: 'data'
        # solution: some tickers dont have XHR_request data, return None
        income_statement_df = None
        balance_sheet_df = None
        cash_flow_df = None
        reuters_income_statement_df = None
        reuters_balance_sheet_df = None
        reuters_cash_flow_df = None


        if 'data' in statement_dicts['income_statement']:
            income_statement_df = pd.DataFrame.from_dict(statement_dicts['income_statement']['data'])

        if 'data' in statement_dicts['balance_sheet']:
            balance_sheet_df = pd.DataFrame.from_dict(statement_dicts['balance_sheet']['data'])

        if 'data' in statement_dicts['cash_flow']:
            cash_flow_df = pd.DataFrame.from_dict(statement_dicts['cash_flow']['data'])

        if 'data' in statement_dicts['reuters_income_statement']:
            reuters_income_statement_df = pd.DataFrame.from_dict(statement_dicts['reuters_income_statement']['data'])
        
        if 'data' in statement_dicts['reuters_balance_sheet']:
            reuters_balance_sheet_df = pd.DataFrame.from_dict(statement_dicts['reuters_balance_sheet']['data'])

        if 'data' in statement_dicts['reuters_cash_flow']:
            reuters_cash_flow_df = pd.DataFrame.from_dict(statement_dicts['reuters_cash_flow']['data'])

        return income_statement_df, balance_sheet_df, cash_flow_df, reuters_income_statement_df, reuters_balance_sheet_df, reuters_cash_flow_df

    @staticmethod
    def __get_insider_trading_df__(soup):
        insider_trading_table = soup.find('table', class_="body-table")
        # might not have insider trading
        if insider_trading_table is None:
            return None

        insider_trading_trs = insider_trading_table.find_all('tr', recursive=False)
        insider_trading_info = []

        tags__ = [td.text.strip() for td in insider_trading_trs[0].find_all('td')]
        tags__.insert(1, 'Insider History URL')
        tags__.append('SEC Form 4 URL')
        for tr in insider_trading_trs[1:]:
            tds = tr.find_all('td', recursive=False)
            info_ = [td.text.strip() for td in tds]
            info_.insert(1, f"https://finviz.com/{tds[0].find('a')['href']}")
            info_.append(tds[len(tds) - 1].find('a')['href'])

            insider_trading_info.append({tags__[i]: info_[i] for i in range(0, len(tags__))})

        return pd.DataFrame(insider_trading_info)

    def __init__(self, ticker="META", api_key=None):
        self.main_url = f'{get_url(path="quote", api_key=api_key)}t={ticker}'
        self.soup = WebScraper.get_soup(main_url=self.main_url)

        # base info
        quote_header = self.soup.find('div', class_='quote-header')
        self.exists = quote_header is not None

        if not self.exists:
            # Doesn't exist
            return

        self.ticker = quote_header.find('h1').text.strip()
        self.company_name = quote_header.find('h2').text.strip()

        sector_tags = self.soup.find('div', class_='quote-links').find('div').find_all('a', recursive=False)
        sectors_arr = [x.text.strip() for x in sector_tags]  # ['Consumer Cyclical', ..., 'NASD']
        self.sectors = sectors_arr[0: -1]
        self.exchange = sectors_arr[-1]

        # quote price
        price_div = quote_header.find('div', class_='quote-price')
        self.price_date = price_div.find(class_='quote-price_date').text.replace('•', '')
        try:
            price_text = quote_header.find(class_='quote-price_wrapper').find('strong').text
            price_text = price_text.replace(',', '')
            self.price = float(price_text)
        except (AttributeError, ValueError) as e:
            print(f"Error parsing price: {e}")
            self.price = None

        self.fundamental_df = Quote.__get_fundamental_df__(self.soup)
        self.outer_ratings_df = Quote.__get_outer_ratings_df__(self.soup)
        self.outer_news_df = Quote.__get_outer_news_df__(self.soup)
        self.income_statement_df, self.balance_sheet_df, self.cash_flow_df, self.reuters_income_statement_df, self.reuters_balance_sheet_df, self.reuters_cash_flow_df = Quote.__get_XHR_requests__(ticker, api_key=api_key)
        self.insider_trading_df = Quote.__get_insider_trading_df__(self.soup)
