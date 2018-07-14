import csv
import unittest
from pathlib import Path

from japan_post import ken_all


class KenAllTest(unittest.TestCase):
    pass

    # def test_fetch(self):
    #     ken_all.fetch()
    #
    # def test_concat_read(self):
    #     out_path = Path('cache/ken_all_concatenated.csv')
    #     path = Path('cache/KEN_ALL.csv')
    #     with out_path.open('w') as out_file:
    #         writer = csv.writer(out_file)
    #         for r in ken_all.concatinate_read(path):
    #             writer.writerow(r)
    #
    #


