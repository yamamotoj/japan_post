import unittest

from japan_post import ken_all_address_splitter


class KenAllAddressSplitterTest(unittest.TestCase):

    def test_split_001(self):
        s = '大江（１丁目、２丁目「６５１、６６２、６６８番地」以外、３丁目５、１３－４、２０、６７８、６８７番地）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('大江', '１丁目'),
            ('大江', '２丁目「６５１番地、６６２番地、６６８番地」を除く'),
            ('大江', '３丁目５番地'),
            ('大江', '３丁目１３番地－４'),
            ('大江', '３丁目２０番地'),
            ('大江', '３丁目６７８番地'),
            ('大江', '３丁目６８７番地')], ret)

    def test_split_002(self):
        s = '大江（２丁目６５１、６６２、６６８番地、３丁目１０３、１１８、２１０、２５４、２６７、３７２、４４４、４６９番地）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('大江', '２丁目６５１番地'),
            ('大江', '２丁目６６２番地'),
            ('大江', '２丁目６６８番地'),
            ('大江', '３丁目１０３番地'),
            ('大江', '３丁目１１８番地'),
            ('大江', '３丁目２１０番地'),
            ('大江', '３丁目２５４番地'),
            ('大江', '３丁目２６７番地'),
            ('大江', '３丁目３７２番地'),
            ('大江', '３丁目４４４番地'),
            ('大江', '３丁目４６９番地')], ret)

    def test_split_003(self):
        s = '江ケ崎（１２～２２、１２７～１４０、１７０９、１７２３－３、１７２８－４番地）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('江ケ崎', '１２番地〜２２番地'),
            ('江ケ崎', '１２７番地〜１４０番地'),
            ('江ケ崎', '１７０９番地'),
            ('江ケ崎', '１７２３番地－３'),
            ('江ケ崎', '１７２８番地－４')], ret)

    def test_split_004(self):
        s = '西早稲田（２丁目１番１～２３号、２番）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('西早稲田', '２丁目１番１号〜２３号'),
            ('西早稲田', '２丁目２番')
        ], ret)

    def test_split_005(self):
        s = '箱石（第２地割「７０～１３６」～第４地割「３～１１」）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('箱石', '第２地割「７０〜１３６」〜第４地割「３〜１１」')
        ], ret)

    def test_split_006(self):
        s = '大豆（１の２、３の２～６、４の２・４・６、１１の１番地）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('大豆', '１番地－２'),
            ('大豆', '３番地－２〜６'),
            ('大豆', '４番地－２'),
            ('大豆', '４番地－４'),
            ('大豆', '４番地－６'),
            ('大豆', '１１番地－１')
        ], ret)

    def test_split_007(self):
        s = '仁礼町（３１５３－１～３１５３－１１００「峰の原」）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('仁礼町', '３１５３－１〜１１００「峰の原」')
        ], ret)

    def test_split_008(self):
        s = '花田町西宿（１１０－２、１１０－７、１１０－１０番地を除く）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('花田町西宿', '（１１０番地－２、１１０番地－７、１１０番地－１０）を除く')
        ], ret)

    def test_split_009(self):
        s = '折茂（今熊「２１３～２３４、２４０、２４７、２６２、２６６、２７５、２７７、２８０、２９５、１１９９、１２０６、１５０４を除く」、大原、沖山、上折茂「１－１３、７１－１９２を除く」）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('折茂', '今熊「２１３〜２３４、２４０、２４７、２６２、２６６、２７５、２７７、２８０、２９５、１１９９、１２０６、１５０４」を除く'),
            ('折茂', '大原'),
            ('折茂', '沖山'),
            ('折茂', '上折茂「１－１３、７１－１９２」を除く')], ret)

    def test_split_010(self):
        s = '土樋（１丁目「１１を除く」）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('土樋', '１丁目「１１」を除く')
        ], ret)

    def test_split_011(self):
        s = '添川（渡戸沢「筍沢温泉」）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('添川', '渡戸沢「筍沢温泉」')
        ], ret)

    def test_split_012(self):
        s = '南山（４３０番地以上「１７７０－１～２、１８６２－４２、１９２３－５を除く」、大谷地、折渡、鍵金野、金山、滝ノ沢、豊牧、沼の台、肘折、平林）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('南山', '４３０番地以上「１７７０－１〜２、１８６２－４２、１９２３－５」を除く'),
            ('南山', '大谷地'),
            ('南山', '折渡'),
            ('南山', '鍵金野'),
            ('南山', '金山'),
            ('南山', '滝ノ沢'),
            ('南山', '豊牧'),
            ('南山', '沼の台'),
            ('南山', '肘折'),
            ('南山', '平林')], ret)

    def test_split_013(self):
        s = '赤坂赤坂アークヒルズ・アーク森ビル（地階・階層不明）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('赤坂赤坂アークヒルズ・アーク森ビル', '地階・階層不明')
        ], ret)

    def test_split_014(self):
        s = '野牛（稲崎平３０２番地・３１５番地、トクサ沢）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('野牛', '稲崎平３０２番地'),
            ('野牛', '稲崎平３１５番地'),
            ('野牛', 'トクサ沢')
        ], ret)

    def test_split_015(self):
        s = '戸山（３丁目１８・２１番）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('戸山', '３丁目１８番'),
            ('戸山', '３丁目２１番')
        ], ret)

    def test_split_016(self):
        s = '穴明２２地割、穴明２３地割'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('穴明', '２２地割'),
            ('穴明', '２３地割')
        ], ret)

    def test_split_017(self):
        s = '毛萱（前川原２３２～２４４、３１１、３１２、３３７～８６２番地〔東京電力福島第二原子力発電所構内〕）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('毛萱', '前川原２３２番地〜２４４番地'),
            ('毛萱', '前川原３１１番地'),
            ('毛萱', '前川原３１２番地'),
            ('毛萱', '前川原３３７番地〜８６２番地「東京電力福島第二原子力発電所構内」')
        ], ret)

    def test_split_018(self):
        s = '美栄町（西５～８線７９～１１０番地）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('美栄町', '西５線〜８線７９番地〜１１０番地')
        ], ret)

    def test_split_019(self):
        s = '三田市の次に番地がくる場合'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('三田市の次に番地がくる場合', '')
        ], ret)

    def test_split_020(self):
        s = '士幌（南一区１８号～２１号南）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('士幌', '南一区１８号〜２１号南')
        ], ret)

    def test_split_021(self):
        s = '山形村一円'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('山形村一円', '')
        ], ret)

    def test_split_022(self):
        s = '南郷通（南）'
        print(s)
        ret = list(ken_all_address_splitter.split_choiki(s))
        self.assertEqual([
            ('南郷通', '南')
        ], ret)
