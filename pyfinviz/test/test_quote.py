from unittest import TestCase
from unittest.mock import patch, Mock

from bs4 import BeautifulSoup

from pyfinviz.quote import Quote


class TestQuote(TestCase):
    @patch("pyfinviz.quote.BeautifulSoup")
    def test__get_outer_ratings_df__TABLE_IS_NONE(self, mock_soup):
        mock_soup.find.return_value = None

        assert Quote.__get_outer_ratings_df__(mock_soup) is None

    @patch("pyfinviz.utils.WebScraper.get_soup")
    def test_main_AMZN(self, mock_get_soup: Mock):
        with open('html/quote_amzn.html', 'r') as f:
            mock_get_soup.return_value = BeautifulSoup(f.read(), 'lxml')

        quote = Quote('AMZN')

        self.assertIsNotNone(quote)
        self.assertTrue(quote.exists)
        self.assertEqual('AMZN', quote.ticker)
        self.assertEqual('[NASD]', quote.exchange)
        self.assertEqual('Amazon.com, Inc.', quote.company_name)
        self.assertEqual(['Consumer Cyclical', 'Internet Retail', 'USA'], quote.sectors)
        self.assertEqual(71, quote.fundamental_df.columns.size)
        self.assertEqual(1, len(quote.fundamental_df))
        self.assertEqual(5, quote.outer_ratings_df.columns.size)
        self.assertEqual(20, len(quote.outer_ratings_df))
        self.assertEqual(4, quote.outer_news_df.columns.size)
        self.assertEqual(100, len(quote.outer_news_df))
        self.assertEqual(20, quote.income_statement_df.columns.size)
        self.assertEqual(8, len(quote.income_statement_df))
        self.assertEqual(11, quote.insider_trading_df.columns.size)
        self.assertEqual(91, len(quote.insider_trading_df))
        self.assertEqual(37, quote.balance_sheet_df.columns.size)
        self.assertEqual(8, len(quote.balance_sheet_df))
        self.assertEqual(23, quote.cash_flow_df.columns.size)
        self.assertEqual(8, len(quote.cash_flow_df))

    @patch("pyfinviz.utils.WebScraper.get_soup")
    def test_main_META(self, mock_get_soup: Mock):
        with open('html/quote_meta.html', 'r') as f:
            mock_get_soup.return_value = BeautifulSoup(f.read(), 'lxml')

        quote = Quote('META')

        self.assertIsNotNone(quote)
        self.assertTrue(quote.exists)
        self.assertEqual('META', quote.ticker)
        self.assertEqual('[NASD]', quote.exchange)
        self.assertEqual('Meta Platforms, Inc.', quote.company_name)
        self.assertEqual(['Communication Services', 'Internet Content & Information', 'USA'], quote.sectors)
        self.assertEqual(71, quote.fundamental_df.columns.size)
        self.assertEqual(1, len(quote.fundamental_df))
        self.assertEqual(5, quote.outer_ratings_df.columns.size)
        self.assertEqual(20, len(quote.outer_ratings_df))
        self.assertEqual(4, quote.outer_news_df.columns.size)
        self.assertEqual(100, len(quote.outer_news_df))
        self.assertEqual(20, quote.income_statement_df.columns.size)
        self.assertEqual(8, len(quote.income_statement_df))
        self.assertEqual(11, quote.insider_trading_df.columns.size)
        self.assertEqual(100, len(quote.insider_trading_df))
        self.assertEqual(37, quote.balance_sheet_df.columns.size)
        self.assertEqual(8, len(quote.balance_sheet_df))
        self.assertEqual(23, quote.cash_flow_df.columns.size)
        self.assertEqual(8, len(quote.cash_flow_df))

    @patch("pyfinviz.utils.WebScraper.get_soup")
    def test_main_DOESNOTEXIST1(self, mock_get_soup: Mock):
        with open('html/quote_doesnotexist1.html', 'r') as f:
            mock_get_soup.return_value = BeautifulSoup(f.read(), 'lxml')

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
