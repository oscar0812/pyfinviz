import pandas as pd

from pyfinviz.utils import WebScraper


class Quote:

    def __init__(self, ticker, exchange, company_name, sectors, fundamental_df, outer_ratings_df, outer_news_df,
                 income_statement_df, insider_trading_df):
        self.exists = ticker is not None
        self.ticker = ticker
        self.exchange = exchange
        self.company_name = company_name
        self.sectors = sectors
        self.fundamental_df = fundamental_df
        self.outer_ratings_df = outer_ratings_df
        self.outer_news_df = outer_news_df
        self.income_statement_df = income_statement_df
        self.insider_trading_df = insider_trading_df

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

        return pd.DataFrame.from_dict(outer_ratings_info)

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

        return pd.DataFrame.from_dict(outer_news_info)

    @staticmethod
    def __get_XHR_requests__(ticker):
        s_u = 'https://finviz.com/api/statement.ashx?t=' + ticker + '&s='
        statement_dicts = {'income_statement': WebScraper.get_json(s_u + 'IA'),
                           'balance_sheet': WebScraper.get_json(s_u + 'BA'),
                           'cash_flow': WebScraper.get_json(s_u + 'CA')}

        # convert dict to dataframes
        income_statement_df = pd.DataFrame.from_dict(statement_dicts['income_statement']['data'])
        balance_sheet_df = pd.DataFrame.from_dict(statement_dicts['balance_sheet']['data'])
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

        return pd.DataFrame.from_dict(insider_trading_info)

    @staticmethod
    def fetch(ticker="FB"):
        main_url = 'https://finviz.com/quote.ashx?t=' + ticker
        soup = WebScraper.get_soup(main_url)

        # base info
        full_title = soup.find('table', class_='fullview-title')

        if full_title is None:
            # Doesn't exist
            return Quote(None, None, None, None, None, None, None, None, None)

        trs = full_title.find_all('tr', recursive=False)
        ticker_ = trs[0].find(id="ticker").text
        exchange_ = trs[0].find('span').text
        company_name_ = trs[1].text
        sectors_ = [x.strip() for x in trs[2].text.split('|')]

        # fundament table (the table with index, market cap, etc.)
        fundamental_tds = soup.find('table', class_='snapshot-table2').find_all('td')

        # convert dict to dataframe (only 1 key per value so have to implement like this)
        fundamental_df = pd.DataFrame(list({fundamental_tds[index].text: fundamental_tds[index + 1].text for index in
                                            range(0, len(fundamental_tds) - 1, 2)}.items()), columns=['name', 'value'])

        outer_ratings_df = Quote.__get_outer_ratings_df__(soup)
        outer_news_df = Quote.__get_outer_news_df__(soup)
        income_statement_df, balance_sheet_df, cash_flow_df = Quote.__get_XHR_requests__(ticker)
        insider_trading_df = Quote.__get_insider_trading_df__(soup)

        return Quote(ticker_, exchange_, company_name_, sectors_, fundamental_df, outer_ratings_df, outer_news_df,
                     income_statement_df, insider_trading_df)
