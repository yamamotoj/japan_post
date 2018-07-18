import sqlite3
from pathlib import Path

from japan_post import ken_all, ken_all_address_splitter


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
        cursor = connection.cursor()
        for r in ken_all.concatinate_read(csv_path):
            for choiki1, choiki2 in ken_all_address_splitter.split_choiki(r[8]):
                cursor.execute(
                    """
                    INSERT INTO ken_all(jis_code, old_zip_code, zip_code,
                    prefecture, shikuchoson,choiki1, choiki2,is_multipule_zip_code,
                     has_koaza, has_chome, is_multiple_chome,has_update, reason)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        r[0], r[1], r[2], r[6], r[7], choiki1, choiki2, r[9], r[10], r[11], r[12],
                        r[13], r[14]))

        cursor.execute("CREATE INDEX prefecture_index ON ken_all(prefecture);")
        cursor.execute("CREATE INDEX shikuchoson_index ON ken_all(shikuchoson);")
        cursor.execute("CREATE INDEX choiki1_index ON ken_all(choiki1);")
        cursor.execute("CREATE INDEX address_index ON ken_all(prefecture, shikuchoson, choiki1);")
        cursor.execute("CREATE INDEX zip_code_index ON ken_all(zip_code);")
