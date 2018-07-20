from pathlib import Path

from japan_post import ken_all
from japan_post.ken_all_sqlite_accessor import KenAllSQliteAccessor


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
        sqlite_accessor = KenAllSQliteAccessor(path)
        sqlite_accessor.create_table()
        sqlite_accessor.insert_rows(ken_all.concatinate_read(csv_path))
        sqlite_accessor.close()

    def parse(self, address):
        pass
