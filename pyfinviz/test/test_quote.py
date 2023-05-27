from unittest import TestCase
from pyfinviz.quote import Quote


class TestQuote(TestCase):

    def test_main_AMZN(self):
        quote = Quote('AMZN')

        self.assertIsNotNone(quote)
        self.assertTrue(quote.exists)
        self.assertEqual('AMZN', quote.ticker)
        self.assertEqual('[NASD]', quote.exchange)
        self.assertEqual('Amazon.com, Inc.', quote.company_name)
        self.assertEqual(['Consumer Cyclical', 'Internet Retail', 'USA'], quote.sectors)
        self.assertEqual(71, quote.fundamental_df.columns.size)
        self.assertEqual(5, quote.outer_ratings_df.columns.size)
        self.assertEqual(4, quote.outer_news_df.columns.size)
        self.assertEqual(20, quote.income_statement_df.columns.size)
        self.assertEqual(11, quote.insider_trading_df.columns.size)
        self.assertEqual(37, quote.balance_sheet_df.columns.size)
        self.assertEqual(23, quote.cash_flow_df.columns.size)

    def test_main_META(self):
        quote = Quote('META')

        self.assertIsNotNone(quote)
        self.assertTrue(quote.exists)
        self.assertEqual('META', quote.ticker)
        self.assertEqual('[NASD]', quote.exchange)
        self.assertEqual('Meta Platforms, Inc.', quote.company_name)
        self.assertEqual(['Communication Services', 'Internet Content & Information', 'USA'], quote.sectors)
        self.assertEqual(71, quote.fundamental_df.columns.size)
        self.assertEqual(5, quote.outer_ratings_df.columns.size)
        self.assertEqual(4, quote.outer_news_df.columns.size)
        self.assertEqual(20, quote.income_statement_df.columns.size)
        self.assertEqual(11, quote.insider_trading_df.columns.size)
        self.assertEqual(37, quote.balance_sheet_df.columns.size)
        self.assertEqual(23, quote.cash_flow_df.columns.size)

    def test_main_DOESNOTEXIST1(self):
        quote = Quote('DOESNOTEXIST1')

        self.assertIsNotNone(quote)
        self.assertFalse(quote.exists)
        self.assertRaises(AttributeError, lambda: quote.ticker)
        self.assertRaises(AttributeError, lambda: quote.exchange)
        self.assertRaises(AttributeError, lambda: quote.company_name)
        self.assertRaises(AttributeError, lambda: quote.sectors)
        self.assertRaises(AttributeError, lambda: quote.fundamental_df)
        self.assertRaises(AttributeError, lambda: quote.outer_ratings_df)
        self.assertRaises(AttributeError, lambda: quote.outer_news_df)
        self.assertRaises(AttributeError, lambda: quote.income_statement_df)
        self.assertRaises(AttributeError, lambda: quote.insider_trading_df)
        self.assertRaises(AttributeError, lambda: quote.balance_sheet_df)
        self.assertRaises(AttributeError, lambda: quote.cash_flow_df)
