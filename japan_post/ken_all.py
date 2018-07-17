import codecs
import csv
import os
import zipfile
from pathlib import Path
from typing import Generator, Tuple

import requests


def download_data() -> Path:
    url = 'http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip'
    response = requests.get(url)

    path = Path('cache') / 'ken_all.zip'
    with open(path, 'wb') as f:
        f.write(response.content)
    return path


def extract_zip(zip_path: Path) -> Generator[Path, None, None]:
    """
    zipを解凍してcsvに保存する
    """
    area_dir = zip_path.parent
    zip_doc = zipfile.ZipFile(str(zip_path))
    csv_files = [i.filename for i in zip_doc.filelist if str.lower(i.filename).endswith('.csv')]
    for csv_filename in csv_files:
        filename = area_dir / os.path.split(csv_filename)[1]
        tmp_filename = filename.with_suffix('.tmp')
        with open(tmp_filename, 'wb') as f:
            f.write(zip_doc.read(csv_filename))

        with codecs.open(tmp_filename, 'r', 'cp932') as f_in:
            with codecs.open(filename, "w", "utf-8") as f_out:
                for row in f_in:
                    f_out.write(row)
        os.remove(tmp_filename)
        yield filename


def get_chome_state(row) -> int:
    count = 0
    for c in row[8]:
        if c == '（':
            count += 1
        if c == '）':
            count -= 1
    return count


def concat_row(row1, row2) -> Tuple:
    row = []
    for i, r in enumerate(zip(row1, row2)):
        if r[0] == r[1]:
            row.append(r[1])
        else:
            row.append(r[0] + r[1])

    return tuple(row)


def concatinate_read(path: Path) -> Generator[Tuple, None, None]:
    """
    :param path:
    :return:
    """
    with path.open('r') as f:
        prev_row = None
        for row in csv.reader(f):
            chome_state = get_chome_state(row)
            if prev_row:
                if chome_state == 0:
                    prev_row = concat_row(prev_row, row)
                elif chome_state == -1:
                    prev_row = concat_row(prev_row, row)
                    yield prev_row
                    prev_row = None
                elif chome_state == 1:
                    raise Exception(f'illegal state:{chome_state} {row}')
                else:
                    raise Exception(f'illegal state:{chome_state} {row}')
            else:
                if chome_state == 0:
                    yield row
                elif chome_state == -1:
                    raise Exception(f'illegal state:{chome_state} {row}')
                elif chome_state == 1:
                    prev_row = row
                else:
                    raise Exception(f'illegal state:{chome_state} {row}')
