import sqlite3
from pathlib import Path

from japan_post import ken_all


class KenAllAddressParser:

    # noinspection SqlNoDataSourceInspection,SpellCheckingInspection,SqlResolve,SqlInsertValues
    @staticmethod
    def build_database(path: Path, overwrite=True, temporary_dir: Path = Path('cache/')):
        """
        :param path: SQLite path
        :param overwrite: set True if overwrite existing databese file
        :param temporary_dir: path to temporary directory to store download data
        """
        if path.exists():
            if overwrite:
                path.unlink()
            else:
                return

        zip_path = ken_all.download_data(temporary_dir, overwrite)
        csv_path = ken_all.extract_zip(zip_path)

        path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(str(path))
        connection.execute(
            """
            CREATE TABLE ken_all (
             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
             jis_code TEXT NOT NULL ,
             old_zip_code TEXT NOT NULL ,
             zip_code TEXT NOT NULL ,
             prefecture_name_kana TEXT NOT NULL ,
             shikuchoson_name_kana TEXT NOT NULL ,
             choiki_name_kana TEXT NOT NULL ,
             prefecture_name TEXT NOT NULL ,
             shikuchoson_name TEXT NOT NULL ,
             choiki_name TEXT NOT NULL ,
             is_multipule_zip_code INTEGER NOT NULL ,
             has_koaza INTEGER NOT NULL ,
             has_chome INTEGER NOT NULL ,
             is_multiple_chome INTEGER NOT NULL ,
             has_update INTEGER NOT NULL ,
             reason INTEGER  NOT NULL
            );
            """)
        for r in ken_all.concatinate_read(csv_path):
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO ken_all(jis_code, old_zip_code, zip_code, prefecture_name_kana,
                 shikuchoson_name_kana, choiki_name_kana, prefecture_name, shikuchoson_name,
                 choiki_name, is_multipule_zip_code, has_koaza, has_chome, is_multiple_chome,
                 has_update, reason)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, r)
