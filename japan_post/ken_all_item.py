class KenAllItem:
    """
    :param jis_code: 全国地方公共団体コード
    :param old_zip_code: （旧）郵便番号（5桁）
    :param zip_code: 郵便番号（7桁）
    :param prefecture_name_kana: 都道府県名（カタカナ)
    :param shikuchoson_name_kana: 市区町村名（カタカナ）
    :param choiki_name_kana: 町域名（カタカナ）
    :param prefecture_name: 都道府県名（漢字)
    :param shikuchoson_name: 市区町村名（漢字）
    :param choiki_name: 町域名（漢字）
    :param is_multipule_zip_code: 一町域が二以上の郵便番号で表される場合の表示
    :param has_koaza: 小字毎に番地が起番されている町域の表示
    :param has_chome: 丁目を有する町域の場合の表示
    :param is_multiple_chome: 一つの郵便番号で二以上の町域を表す場合の表示
    :param has_update: 更新の表示（「0」は変更なし、「1」は変更あり、「2」廃止（廃止データのみ使用））
    :param reason: 変更理由　（
                 「0」は変更なし
                 「1」市政・区政・町政・分区・政令指定都市施行
                 「2」住居表示の実施、
                 「3」区画整理、
                 「4」郵便区調整等、
                 「5」訂正、
                 「6」廃止（廃止データのみ使用）
    """

    def __init__(self,
                 jis_code: str,
                 old_zip_code: str,
                 zip_code: str,
                 prefecture: str,
                 shikuchoson: str,
                 choiki1: str,
                 choiki2: str,
                 is_multipule_zip_code: bool,
                 has_koaza: bool,
                 has_chome: bool,
                 is_multiple_chome: bool,
                 has_update: int,
                 reason: int):
        self.jis_code = jis_code
        self.old_zip_code = old_zip_code
        self.zip_code = zip_code
        self.prefecture = prefecture
        self.shikuchoson = shikuchoson
        self.choiki1 = choiki1
        self.choiki2 = choiki2
        self.is_multipule_zip_code = is_multipule_zip_code
        self.has_koaza = has_koaza
        self.has_chome = has_chome
        self.is_multiple_chome = is_multiple_chome
        self.has_update = has_update
        self.reason = reason

