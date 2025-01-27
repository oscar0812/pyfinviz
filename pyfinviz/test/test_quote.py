from unittest import TestCase

from pyfinviz.quote import Quote


class TestQuote(TestCase):

    def test_main_AMZN(self):
        quote = Quote('AMZN')

        self.assertIsNotNone(quote)
        self.assertTrue(quote.exists)
        self.assertEqual('AMZN', quote.ticker)
        self.assertEqual('Amazon.com Inc', quote.company_name)
        self.assertIsNotNone(quote.profile_bio)
        self.assertEqual('NASD', quote.exchange)
        self.assertEqual(['Consumer Cyclical', 'Internet Retail', 'USA'], quote.sectors)
        self.assertIsNotNone(quote.price_date)
        self.assertIsNotNone(quote.price)
        self.assertIsNotNone(quote.dollar_change)
        self.assertIsNotNone(quote.percentage_change)
        self.assertLessEqual(72, quote.fundamental_df.columns.size)
        self.assertEqual(1, len(quote.fundamental_df))
        self.assertEqual(5, quote.outer_ratings_df.columns.size)
        self.assertEqual(20, len(quote.outer_ratings_df))
        self.assertEqual(4, quote.outer_news_df.columns.size)
        self.assertGreater(len(quote.outer_news_df), 0)
        self.assertGreater(quote.income_statement_df.columns.size, 0)
        self.assertEqual(8, len(quote.income_statement_df))
        self.assertEqual('Period End Date', quote.income_statement_df.columns.tolist()[0])
        self.assertEqual(11, quote.insider_trading_df.columns.size)
        self.assertEqual(39, quote.balance_sheet_df.columns.size)
        self.assertEqual(8, len(quote.balance_sheet_df))
        self.assertEqual('Period End Date', quote.balance_sheet_df.columns.tolist()[0])
        self.assertEqual(36, quote.cash_flow_df.columns.size)
        self.assertEqual(8, len(quote.cash_flow_df))
        self.assertEqual('Period End Date', quote.cash_flow_df.columns.tolist()[0])
        self.assertIsNotNone(quote.stockwits_news_df)
        self.assertGreater(len(quote.stockwits_news_df), 0)
        self.assertIsNotNone(quote.managers_and_funds_df)

    def test_main_META(self):
        quote = Quote('META')

        self.assertIsNotNone(quote)
        self.assertTrue(quote.exists)
        self.assertEqual('META', quote.ticker)
        self.assertEqual('Meta Platforms Inc', quote.company_name)
        self.assertIsNotNone(quote.profile_bio)
        self.assertEqual('NASD', quote.exchange)
        self.assertEqual(['Communication Services', 'Internet Content & Information', 'USA'], quote.sectors)
        self.assertIsNotNone(quote.price_date)
        self.assertIsNotNone(quote.price)
        self.assertIsNotNone(quote.dollar_change)
        self.assertIsNotNone(quote.percentage_change)
        self.assertLessEqual(72, quote.fundamental_df.columns.size)
        self.assertEqual(1, len(quote.fundamental_df))
        self.assertEqual(5, quote.outer_ratings_df.columns.size)
        self.assertEqual(20, len(quote.outer_ratings_df))
        self.assertEqual(4, quote.outer_news_df.columns.size)
        self.assertGreater(len(quote.outer_news_df), 0)
        self.assertGreater(quote.income_statement_df.columns.size, 0)
        self.assertEqual(8, len(quote.income_statement_df))
        self.assertEqual('Period End Date', quote.income_statement_df.columns.tolist()[0])
        self.assertEqual(11, quote.insider_trading_df.columns.size)
        self.assertEqual(100, len(quote.insider_trading_df))
        self.assertEqual(['Insider Trading', 'Insider History URL', 'Relationship', 'Date', 'Transaction', 'Cost',
                          '#Shares', 'Value ($)', '#Shares Total', 'SEC Form 4', 'SEC Form 4 URL'],
                         quote.insider_trading_df.columns.tolist())
        self.assertEqual(39, quote.balance_sheet_df.columns.size)
        self.assertEqual(8, len(quote.balance_sheet_df))
        self.assertEqual('Period End Date', quote.balance_sheet_df.columns.tolist()[0])
        self.assertEqual(36, quote.cash_flow_df.columns.size)
        self.assertEqual(8, len(quote.cash_flow_df))
        self.assertEqual('Period End Date', quote.cash_flow_df.columns.tolist()[0])
        self.assertIsNotNone(quote.stockwits_news_df)
        self.assertGreater(len(quote.stockwits_news_df), 0)
        self.assertIsNotNone(quote.managers_and_funds_df)

    def test_main_NNDM(self):
        quote = Quote('NNDM')

        self.assertIsNotNone(quote)
        self.assertTrue(quote.exists)
        self.assertEqual('NNDM', quote.ticker)
        self.assertEqual('Nano Dimension Ltd ADR', quote.company_name)
        self.assertIsNotNone(quote.profile_bio)
        self.assertEqual('NASD', quote.exchange)
        self.assertEqual(['Technology', 'Computer Hardware', 'Israel'], quote.sectors)
        self.assertIsNotNone(quote.price_date)
        self.assertIsNotNone(quote.price)
        self.assertIsNotNone(quote.dollar_change)
        self.assertIsNotNone(quote.percentage_change)
        self.assertLessEqual(72, quote.fundamental_df.columns.size)
        self.assertEqual(1, len(quote.fundamental_df))
        self.assertEqual(5, quote.outer_ratings_df.columns.size)
        self.assertEqual(1, len(quote.outer_ratings_df))
        self.assertEqual(4, quote.outer_news_df.columns.size)
        self.assertGreater(len(quote.outer_news_df), 0)
        self.assertGreater(quote.income_statement_df.columns.size, 0)
        self.assertEqual(8, len(quote.income_statement_df))
        self.assertEqual('Period End Date', quote.income_statement_df.columns.tolist()[0])
        self.assertIsNotNone(quote.insider_trading_df)
        self.assertEqual(['Insider Trading', 'Insider History URL', 'Relationship', 'Date', 'Transaction', 'Cost',
                          '#Shares', 'Value ($)', '#Shares Total', 'SEC Form 4', 'SEC Form 4 URL'],
                         quote.insider_trading_df.columns.tolist())
        self.assertEqual(39, quote.balance_sheet_df.columns.size)
        self.assertEqual(8, len(quote.balance_sheet_df))
        self.assertEqual('Period End Date', quote.balance_sheet_df.columns.tolist()[0])
        self.assertEqual(36, quote.cash_flow_df.columns.size)
        self.assertEqual(8, len(quote.cash_flow_df))
        self.assertEqual('Period End Date', quote.cash_flow_df.columns.tolist()[0])
        self.assertIsNotNone(quote.stockwits_news_df)
        self.assertGreater(len(quote.stockwits_news_df), 0)
        self.assertIsNotNone(quote.managers_and_funds_df)

    def test_main_CGC(self):
        quote = Quote('CGC')

        self.assertIsNotNone(quote)
        self.assertTrue(quote.exists)
        self.assertEqual('CGC', quote.ticker)
        self.assertEqual('Canopy Growth Corporation', quote.company_name)
        self.assertIsNotNone(quote.profile_bio)
        self.assertEqual('NASD', quote.exchange)
        self.assertEqual(['Healthcare', 'Drug Manufacturers - Specialty & Generic', 'Canada'], quote.sectors)
        self.assertIsNotNone(quote.price_date)
        self.assertIsNotNone(quote.price)
        self.assertIsNotNone(quote.dollar_change)
        self.assertIsNotNone(quote.percentage_change)
        self.assertLessEqual(72, quote.fundamental_df.columns.size)
        self.assertEqual(1, len(quote.fundamental_df))
        self.assertEqual(5, quote.outer_ratings_df.columns.size)
        self.assertEqual(20, len(quote.outer_ratings_df))
        self.assertEqual(4, quote.outer_news_df.columns.size)
        self.assertGreater(len(quote.outer_news_df), 0)
        self.assertGreater(quote.income_statement_df.columns.size, 0)
        self.assertEqual(8, len(quote.income_statement_df))
        self.assertEqual('Period End Date', quote.income_statement_df.columns.tolist()[0])
        self.assertEqual(11, quote.insider_trading_df.columns.size)
        self.assertEqual(['Insider Trading', 'Insider History URL', 'Relationship', 'Date', 'Transaction', 'Cost',
                          '#Shares', 'Value ($)', '#Shares Total', 'SEC Form 4', 'SEC Form 4 URL'],
                         quote.insider_trading_df.columns.tolist())
        self.assertEqual(39, quote.balance_sheet_df.columns.size)
        self.assertEqual(8, len(quote.balance_sheet_df))
        self.assertEqual('Period End Date', quote.balance_sheet_df.columns.tolist()[0])
        self.assertEqual(36, quote.cash_flow_df.columns.size)
        self.assertEqual(8, len(quote.cash_flow_df))
        self.assertEqual('Period End Date', quote.cash_flow_df.columns.tolist()[0])
        self.assertIsNotNone(quote.stockwits_news_df)
        self.assertGreater(len(quote.stockwits_news_df), 0)
        self.assertIsNone(quote.managers_and_funds_df)

    def test_main_NOW(self):
        quote = Quote('NOW')

        self.assertIsNotNone(quote)
        self.assertTrue(quote.exists)
        self.assertEqual('NOW', quote.ticker)
        self.assertEqual('ServiceNow Inc', quote.company_name)
        self.assertIsNotNone(quote.profile_bio)
        self.assertEqual('NYSE', quote.exchange)
        self.assertEqual(['Technology', 'Software - Application', 'USA'], quote.sectors)
        self.assertIsNotNone(quote.price_date)
        self.assertIsNotNone(quote.price)
        self.assertIsNotNone(quote.dollar_change)
        self.assertIsNotNone(quote.percentage_change)
        self.assertLessEqual(72, quote.fundamental_df.columns.size)
        self.assertEqual(1, len(quote.fundamental_df))
        self.assertEqual(5, quote.outer_ratings_df.columns.size)
        self.assertEqual(20, len(quote.outer_ratings_df))
        self.assertEqual(4, quote.outer_news_df.columns.size)
        self.assertGreater(len(quote.outer_news_df), 0)
        self.assertGreater(quote.income_statement_df.columns.size, 0)
        self.assertEqual(8, len(quote.income_statement_df))
        self.assertEqual('Period End Date', quote.income_statement_df.columns.tolist()[0])
        self.assertEqual(11, quote.insider_trading_df.columns.size)
        self.assertEqual(['Insider Trading', 'Insider History URL', 'Relationship', 'Date', 'Transaction', 'Cost',
                          '#Shares', 'Value ($)', '#Shares Total', 'SEC Form 4', 'SEC Form 4 URL'],
                         quote.insider_trading_df.columns.tolist())
        self.assertEqual(39, quote.balance_sheet_df.columns.size)
        self.assertEqual(8, len(quote.balance_sheet_df))
        self.assertEqual('Period End Date', quote.balance_sheet_df.columns.tolist()[0])
        self.assertEqual(36, quote.cash_flow_df.columns.size)
        self.assertEqual(8, len(quote.cash_flow_df))
        self.assertEqual('Period End Date', quote.cash_flow_df.columns.tolist()[0])
        self.assertIsNotNone(quote.stockwits_news_df)
        self.assertGreater(len(quote.stockwits_news_df), 0)
        self.assertIsNotNone(quote.managers_and_funds_df)

    def test_main_DOESNOTEXIST1(self):
        quote = Quote('DOESNOTEXIST1')

        self.assertIsNotNone(quote)
        self.assertFalse(quote.exists)
        self.assertRaises(AttributeError, lambda: quote.ticker)
        self.assertRaises(AttributeError, lambda: quote.exchange)
        self.assertRaises(AttributeError, lambda: quote.company_name)
        self.assertRaises(AttributeError, lambda: quote.profile_bio)
        self.assertRaises(AttributeError, lambda: quote.sectors)
        self.assertRaises(AttributeError, lambda: quote.price_date)
        self.assertRaises(AttributeError, lambda: quote.price)
        self.assertRaises(AttributeError, lambda: quote.dollar_change)
        self.assertRaises(AttributeError, lambda: quote.percentage_change)
        self.assertRaises(AttributeError, lambda: quote.fundamental_df)
        self.assertRaises(AttributeError, lambda: quote.outer_ratings_df)
        self.assertRaises(AttributeError, lambda: quote.outer_news_df)
        self.assertRaises(AttributeError, lambda: quote.income_statement_df)
        self.assertRaises(AttributeError, lambda: quote.insider_trading_df)
        self.assertRaises(AttributeError, lambda: quote.balance_sheet_df)
        self.assertRaises(AttributeError, lambda: quote.cash_flow_df)
        self.assertRaises(AttributeError, lambda: quote.stockwits_news_df)
        self.assertRaises(AttributeError, lambda: quote.managers_and_funds_df)
