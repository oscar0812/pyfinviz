from unittest import TestCase

from pyfinviz import News


class TestNews(TestCase):

    def test_market_news(self):
        news = News(view_option=News.ViewOption.MARKET_NEWS)

        self.assertIsNotNone(news)
        self.assertEqual('https://finviz.com/news.ashx?v=1', news.main_url)
        self.assertEqual(3, news.news_df.columns.size)
        self.assertEqual(3, news.blogs_df.columns.size)

        first_row = news.news_df.iloc[0].to_list()
        self.assertIsNotNone(first_row)
        self.assertEqual(3, len(first_row))
        self.assertIsNotNone(first_row[0])
        self.assertIsNotNone(first_row[1])
        self.assertLess(0, len(first_row[1]))
        self.assertIsNotNone(first_row[2])
        self.assertLess(0, len(first_row[2]))

        first_row = news.blogs_df.iloc[0].to_list()
        self.assertIsNotNone(first_row)
        self.assertEqual(3, len(first_row))
        self.assertIsNotNone(first_row[0])
        self.assertIsNotNone(first_row[1])
        self.assertLess(0, len(first_row[1]))
        self.assertIsNotNone(first_row[2])
        self.assertLess(0, len(first_row[2]))

    def test_stock_news(self):
        news = News(view_option=News.ViewOption.STOCKS_NEWS)

        self.assertIsNotNone(news)
        self.assertEqual('https://finviz.com/news.ashx?v=3', news.main_url)
        self.assertEqual(3, news.news_df.columns.size)
        self.assertIsNone(news.blogs_df)

        first_row = news.news_df.iloc[0].to_list()
        self.assertIsNotNone(first_row)
        self.assertEqual(3, len(first_row))
        self.assertIsNotNone(first_row[0])
        self.assertIsNotNone(first_row[1])
        self.assertLess(0, len(first_row[1]))
        self.assertIsNotNone(first_row[2])
        self.assertLess(0, len(first_row[2]))

    def test_ETF_news(self):
        news = News(view_option=News.ViewOption.ETF_NEWS)

        self.assertIsNotNone(news)
        self.assertEqual('https://finviz.com/news.ashx?v=4', news.main_url)
        self.assertEqual(3, news.news_df.columns.size)
        self.assertIsNone(news.blogs_df)

        first_row = news.news_df.iloc[0].to_list()
        self.assertIsNotNone(first_row)
        self.assertEqual(3, len(first_row))
        self.assertIsNotNone(first_row[0])
        self.assertIsNotNone(first_row[1])
        self.assertLess(0, len(first_row[1]))
        self.assertIsNotNone(first_row[2])
        self.assertLess(0, len(first_row[2]))

    def test_crypto_news(self):
        news = News(view_option=News.ViewOption.CRYPTO_NEWS)

        self.assertIsNotNone(news)
        self.assertEqual('https://finviz.com/news.ashx?v=5', news.main_url)
        self.assertEqual(3, news.news_df.columns.size)
        self.assertIsNone(news.blogs_df)

        first_row = news.news_df.iloc[0].to_list()
        self.assertIsNotNone(first_row)
        self.assertEqual(3, len(first_row))
        self.assertIsNotNone(first_row[0])
        self.assertIsNotNone(first_row[1])
        self.assertLess(0, len(first_row[1]))
        self.assertIsNotNone(first_row[2])
        self.assertLess(0, len(first_row[2]))
