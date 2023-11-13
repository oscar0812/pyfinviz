from unittest import TestCase

from pyfinviz import Groups


class TestGroups(TestCase):
    def test_main_DEFAULT_VALUES(self):
        groups = Groups()

        self.assertIsNotNone(groups)
        self.assertEqual('https://finviz.com/groups.ashx?g=sector&v=110&o=name', groups.main_url)
        self.assertIsNotNone(groups.soup)
        self.assertIsNotNone(groups.table_df)
        self.assertEqual(['No', 'Name', 'Stocks', 'MarketCap', 'Dividend', 'PE', 'FwdPE', 'PEG', 'FloatShort',
                          'Change', 'Volume'], groups.table_df.columns.to_list())

    def test_main_GROUP_OPTION_INDUSTRY_BASIC_MATERIALS_and_VIEW_OPTON_VALUATION(self):
        groups = Groups(group_option=Groups.GroupOption.INDUSTRY_BASIC_MATERIALS,
                        view_option=Groups.ViewOption.VALUATION)

        self.assertIsNotNone(groups)
        self.assertEqual('https://finviz.com/groups.ashx?g=industry&sg=basicmaterials&v=120&o=name', groups.main_url)
        self.assertIsNotNone(groups.soup)
        self.assertIsNotNone(groups.table_df)
        self.assertEqual(['No', 'Name', 'MarketCap', 'PE', 'FwdPE', 'PEG', 'PS', 'PB', 'PC', 'PFCF', 'EPSpast5Y',
                          'EPSnext5Y', 'Salespast5Y', 'Change', 'Volume'], groups.table_df.columns.to_list())

    def test_main_GROUP_OPTION_SECTOR_and_VIEW_PERFORMANCE_and_ORDER_BY_NAME_ASC(self):
        groups = Groups(group_option=Groups.GroupOption.SECTOR,
                        view_option=Groups.ViewOption.PERFORMANCE,
                        order_by=Groups.OrderBy.NAME,
                        order_direction=Groups.OrderDirection.ASC)

        self.assertIsNotNone(groups)
        self.assertEqual('https://finviz.com/groups.ashx?g=sector&v=140&o=name', groups.main_url)
        self.assertIsNotNone(groups.soup)
        self.assertIsNotNone(groups.table_df)
        self.assertEqual(['No', 'Name', 'PerfWeek', 'PerfMonth', 'PerfQuart', 'PerfHalf', 'PerfYear', 'PerfYTD',
                          'Recom', 'AvgVolume', 'RelVolume', 'Change', 'Volume'], groups.table_df.columns.to_list())

    def test_main_GROUP_OPTION_CAPITALIZATION_and_VIEW_PERFORMANCE_and_ORDER_BY_MARKET_CAPITALIZATION_DESC(self):
        groups = Groups(group_option=Groups.GroupOption.CAPITALIZATION,
                        view_option=Groups.ViewOption.PERFORMANCE,
                        order_by=Groups.OrderBy.MARKET_CAPITALIZATION,
                        order_direction=Groups.OrderDirection.DESC)

        self.assertIsNotNone(groups)
        self.assertEqual('https://finviz.com/groups.ashx?g=capitalization&v=140&o=-marketcap', groups.main_url)
        self.assertIsNotNone(groups.soup)
        self.assertIsNotNone(groups.table_df)
        self.assertEqual(['No', 'Name', 'PerfWeek', 'PerfMonth', 'PerfQuart', 'PerfHalf', 'PerfYear', 'PerfYTD',
                          'Recom', 'AvgVolume', 'RelVolume', 'Change', 'Volume'], groups.table_df.columns.to_list())