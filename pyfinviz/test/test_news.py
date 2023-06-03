from datetime import datetime
from unittest import TestCase

from pyfinviz import News


class TestNews(TestCase):

    def test_main(self):
        news = News()

        self.assertIsNotNone(news)
        self.assertEqual('https://finviz.com/news.ashx', news.main_url)
        self.assertEqual(3, news.news_df.columns.size)
        self.assertEqual(3, news.blogs_df.columns.size)

        first_row = news.news_df.iloc[0].to_list()
        self.assertIsNotNone(first_row)
        self.assertEqual(3, len(first_row))
        self.assertIsNotNone(first_row[0])
        self.assertIsNotNone(datetime.strptime(first_row[0], '%H:%M%p'))  # verify that it is a time
        self.assertIsNotNone(first_row[1])
        self.assertLess(0, len(first_row[1]))
        self.assertIsNotNone(first_row[2])
        self.assertLess(0, len(first_row[2]))

        first_row = news.blogs_df.iloc[0].to_list()
        self.assertIsNotNone(first_row)
        self.assertEqual(3, len(first_row))
        self.assertIsNotNone(first_row[0])
        self.assertIsNotNone(datetime.strptime(first_row[0], '%H:%M%p'))  # verify that it is a time
        self.assertIsNotNone(first_row[1])
        self.assertLess(0, len(first_row[1]))
        self.assertIsNotNone(first_row[2])
        self.assertLess(0, len(first_row[2]))
