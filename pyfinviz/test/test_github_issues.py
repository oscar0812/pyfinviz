from unittest import TestCase

from pyfinviz.screener import Screener


class TestGithubIssues(TestCase):

    def test(self):
        options = [
            Screener.IndustryOption.ALUMINUM
        ]

        screener = Screener(filter_options=options, view_option=Screener.ViewOption.VALUATION,
                            pages=[x for x in range(1, 4)])
        data = screener.data_frames[1]

