from pyfinviz.quote import Quote

if __name__ == '__main__':
    '''
    options = [ScreenerDescriptive.AnalystRecomOption.STRONG_BUY_1, ScreenerDescriptive.IndustryOption.STOCKS_ONLY_EX_FUNDS]
    sd = ScreenerDescriptive.fetch(options, ScreenerDescriptive.ViewOption.VALUATION, pages=[x for x in range(1, 21)])
    sd.to_csv('screener.csv')
    '''

    quote = Quote.fetch("AMZN")
    if quote.exists:
        print(quote.insider_trading_df)
        quote.exists
        quote.ticker
        quote.exchange
        quote.company_name
        quote.sectors
        quote.fundamental_df
        quote.outer_ratings_df
        quote.outer_news_df
        quote.income_statement_df
        quote.insider_trading_df

    '''
    sd = pd.read_csv('screener.csv')
    sort_by = 'EPSthisY'
    sd = sd.sort_values(by=sort_by, key=lambda x: np.argsort(index_natsorted(sd[sort_by])))
    a = 1
    '''