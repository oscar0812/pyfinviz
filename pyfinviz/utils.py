import requests
from bs4 import BeautifulSoup
from fp.fp import FreeProxy

import re
import numpy as np
import pandas as pd


class WebScraper:
    @staticmethod
    def get_proxy():
        while 1:
            proxy = FreeProxy(country_id=['US'], rand=True).get()
            if proxy is not None:
                break
        return proxy

    @staticmethod
    def get_soup(main_url, use_proxy=False, remove_imports=True):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/87.0.4280.88 Safari/537.36'}
        if use_proxy:
            p = WebScraper.get_proxy()
            response = requests.get(main_url, headers=headers, proxies={'http': p, 'https': p})
        else:
            response = requests.get(main_url, headers=headers)

        soup = BeautifulSoup(response.content, 'lxml')
        if remove_imports:
            for script in soup(["script", "style"]):  # remove all javascript and stylesheet code
                script.extract()
        return soup

    @staticmethod
    def get_json(url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/87.0.4280.88 Safari/537.36'}

        return requests.get(url, headers=headers).json()

    '''
    SOME PAGES ONLY HAVE 1 TABLE PER PAGE.
    FIND THAT TABLE AND RETURN IT AS A pd.DataFrame
    '''

    @staticmethod
    def get_single_table_pandas(main_url):
        soup = WebScraper.get_soup(main_url)
        td = soup.find("td", {"class": "table-top"})
        main_table_rows = td.find_parent("table").find_all("tr")
        table_header = [re.sub(r'[^a-zA-Z0-9]', '', td.text.strip()) for td in
                        main_table_rows[0].find_all("td", recursive=False)]
        table_info_array = np.asarray(
            [[td.text.strip() for td in row.find_all("td", recursive=False)] for row in main_table_rows[1:]])

        return soup, pd.DataFrame(table_info_array, columns=table_header)
