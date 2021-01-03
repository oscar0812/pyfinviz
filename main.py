from pyfinviz.screener.descriptive import ScreenerDescriptive

if __name__ == '__main__':
    options = [ScreenerDescriptive.AnalystRecomOption.STRONG_BUY_1, ScreenerDescriptive.IndustryOption.STOCKS_ONLY_EX_FUNDS]
    sd = ScreenerDescriptive.fetch(options, ScreenerDescriptive.ViewOption.VALUATION, pages=[x for x in range(1, 21)])
    sd.to_csv('screener.csv')
    
    '''
    sd = pd.read_csv('screener.csv')
    sort_by = 'EPSthisY'
    sd = sd.sort_values(by=sort_by, key=lambda x: np.argsort(index_natsorted(sd[sort_by])))
    a = 1
    '''