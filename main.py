if __name__ == '__main__':
    from pyfinviz.news import News

    news = News()

    # available variables:
    print(news.main_url)  # scraped URL
    print(news.soup)  # beautiful soup object
    print(news.news_df)  # NEWS table information in a pd.DataFrame object
    print(news.blogs_df)  # BLOGS table information in a pd.DataFrame object

    # =====

    from pyfinviz.crypto import Crypto

    # with no params (SECTOR, OVERVIEW by default)
    crypto = Crypto()
    # with params
    crypto = Crypto(relative_performance_option=Crypto.RelativePerformanceOption.ONE_YEAR)

    # available variables:
    print(crypto.main_url)  # scraped URL
    print(crypto.soup)  # beautiful soup object
    print(crypto.table_df)  # table information in a pd.DataFrame object

    # =====

    from pyfinviz.groups import Groups

    # with no params (sector overview)
    groups = Groups()
    # with params (View the group VALUATION of the INDUSTRY sector)
    groups = Groups(group_option=Groups.GroupOption.INDUSTRY, view_option=Groups.ViewOption.VALUATION)
    # with params (View the group PERFORMANCE of the TECH sector)
    groups = Groups(group_option=Groups.GroupOption.INDUSTRY_TECHNOLOGY,
                    view_option=Groups.ViewOption.PERFORMANCE)

    # available variables:
    print(groups.main_url)  # scraped URL
    print(groups.soup)  # beautiful soup object
    print(groups.table_df)  # table information in a pd.DataFrame object

    # =====

    from pyfinviz.insider import Insider

    # with no params (ALL the LATEST insider trades)
    insider = Insider()
    # with params (the LATEST BUY insider trades)
    insider = Insider(filter_option=Insider.FilterOption.BUY)

    # available variables:
    print(insider.main_url)  # scraped URL
    print(insider.soup)  # beautiful soup object
    print(insider.table_df)  # table information in a pd.DataFrame object

    # =====

    from pyfinviz.quote import Quote

    quote = Quote(ticker="AMZN")

    # available variables:
    print(quote.exists)  # check if fetch was successful (STOCK may not exist)
    print(quote.ticker)  # AMZN
    print(quote.exchange)  # NASD
    print(quote.company_name)  # Amazon.com, Inc.
    print(quote.sectors)  # ['Consumer Cyclical', 'Internet Retail', 'USA']
    print(quote.fundamental_df)  # Index    P/E EPS (ttm) Insider Own  ...  SMA50  SMA200     Volume  Change
    print(quote.outer_ratings_df)  # 0   Nov-04-20     Upgrade  ...                Hold → Buy  $3360 → $4000
    print(quote.outer_news_df)  # 0   Jan-04-21 10:20PM  ...                   Bloomberg
    print(quote.income_statement_df)  # 1      12/31/2019  ...                    22.99206
    print(quote.insider_trading_df)  # 0         WILKE JEFFREY A  ...  http://www.sec.gov/Archives/edgar/data/1018724...

    # =====

    from pyfinviz.screener import Screener

    # with no params (default screener table)
    screener = Screener()
    # with params (The first 3 pages of "STOCKS ONLY" where Analyst recommend a strong buy)
    options = [Screener.IndustryOption.STOCKS_ONLY_EX_FUNDS, Screener.AnalystRecomOption.STRONG_BUY_1]
    screener = Screener(filter_options=options, view_option=Screener.ViewOption.VALUATION,
                        pages=[x for x in range(1, 4)])

    # available variables:
    print(screener.main_url)  # scraped URL
    print(screener.soups)  # beautiful soup object per page {1: soup, 2: soup, ...}
    print(screener.data_frames)  # table information in a pd.DataFrame object per page {1: table_df, 2, table_df, ...}
