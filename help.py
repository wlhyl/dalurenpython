from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


class HelpDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # QtWidgets.QDialog(self,parent)
        self.setWindowTitle("帮助")
        self.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint)
        self.resize(700, 500)
        guaTiLayout = QtWidgets.QVBoxLayout()
        # self.layout=helpLayout
        self.setLayout(guaTiLayout)
        self.guaTiTextBrowser = QtWidgets.QTextBrowser()
        guaTiLayout.addWidget(self.guaTiTextBrowser)
        guaTiStrings = ("<div><font style=font-weight:bold;>说明：</font></div>"
                       "<div>八三四九为阳宫，二七六一为阴宫</div>"
                       "<div>太乙在一、八、三、四宫为内，助主；太乙在九、二、七、六宫为在外，助客 </div>"
                       "<div>阴阳易绝之气举事皆凶</div>"
                       "<div> 数 &lt; 10: 无天之算 </div>"
                       "<div> 数 % 10 &lt; 5: 无地之算 </div>"
                       "<div> 数 % 10 == 0: 无人之算 </div>"
                       "<div>开休生大吉，景小吉，惊小凶，杜死伤大凶</div>"
                       "<div><font style=font-weight:bold;color:red>格局：</font>"
                       "</div>"
                       "<div><font style=font-weight:bold;>掩 ：</font><div>"
                       "《经》曰：始击将临太乙宫，谓之掩。岁计遇之，王纲失序，臣强群弱，宜修德以禳之。"
                       "盖掩袭劫杀之义。若掩太乙在阳绝之地，君凶；阴绝之地，臣诛。掩主大将，主人算和，"
                       "吉；不和凶。参将击之胜。</div></div>"
                       "<div><font style=font-weight:bold;>击：</font><div>《经》曰："
                       "太乙所在宫，客目在太乙前一辰，为前击；在太乙后一辰，为后击；在太乙前一宫，为外宫击；"
                       "在太乙后一宫，为内宫击。所为击者，臣凌君卑。凌尊，下凌上，僭也。岁计遇之，将相相伐之义也。"
                       "</div></div>"
                       "<div><font style=font-weight:bold;>迫：</font><div>《经》曰："
                       "前为外迫，后为内迫，为上、下二目，主、客大小四将，在太乙左右为迫。"
                       "王希明曰：下目无迫。若上目在太乙前一辰，为外辰迫；在后一辰，为内辰迫； 在太乙前一宫，"
                       "为外宫迫；后一宫，为内宫迫。宫迫，灾微缓；"
                       "辰迫，灾急疾。岁计遇迫，人君慎之。</div></div>"
                       "<div><font style=font-weight:bold;>囚：</font><div>《经》曰："
                       "囚者，篡戮之义也。若文昌将并主、客、大、小四将俱与太乙同宫，总名曰囚。"
                       "若在易气、绝气之地，大凶；若在绝阳、绝阴之地，自败，臣受诛。若诸将与太乙同宫，或近大将，"
                       "谋在同类；近参将，谋在内也。算和者，利；算不和者，谋不成也。"
                       "（中国古代星占学，靠近天目者谋在内及同姓，近地目者谋在外及异姓。若算和谋成，"
                       "算不和则谋不成。）</div></div>"
                       "<div><font style=font-weight:bold;>关：</font><div>《经》曰："
                       "客、主、大、小将目相宫齐为关。王希明曰：关之为义，但将相怕忌之事，不及于君也。"
                       "主、客、大、小将同宫数齐，皆为关日。 </div></div>"
                       "<div><font style=font-weight:bold;>格：</font><div>《经》曰："
                       "客目、大、小将与太乙对宫为格，言政事上下格也。若在阳绝之地，又与岁计遇格，不利。"
                       "有为所格者，格易之义也，若格太乙者，盗侮其君，主客算不知者必败。</div></div>"
                       "<div><font style=font-weight:bold;>对：</font><div>《经》曰："
                       "下目文昌将与太乙冲而相当都为对，若下目相对之时皆为大臣怀二心，君逐良将，凶奸生，下"
                       "臣欺上。</div></div>"
                       "<div><font style=font-weight:bold;>四郭固：</font><div>"
                       "《经》曰："
                       "四郭固者，文昌将囚太乙宫，至大将参将又相关，或客目临之或客大小将相关，皆四郭固也。"
                       "主人胜固者凭胜不利先起四郭之固岁计遇之主篡废之祸利以修德禳之也。"
                       "《太乙通解》四郭固是指天子之都邑，四面皆有城墙，宜坚壁固守，谨防灾变。</div></div>"
                       )
        guaTiFont = QtGui.QFont()
        guaTiFont.setPixelSize(18)
        self.guaTiTextBrowser.setFont(guaTiFont)
        self.guaTiTextBrowser.setHtml(guaTiStrings)