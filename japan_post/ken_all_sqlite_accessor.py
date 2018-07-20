import functools
import sqlite3
from typing import List

from japan_post import ken_all_address_splitter
from japan_post.ken_all_item import KenAllItem


# noinspection SqlNoDataSourceInspection,SqlResolve
class KenAllSQliteAccessor:

    def __init__(self, path):
        self.path = path

    @property
    @functools.lru_cache()
    def connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path)

    def close(self):
        self.connection.close()

    def create_table(self):
        self.connection.execute(
            """
            CREATE TABLE ken_all (
             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
             jis_code TEXT NOT NULL ,
             old_zip_code TEXT NOT NULL ,
             zip_code TEXT NOT NULL ,
             prefecture TEXT NOT NULL ,
             shikuchoson TEXT NOT NULL ,
             choiki1 TEXT NOT NULL ,
             choiki2 TEXT NOT NULL ,
             is_multipule_zip_code INTEGER NOT NULL ,
             has_koaza INTEGER NOT NULL ,
             has_chome INTEGER NOT NULL ,
             is_multiple_chome INTEGER NOT NULL ,
             has_update INTEGER NOT NULL ,
             reason INTEGER  NOT NULL
            );
            """)
        self.connection.execute("CREATE INDEX address_index ON ken_all(shikuchoson, choiki1);")
        self.connection.execute("CREATE INDEX choiki1_index ON ken_all(choiki1);")
        self.connection.commit()

    def insert_rows(self, rows):
        for r in rows:
            for choiki1, choiki2 in ken_all_address_splitter.split_choiki(r[8]):
                self.connection.execute(
                    """
                    INSERT INTO ken_all(jis_code, old_zip_code, zip_code,
                    prefecture, shikuchoson,choiki1, choiki2,is_multipule_zip_code,
                     has_koaza, has_chome, is_multiple_chome,has_update, reason)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        r[0], r[1], r[2], r[6], r[7], choiki1, choiki2, r[9], r[10], r[11], r[12],
                        r[13], r[14]))
        self.connection.commit()

    @functools.lru_cache()
    def select_prefectures(self) -> List[str]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT DISTINCT prefecture FROM ken_all;")
        ret = [r[0] for r in cursor.fetchall()]
        cursor.close()
        return ret

    @functools.lru_cache()
    def select_shikuchoson_by_prefecture(self, prefecture: str) -> List[str]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT DISTINCT shikuchoson FROM ken_all WHERE prefecture=? ;",
                       [prefecture])
        ret = [r[0] for r in cursor.fetchall()]
        cursor.close()
        return ret

    @functools.lru_cache()
    def select_choiki1_by_shikuchoson(self, prefecture: str, shikuchoson: str) -> List[str]:
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT DISTINCT choiki1 FROM ken_all WHERE prefecture=? and shikuchoson=? ;",
            [prefecture, shikuchoson])
        ret = [r[0] for r in cursor.fetchall()]
        cursor.close()
        return ret

    @functools.lru_cache()
    def select_items_by_shikuchoson_and_choiki1(self, shikuchoson: str, choiki1: str) -> List[
        KenAllItem]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT  * FROM ken_all WHERE shikuchoson=? AND choiki1=?;",
                       [shikuchoson, choiki1])
        ret = [KenAllItem(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10],
                          r[11], r[12]) for r in cursor.fetchall()]
        cursor.close()
        return ret
