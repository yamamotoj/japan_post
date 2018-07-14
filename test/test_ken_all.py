import unittest
from pathlib import Path

from japan_post import ken_all


class KenAllTest(unittest.TestCase):

    # def test_fetch(self):
    #     ken_all.fetch()

    def test_concat_read(self):
        path = Path('cache/KEN_ALL.csv')
        for r in ken_all.concatinate_read(path):
            pass




