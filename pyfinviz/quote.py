import pandas as pd

from pyfinviz.utils import WebScraper


class Quote:

    @staticmethod
    def __get_outer_ratings_df__(soup):
        outer_ratings_table = soup.find('table', class_='fullview-ratings-outer')
        # might not have outer ratings
        if outer_ratings_table is None:
            return None

        outer_ratings_trs = outer_ratings_table.find_all('tr', recursive=False)

        outer_ratings_info = []
        tags__ = ['Date', 'Status', 'Outer', 'Rating', 'Price']
        for tr in outer_ratings_trs:
            o_tds_text = [td.text for td in tr.find_all('td')[1:]]
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
            news_a = o_tds[1].find('a')
            news_from = o_tds[1].find('span')
            date_ = o_tds[0].text.strip()
            if '-' not in date_:
                date_ = prev_date.split(' ')[0] + ' ' + date_

            prev_date = date_
            info_ = [date_, news_a.text, news_a['href'], news_from.text]
            outer_news_info.append({tags__[i]: info_[i] for i in range(0, len(tags__))})

        return pd.DataFrame(outer_news_info)

    @staticmethod
    def __get_XHR_requests__(ticker):
        s_u = 'https://finviz.com/api/statement.ashx?t=' + ticker + '&s='
        statement_dicts = {'income_statement': WebScraper.get_json(s_u + 'IA'),
                           'balance_sheet': WebScraper.get_json(s_u + 'BA'),
                           'cash_flow': WebScraper.get_json(s_u + 'CA')}

        # convert dict to dataframes
        # issue 2: KeyError: 'data'
        # solution: some tickers dont have XHR_request data, return None
        income_statement_df = None
        balance_sheet_df = None
        cash_flow_df = None

        if 'data' in statement_dicts['income_statement']:
            income_statement_df = pd.DataFrame.from_dict(statement_dicts['income_statement']['data'])

        if 'data' in statement_dicts['balance_sheet']:
            balance_sheet_df = pd.DataFrame.from_dict(statement_dicts['balance_sheet']['data'])

        if 'data' in statement_dicts['cash_flow']:
            cash_flow_df = pd.DataFrame.from_dict(statement_dicts['cash_flow']['data'])

        return income_statement_df, balance_sheet_df, cash_flow_df

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
            info_.insert(1, 'https://finviz.com/' + tds[0].find('a')['href'])
            info_.append(tds[len(tds) - 1].find('a')['href'])

            insider_trading_info.append({tags__[i]: info_[i] for i in range(0, len(tags__))})

        return pd.DataFrame(insider_trading_info)

    def __init__(self, ticker="FB"):
        main_url = 'https://finviz.com/quote.ashx?t=' + ticker
        self.soup = WebScraper.get_soup(main_url)

        # base info
        full_title = self.soup.find('table', class_='fullview-title')
        self.exists = full_title is not None

        if full_title is None:
            # Doesn't exist
            return

        trs = full_title.find_all('tr', recursive=False)
        self.ticker = trs[0].find(id="ticker").text
        self.exchange = trs[0].find('span').text
        self.company_name = trs[1].text
        self.sectors = [x.strip() for x in trs[2].text.split('|')]

        # fundament table (the table with index, market cap, etc.)
        fundamental_tds = self.soup.find('table', class_='snapshot-table2').find_all('td')

        self.fundamental_df = pd.DataFrame.from_dict(
            {fundamental_tds[index].text: [fundamental_tds[index + 1].text] for index in
             range(0, len(fundamental_tds) - 1, 2)})

        self.outer_ratings_df = Quote.__get_outer_ratings_df__(self.soup)
        self.outer_news_df = Quote.__get_outer_news_df__(self.soup)
        self.income_statement_df, self.balance_sheet_df, self.cash_flow_df = Quote.__get_XHR_requests__(ticker)
        self.insider_trading_df = Quote.__get_insider_trading_df__(self.soup)
