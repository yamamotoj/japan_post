import unittest
from pathlib import Path

from japan_post import ken_all
from japan_post.ken_all_address_parser import KenAllAddressParser


class KenAllAddressParserTest(unittest.TestCase):

    def test_build_database(self):
        KenAllAddressParser.build_database(Path('cache/ken_all.sqlite'))
