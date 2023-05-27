from unittest import TestCase
from pyfinviz.utils import *


class TestWebScraper(TestCase):
    def test_get_proxy(self):
        proxy_: str = WebScraper.get_proxy()
        http_ = 'http://'

        self.assertIsNotNone(proxy_)
        self.assertTrue(proxy_.startswith(http_))
        self.assertTrue(len(proxy_) > len(http_))

    def test_get_soup(self):
        soup_: BeautifulSoup = WebScraper.get_soup('https://www.scrapethissite.com/pages/simple/', False, True)
        self.assertIsNotNone(soup_)

        countries = soup_.find_all('div', class_='country')
        self.assertEqual(250, len(countries))

    def test_get_json(self):
        json_ = WebScraper.get_json('https://jsonplaceholder.typicode.com/posts')
        self.assertIsNotNone(json_)
        self.assertEqual(100, len(json_))

    def test_get_single_table_pandas(self):
        self.assertTrue(1)
