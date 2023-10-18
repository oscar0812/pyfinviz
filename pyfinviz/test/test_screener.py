from unittest import TestCase

from pyfinviz import Screener


class TestScreener(TestCase):
    def test_page_number(self):
        self.assertEqual('1', Screener.page_number(1))
        self.assertEqual('21', Screener.page_number(2))
        self.assertEqual('41', Screener.page_number(3))
        self.assertEqual('61', Screener.page_number(4))
        self.assertEqual('81', Screener.page_number(5))
        self.assertEqual('101', Screener.page_number(6))
        self.assertEqual('121', Screener.page_number(7))
        # ...
        self.assertEqual('941', Screener.page_number(48))
        self.assertEqual('961', Screener.page_number(49))
        self.assertEqual('981', Screener.page_number(50))
        # ...
        self.assertEqual('1941', Screener.page_number(98))
        self.assertEqual('1961', Screener.page_number(99))
        self.assertEqual('1981', Screener.page_number(100))

    def test_main_DEFAULT_VALUES(self):
        screener = Screener()

        self.assertIsNotNone(screener)
        self.assertEqual('https://finviz.com/screener.ashx?ft=4&v=111&s=&f=&r=', screener.main_url)
        self.assertEqual([1], list(screener.soups.keys()))  # get page 1 by default
        self.assertEqual([1], list(screener.data_frames.keys()))  # get page 1 by default
        self.assertEqual(['No', 'Ticker', 'Company', 'Sector', 'Industry', 'Country', 'MarketCap',
                          'PE', 'Price', 'Change', 'Volume'], screener.data_frames.get(1).columns.to_list())

    def test_main_FILTER_NASDAQ_and_FILTER_S_AND_P500_and_VIEWOPTION_VALUATION_PAGES_1_3(self):
        pages = [1, 3]
        screener = Screener(filter_options=[Screener.ExchangeOption.NASDAQ, Screener.IndexOption.S_AND_P_500],
                            view_option=Screener.ViewOption.VALUATION,
                            pages=pages)

        self.assertIsNotNone(screener)
        self.assertEqual('https://finviz.com/screener.ashx?ft=4&v=121&s=&f=exch_nasd,idx_sp500&r=', screener.main_url)
        self.assertCountEqual(pages, list(screener.soups.keys()))  # assert equal elements regardless of order
        self.assertCountEqual(pages, list(screener.data_frames.keys()))  # assert equal elements regardless of order

        expected_columns = ['No', 'Ticker', 'MarketCap', 'PE', 'FwdPE', 'PEG', 'PS', 'PB', 'PC', 'PFCF', 'EPSthisY',
                            'EPSnextY', 'EPSpast5Y', 'EPSnext5Y', 'Salespast5Y', 'Price', 'Change', 'Volume']

        self.assertEqual(expected_columns, screener.data_frames.get(1).columns.to_list())
        self.assertEqual(expected_columns, screener.data_frames.get(3).columns.to_list())
