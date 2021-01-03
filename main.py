from pyfinviz.screener import Screener

if __name__ == '__main__':
    '''
    options = [ScreenerDescriptive.AnalystRecomOption.STRONG_BUY_1, ScreenerDescriptive.IndustryOption.STOCKS_ONLY_EX_FUNDS]
    sd = ScreenerDescriptive.fetch(options, ScreenerDescriptive.ViewOption.VALUATION, pages=[x for x in range(1, 21)])
    sd.to_csv('screener.csv')
    '''

    # with no params (default screener table)
    table_info = Screener.fetch()
    # with params (The first 3 pages of "Screen Aerospace and Defense" where Analyst recommend a strong buy)
    options = [Screener.IndustryOption.STOCKS_ONLY_EX_FUNDS, Screener.AnalystRecomOption.STRONG_BUY_1]
    table_info = Screener.fetch(filter_options=options, view_option=Screener.ViewOption.VALUATION, pages=[x for x in range(1, 4)])

    a = 1
    '''
    sd = pd.read_csv('screener.csv')
    sort_by = 'EPSthisY'
    sd = sd.sort_values(by=sort_by, key=lambda x: np.argsort(index_natsorted(sd[sort_by])))
    a = 1
    '''