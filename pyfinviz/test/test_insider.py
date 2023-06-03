from unittest import TestCase

from pyfinviz import Insider


class TestInsider(TestCase):
    def test_main_DEFAULT_VALUES(self):
        insider = Insider()

        self.assertIsNotNone(insider)
        self.assertEqual('https://finviz.com/insidertrading.ashx?tc=7', insider.main_url)
        self.assertIsNotNone(insider.soup)
        self.assertIsNotNone(insider.table_df)
        self.assertEqual(['Ticker', 'Owner', 'Relationship', 'Date', 'Transaction', 'Cost', 'Shares', 'Value',
                          'SharesTotal', 'SECForm4'], insider.table_df.columns.to_list())

    def test_main_FILTER_OPTION_BUY_and_VIEW_OPTION_TOP_INSIDER_TRADING_RECENT_WEEK(self):
        insider = Insider(filter_option=Insider.FilterOption.BUY,
                          view_option=Insider.ViewOption.TOP_INSIDER_TRADING_RECENT_WEEK)

        self.assertIsNotNone(insider)
        self.assertEqual('https://finviz.com/insidertrading.ashx?tc=1&or=-10&tv=100000&o=-transactionValue',
                         insider.main_url)
        self.assertIsNotNone(insider.soup)
        self.assertIsNotNone(insider.table_df)
        self.assertEqual(['Ticker', 'Owner', 'Relationship', 'Date', 'Transaction', 'Cost', 'Shares', 'Value',
                          'SharesTotal', 'SECForm4'], insider.table_df.columns.to_list())
