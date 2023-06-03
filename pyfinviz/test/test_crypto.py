from unittest import TestCase

from pyfinviz import Crypto


class TestCrypto(TestCase):
    def test_main_DEFAULT_VALUES(self):
        crypto = Crypto()

        self.assertIsNotNone(crypto)
        self.assertEqual('https://finviz.com/crypto_performance.ashx?v=1', crypto.main_url)
        self.assertIsNotNone(crypto.soup)
        self.assertIsNotNone(crypto.table_df)
        self.assertEqual(['No', 'Ticker', 'Price', 'Perf5Min', 'PerfHour', 'PerfDay', 'PerfWeek', 'PerfMonth',
                          'PerfQuart', 'PerfHalf', 'PerfYear', 'PerfYTD'], crypto.table_df.columns.to_list())

    def test_main_RELATIVE_PERFORMANCE_OPTION_YEAR_TO_DATE(self):
        crypto = Crypto(relative_performance_option=Crypto.RelativePerformanceOption.YEAR_TO_DATE)

        self.assertIsNotNone(crypto)
        self.assertEqual('https://finviz.com/crypto_performance.ashx?v=7', crypto.main_url)
        self.assertIsNotNone(crypto.soup)
        self.assertIsNotNone(crypto.table_df)
        self.assertEqual(['No', 'Ticker', 'Price', 'Perf5Min', 'PerfHour', 'PerfDay', 'PerfWeek', 'PerfMonth',
                          'PerfQuart', 'PerfHalf', 'PerfYear', 'PerfYTD'], crypto.table_df.columns.to_list())
