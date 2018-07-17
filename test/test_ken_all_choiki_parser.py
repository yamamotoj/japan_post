import csv
import unittest

from japan_post import ken_all_choiki_yacc
from test.geo_coder import GeoCoder


class KenAllChoikiParserTest(unittest.TestCase):

    def test_choiki_parse001(self):
        s = '大江（１丁目、２丁目「６５１、６６２、６６８番地」以外、３丁目５、１３－４、２０、６７８、６８７番地）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('大江-(1丁目,2丁目-除く-(651番地,662番地,668番地),3丁目-(5番地,13番地-4,20番地,678番地,687番地))',
                         str(ret), s)

    def test_choiki_parse002(self):
        s = '大江（２丁目６５１、６６２、６６８番地、３丁目１０３、１１８、２１０、２５４、２６７、３７２、４４４、４６９番地）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual(
            '大江-(2丁目-(651番地,662番地,668番地),3丁目-(103番地,118番地,210番地,254番地,267番地,372番地,444番地,469番地))',
            str(ret), s)

    def test_choiki_parse003(self):
        s = '江ケ崎（１２～２２、１２７～１４０、１７０９、１７２３－３、１７２８－４番地）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('江ケ崎-([12番地~22番地],[127番地~140番地],1709番地,1723番地-3,1728番地-4)', str(ret), s)

    def test_choiki_parse004(self):
        s = '西早稲田（２丁目１番１～２３号、２番）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('西早稲田-2丁目-(1番-[1号~23号],2番)', str(ret), s)

    def test_choiki_parse005(self):
        s = '箱石（第２地割「７０～１３６」～第４地割「３～１１」）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('箱石-[第2地割-[70~136]~第4地割-[3~11]]', str(ret), s)

    def test_choiki_parse006(self):
        s = '江戸川（１～３丁目、４丁目１～１４番）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('江戸川-([1丁目~3丁目],4丁目-[1番~14番])', str(ret), s)

    def test_choiki_parse007(self):
        s = '大豆（１の２、３の２～６、４の２・４・６、１１の１番地）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('大豆（1番地-2、3番地-[2~6]、4番地-(2,4,6)、11番地-1）', str(ret), s)

    def test_choiki_parse008(self):
        s = '仁礼町（３１５３－１～３１５３－１１００「峰の原」）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('仁礼町-3153-[1~1100]-峰の原', str(ret), s)

    def test_choiki_parse009(self):
        s = '花田町西宿（１１０－２、１１０－７、１１０－１０番地を除く）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('花田町西宿-除く-(110番地-2,110番地-7,110番地-10)', str(ret), s)

    def test_choiki_parse010(self):
        s = '三ツ松（５９６、８９４－１、９１５－４、９２５、９２７－２、９３２－４、９３４～９６８、１０１３－１、１４６４番地）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual(
            '三ツ松-(596番地,894番地-1,915番地-4,925番地,927番地-2,932番地-4,[934番地~968番地],1013番地-1,1464番地)',
            str(ret), s)

    def test_choiki_parse011(self):
        s = '折茂（今熊「２１３～２３４、２４０、２４７、２６２、２６６、２７５、２７７、２８０、２９５、１１９９、１２０６、１５０４を除く」、大原、沖山、上折茂「１－１３、７１－１９２を除く」）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual(
            '折茂-(今熊-除く-([213~234],240,247,262,266,275,277,280,295,1199,1206,1504),大原,沖山,上折茂-除く-(1-13,71-192))',
            str(ret), s)

    def test_choiki_parse012(self):
        s = '葛巻（第４０地割「５７番地１２５、１７６を除く」～第４５地割）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('葛巻-[第40地割-除く-57番地-(125,176)~第45地割]', str(ret), s)

    def test_choiki_parse013(self):
        s = '土樋（１丁目「１１を除く」）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('土樋-1丁目-除く-11', str(ret), s)

    def test_choiki_parse014(self):
        s = '添川（渡戸沢「筍沢温泉」）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('添川-渡戸沢-筍沢温泉', str(ret), s)

    def test_choiki_parse015(self):
        s = '南山（４３０番地以上「１７７０－１～２、１８６２－４２、１９２３－５を除く」、大谷地、折渡、鍵金野、金山、滝ノ沢、豊牧、沼の台、肘折、平林）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual(
            '南山-(430番地以上-除く-([1770-1~2],1862-42,1923-5),大谷地,折渡,鍵金野,金山,滝ノ沢,豊牧,沼の台,肘折,平林)',
            str(ret), s)

    def test_choiki_parse016(self):
        s = '茂田井（１～５００「２１１番地を除く」「古町」、２５２７～２５２９「土遠」）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('茂田井-([1~500]-(除く-211番地,古町),[2527~2529]-土遠)', str(ret), s)

    def test_choiki_parse017(self):
        s = '牧之原（２５０～３４３番地「２５５、２５６、２５８、２５９、２６２、２７６、２９４～３００、３０２～３０４番地を除く」）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual(
            '牧之原-[250番地~343番地]-除く-(255番地,256番地,258番地,259番地,262番地,276番地,[294番地~300番地],[302番地~304番地])',
            str(ret), s)

    def test_choiki_parse018(self):
        s = '赤坂赤坂アークヒルズ・アーク森ビル（地階・階層不明）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('赤坂赤坂アークヒルズ・アーク森ビル-地階・階層不明', str(ret), s)

    def test_choiki_parse019(self):
        s = '三里塚（御料牧場・成田国際空港内）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('三里塚-(御料牧場,成田国際空港内)', str(ret), s)

    def test_choiki_parse020(self):
        s = '野牛（稲崎平３０２番地・３１５番地、トクサ沢）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('野牛-(稲崎平-(302番地,315番地),トクサ沢)', str(ret), s)

    def test_choiki_parse021(self):
        s = '戸山（３丁目１８・２１番）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('戸山-3丁目-(18番,21番)', str(ret), s)

    def test_choiki_parse022(self):
        s = '西瑞江（４丁目１～２番・１０～２７番、５丁目）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('西瑞江-(4丁目-([1番~2番],[10番~27番]),5丁目)', str(ret), s)

    def test_choiki_parse023(self):
        s = '結東（逆巻・前倉・結東）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('結東-(逆巻,前倉,結東)', str(ret), s)

    def test_choiki_parse024(self):
        s = '岡之原町（８３２の２・４、８５２の３）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('岡之原町-(832-(2,4),852-3)', str(ret), s)

    def test_choiki_parse025(self):
        s = '牧（１～３丁目、白滝Ｂ・Ｃ、高見）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('牧-([1丁目~3丁目],白滝Ｂ,Ｃ,高見)', str(ret), s)

    def test_choiki_parse026(self):
        s = '土居（甲・乙）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('土居-(甲,乙)', str(ret), s)

    def test_choiki_parse027(self):
        s = '山田町下谷上（大上谷、修法ケ原、中一里山「９番地の４、１２番地を除く」長尾山、再度公園）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('山田町下谷上-(大上谷,修法ケ原,中一里山-(除く-(9番地-4,12番地),長尾山),再度公園)', str(ret), s)

    def test_choiki_parse028(self):
        s = '阿寒町上仁々志別'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('阿寒町上仁々志別', str(ret), s)

    def test_choiki_parse029(self):
        s = '穴明２２地割、穴明２３地割'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('穴明-22地割,穴明-23地割', str(ret), s)

    def test_choiki_parse030(self):
        s = '越中畑６４地割～越中畑６６地割'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('越中畑-[64地割~66地割]', str(ret), s)

    def test_choiki_parse031(self):
        s = '滝沢（下川原１９０－１）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('滝沢-下川原-190-1', str(ret), s)

    def test_choiki_parse032(self):
        s = '真光寺ヴィレッジ'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('真光寺ヴィレッジ', str(ret), s)

    def test_choiki_parse033(self):
        s = '毛萱（前川原２３２～２４４、３１１、３１２、３３７～８６２番地〔東京電力福島第二原子力発電所構内〕）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('毛萱-前川原-([232番地~244番地],311番地,312番地,[337番地~862番地]-東京電力福島第二原子力発電所構内)',
                         str(ret), s)

    # def test_choiki_parse034(self):
    #     s = '美栄町（西５～８線７９～１１０番地）'
    #     print(s)
    #     ret = ken_all_choiki_yacc.parse_choiki(s)
    #     self.assertEqual('', str(ret), s)

    def test_choiki_parse035(self):
        s = '位登（猪位金４～７区、清美町）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('位登-(猪位金-[4区~7区],清美町)', str(ret), s)

    def test_choiki_parse036(self):
        s = '大前（細原２２５９～）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('大前-細原-2259以上', str(ret), s)

    def test_choiki_parse037(self):
        s = '新所・岡崎・梅田入会地'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('新所・岡崎・梅田入会地', str(ret), s)

    def test_choiki_parse038(self):
        s = '玖珂町（番地のみ）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('玖珂町-番地', str(ret), s)

    def test_choiki_parse039(self):
        s = '鶴見（大字、番地）'
        ret = ken_all_choiki_yacc.parse_choiki(s)
        self.assertEqual('鶴見-(大字,番地)', str(ret), s)

