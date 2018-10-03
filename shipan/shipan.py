import regex
import json
from prettytable import PrettyTable
from ganzhiwuxin import *
from common import GetLi
from shipan import guati
from common.moonMansions import getMoonMansion


class NoSanchuan(Exception):
    def __init__(self, msg):
        super().__init__()
        self.__msg = msg

    def __str__(self):
        return self.__msg


def 寄宫(g):
    寄宫映射 = [0, 支("寅"), 支("辰"), 支("巳"), 支("未"), 支("巳"), 支("未"), 支("申"), 支("戌"),
                    支("亥"), 支("丑")]
    if not isinstance(g, 干):
        raise ValueError('只有干才有寄宫')
    return 寄宫映射[g.num]


def 干Of寄宫(d):
    if not isinstance(d, 支):
        raise ValueError('从支得到干')
    ganList = []
    for i in range(1, 11):
        if 寄宫(干(i)) == d:
            ganList.append(干(i))
    return ganList


class ShiPan():

    def __init__(self, year, month, day, hour, minutes,
                 second, 月将, 占时, 昼占=True, 占测的事="", 性别=0, 生年=2018):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minutes = minutes
        self.second = second
        self.yueJiang = 支(月将)
        self.zhanShi = 支(占时)
        self.昼占 = 昼占
        self.占测的事 = 占测的事
        self.性别 = 性别
        self.生年 = 生年
        self.四柱与节气 = GetLi(year, month, day, hour, minutes, second)
        self.moonMansion = getMoonMansion(year, month, day, hour, minutes, second)
        self.占日 = self.四柱与节气[2]
        self.空亡 = self.__空亡
        self.tp = TianPan(self.yueJiang, self.zhanShi)
        self.sk = SiKe(self.tp, self.占日)
        self.sc = SanChuan(self.tp, self.sk)
        self.tianJiang = 天将盘(self.tp, self.sk, self.昼占)
        self.本命, self.行年 = self.__年命()
        self.格局 = self.sc.格局
        self.格局comment = []
        guaTiModules = guati
        guaTiFuns = []
        for attr in (a for a in dir(guaTiModules) if a.startswith('do_')):
            callback = getattr(guaTiModules, attr)
            guaTiFuns.append(callback)
        for fun in guaTiFuns:
            fun(self)
        # with open('shipan/guaticomment.json', 'r', encoding='UTF-8') as f:
        #     guaTiCommentJson = json.load(f)
        if "虎视" in self.格局 or "冬蛇掩目" in self.格局:
            self.格局.append("虎视卦")
        if "见机" in self.格局 or "察微" in self.格局 or "复等" in self.格局:
            self.格局.append("涉害卦")
        # for i in self.格局:
        #     __g = ("<div>"
        #            "<font style=font-weight:bold;>{}：</font>"
        #            "<div>{}</div></div>")
        #     __gc = guaTiCommentJson.get(i)
        #     if __gc is None:
        #         continue
        #     self.格局comment.append(__g.format(i, __gc))

    @property
    def table(self):
        __sanChuan = [self.sc.初, self.sc.中, self.sc.末]
        __tianJiang = [self.tianJiang[i] for i in __sanChuan]

        xSanchuan = PrettyTable()

        xSanchuan.header = False
        xSanchuan.padding_width = 0
        xSanchuan.border = 0

        for i in range(0, 3):
            xSanchuan.add_row([" ", "", self.sc.六亲[i], self.sc.遁干[i],
                               __sanChuan[i], __tianJiang[i]])

        siKeTianJiang = ["", ""]
        siKeTianJiang.append(self.tianJiang[self.sk.支阴神])
        siKeTianJiang.append(self.tianJiang[self.sk.支阳神])
        siKeTianJiang.append(self.tianJiang[self.sk.干阴神])
        siKeTianJiang.append(self.tianJiang[self.sk.干阳神])

        xsiKe = PrettyTable()

        xsiKe.header = False
        xsiKe.padding_width = 0
        xsiKe.border = 0

        xsiKe.add_row(siKeTianJiang)
        siKeTable = [
            ["", "", self.sk.支阴神, self.sk.支阳神, self.sk.干阴神, self.sk.干阳神],
            ["", "", self.sk.支阳神, self.sk.支, self.sk.干阳神, self.sk.干]]
        xsiKe.add_row(siKeTable[0])
        xsiKe.add_row(siKeTable[1])

        __tp = self.tp
        diPanTable = [[支("巳"), 支("午"), 支("未"), 支("申")],
                      [支("辰"), None, None, 支("酉")],
                      [支("卯"), None, None, 支("戌")],
                      [支("寅"), 支("丑"), 支("子"), 支("亥")]]
        tianPanTable = []
        for i in diPanTable:
            __row = []
            for j in i:
                if j is None:
                    __row.append("")
                else:
                    __row.append(self.tp[j])
            tianPanTable.append(__row)

        tianPanTable[1].insert(0, self.tianJiang[tianPanTable[1][0]])
        tianPanTable[1].append(self.tianJiang[tianPanTable[1][-1]])

        tianPanTable[2].insert(0, self.tianJiang[tianPanTable[2][0]])
        tianPanTable[2].append(self.tianJiang[tianPanTable[2][-1]])

        __tmp = []
        for i in tianPanTable[0]:
            __tmp.append(self.tianJiang[i])
        __tmp.insert(0, '')
        __tmp.append('')
        tianPanTable[0].insert(0, '')
        tianPanTable[0].append('')
        tianPanTable.insert(0, __tmp)

        __tmp = []
        for i in tianPanTable[-1]:
            __tmp.append(self.tianJiang[i])
        __tmp.insert(0, '')
        __tmp.append('')
        tianPanTable[-1].insert(0, '')
        tianPanTable[-1].append('')
        tianPanTable.append(__tmp)

        xtianPan = PrettyTable()

        xtianPan.header = False
        xtianPan.padding_width = 0
        xtianPan.border = 0

        for i in tianPanTable:
            xtianPan.add_row(i)

        return [xSanchuan, xsiKe,
                xtianPan]

    def __str__(self):
        # shipanPrint = [str(self.__天盘), str(self.__四课), str(self.__三传)]
        __table = self.table
        __string = ""
        for i in __table:
            __string = "{}\n{}\n".format(__string, i.get_string())
        return __string

    @property
    def toHml(self):
        __table = self.table
        __tableString = ""
        for i in __table:
            __tableString = "{}{}".format(__tableString, i.get_html_string())
        __spTable = '<div style="width:100px">{}</div>'.format(__tableString)
        __head = '''
<head>
    <style>
        table
        {
            width:100%;
            margin:10px;
        }
        td{ width:10px;}
        div{ margin: 10px}
    </style>
</head>'''
        __spHeader = "<div>{}年{}月{}日{}时{}分{}秒</div>".format(self.year,
                                                            self.month,
                                                            self.day,
                                                            self.hour,
                                                            self.minutes,
                                                            self.second)
        __spHeader = "{}<div>占测的事：{}</div>".format(__spHeader, self.占测的事)
        __spHeader = "{}<div>四柱：{} {} {} {}</div><div>{}</div><div>{}</div>".format(
                                                        __spHeader,
                                                        self.四柱与节气[0],
                                                        self.四柱与节气[1],
                                                        self.四柱与节气[2],
                                                        self.四柱与节气[3],
                                                        self.四柱与节气[5],
                                                        self.四柱与节气[6])
        __昼占 = "夜占"
        if self.昼占:
            __昼占 = "昼占"
        __spHeader = ("{}<div>月将：{}&nbsp&nbsp&nbsp月宿：{}&nbsp&nbsp&nbsp占时：{}&nbsp{}&nbsp&nbsp&nbsp"
                      "(空亡: {} {})</div>").format(
            __spHeader,
            self.yueJiang,
            self.moonMansion,
            self.zhanShi,
            __昼占,
            self.空亡[0], self.空亡[1])
        __spHeader = "{} <div>性别：{} 本命：{} 行年：{}</div>".format(
                    __spHeader, "男" if self.性别 == 0 else "女", self.本命, self.行年)
        __格局 = "<div><b>卦体:</b> {}</div>".format(" ".join(self.格局))
        __格局comment = ""
        for i in self.格局comment:
            __格局comment = "{}<div>{}</div>".format(__格局comment, i)
        __html = "<html>{}<body>{}{}{}{}</body></html>".format(__head,
                                                             __spHeader,
                                                             __spTable,
                                                             __格局,
                                                             __格局comment)

        return __html

    def setGuaTi(self, g):
        self.格局.append(g)

    @property
    def 天盘(self):
        return self.tp

    @property
    def 四课(self):
        return self.sk

    @property
    def 三传(self):
        return self.sc

    @property
    def __空亡(self):
        d = []
        gan = self.占日.干
        zhi = self.占日.支
        jia = 干("甲")

        delta = gan - jia

        xunShou = zhi + (-1 * delta)

        return [xunShou + (-2), xunShou + (-1)]

    def __年命(self):
        本命 = GetLi(self.生年, 5, 20, 12, 0, 0)[0]
        if self.性别 == 0:
            行年 = 干支(干("丙"), 支("寅")) + (self.year - self.生年)
        else:
            行年 = 干支(干("壬"), 支("申")) + (self.生年 - self.year)
        return 本命, 行年


class TianPan():
    '''
以寅上支标示天盘，方便__str__输出
a = 天盘(支(2), 支(1))
a[支(4)] 获取巳上神
    '''
    def __init__(self, 月将, 占时):
        if not isinstance(月将, 支):
            raise ValueError("月将需要是地支class")

        if not isinstance(占时, 支):
            raise ValueError("占时需要是地支class")
        self.__天盘 = 月将 + ((占时 - 支("子"))*-1)
        self.__月将 = 月将
        self.__占时 = 占时

    def __str__(self):
        x = PrettyTable()

        x.header = False
        x.padding_width = 0
        x.border = 0

        for i in self.__table:
            x.add_row(i)
        return x.get_string()

    @property
    def __table(self):
        x = []

        line = []
        for i in range(3, 7):
            line.append(self.__天盘 + i)
        x.append(line)

        line = [self.__天盘 + 2, '', '', self.__天盘 + 7]
        x.append(line)

        line = [self.__天盘 + 1, '', '', self.__天盘 + 8]
        x.append(line)

        line = []
        for i in range(9, 13):
            line.append(self.__天盘 + i)
        line.reverse()
        x.append(line)
        return x

    def __getitem__(self, key):
        '''
        用于取得支上神
        '''
        if not isinstance(key, 支):
            raise ValueError('{0} 不是地支'.format(key))

        return self.__天盘 + (key - 支(1))

    def 临(self, key):
        '''地支所临的地盘支'''
        if not isinstance(key, 支):
            raise ValueError('{0} 不是地支'.format(key))

        return self.__占时 + (key - self.__月将)


class SiKe():
    def __init__(self, t, r):
        if not isinstance(t, TianPan):
            raise ValueError("{0} 不是天盘".format(t))
        if not isinstance(r, 干支):
            raise ValueError("{0} 不是干支表示的日".format(t))

        self.__天盘 = t
        self.__日 = r
        self.__干 = self.__日.干
        self.__干阳神 = self.__天盘[寄宫(self.__干)]
        self.__干阴神 = self.__天盘[self.__干阳神]

        self.__支 = self.__日.支
        self.__支阳神 = self.__天盘[self.__支]
        self.__支阴神 = self.__天盘[self.__支阳神]

    @property
    def 干(self):
        return self.__干

    @property
    def 干阳神(self):
        return self.__干阳神

    @property
    def 干阴神(self):
        return self.__干阴神

    @property
    def 支(self):
        return self.__支

    @property
    def 支阳神(self):
        return self.__支阳神

    @property
    def 支阴神(self):
        return self.__支阴神

    @property
    def 一课(self):
        return (self.__干阳神, self.__干)

    @property
    def 二课(self):
        return (self.__干阴神, self.__干阳神)

    @property
    def 三课(self):
        return (self.__支阳神, self.__支)

    @property
    def 四课(self):
        return (self.__支阴神, self.__支阳神)

    def __str__(self):
        x = PrettyTable()

        x.header = False
        x.padding_width = 0
        x.border = 0

        for i in self.__table:
            x.add_row(i)
        return x.get_string()

    @property
    def __table(self):
        x = []
        x.append([self.__支阴神, self.__支阳神, self.__干阴神, self.__干阳神])
        x.append([self.__支阳神, self.__支, self.__干阳神, self.__干])
        return x


class SanChuan():
    bazhuan = (干支(干("甲"), 支("寅")), 干支(干("庚"), 支("申")),
               干支(干("丁"), 支("未")), 干支(干("己"), 支("未")))

    def __init__(self, t, s):
        if not isinstance(t, TianPan):
            raise ValueError("{0} 不是天盘".format(t))
        if not isinstance(s, SiKe):
            raise ValueError("{0} 不是四课".format(s))
        self.__天盘 = t
        self.__四课 = s
        self.__初 = None
        self.__中 = None
        self.__末 = None
        self.__type = []
        self.__初, self.__中, self.__末 = self.__获取三传()

    def __获取三传(self):
        if self.__四课.支阳神 == self.__四课.支:
            return self.__伏呤()
        if self.__四课.支阳神.六冲(self.__四课.支):
            return self.__返呤()
        try:
            return self.__贼克()
        except NoSanchuan as err:
            pass

        try:
            return self.__遥克()
        except NoSanchuan as err:
            pass

        try:
            return self.__昂星()
        except NoSanchuan as err:
            pass
        try:
            return self.__别责()
        except NoSanchuan as err:
            pass
        try:
            return self.__八专()
        except NoSanchuan as err:
            pass

    def __有贼(self):
        ke = []
        __ke = [self.__四课.一课, self.__四课.二课, self.__四课.三课, self.__四课.四课]
        for i in range(0, 4):
            __课 = __ke[i]
            if __课[1].wuxing.克(__课[0].wuxing):
                ke.append(__课)

        if len(ke) == 0:
            return ke
        # 删除重复课
        list_tmp = []
        ke_tmp = []
        for i in ke:
            if i[0] not in list_tmp:
                list_tmp.append(i[0])
                ke_tmp.append(i)
        return ke_tmp

    def __有克(self):
        ke = []
        __ke = [self.__四课.一课, self.__四课.二课, self.__四课.三课, self.__四课.四课]

        for i in range(0, 4):
            __课 = __ke[i]
            if __课[0].wuxing.克(__课[1].wuxing):
                ke.append(__课)
        if len(ke) == 0:
            return ke
        # 删除重复课
        list_tmp = []
        ke_tmp = []
        for i in ke:
            if i[0] not in list_tmp:
                list_tmp.append(i[0])
                ke_tmp.append(i)
        return ke_tmp

    def __贼克(self):
        __贼 = self.__有贼()

        if len(__贼) != 0:
            if len(__贼) == 1:
                __初 = __贼[0][0]
                __中 = self.__天盘[__初]
                __末 = self.__天盘[__中]
                self.__type.append("重审卦")
                return (__初, __中, __末)
            else:
                return self.__比用(__贼)

        __克 = self.__有克()
        if len(__克) != 0:
            if len(__克) == 1:
                __初 = __克[0][0]
                __中 = self.__天盘[__初]
                __末 = self.__天盘[__中]
                self.__type.append("元首卦")
                return (__初, __中, __末)
            else:
                return self.__比用(__克)
        raise NoSanchuan('不能用贼克取三传')

    def __比用(self, ke):
        # le(results) ==1, >1, ==0
        # ke 是一个列表
        result = []
        for i in ke:
            if 阴阳相同(i[0], self.__四课.干):
                result.append(i)
        if len(result) == 1:
            __初 = result[0][0]
            __中 = self.__天盘[__初]
            __末 = self.__天盘[__中]
            self.__type.append("知一卦")
            return (__初, __中, __末)
        elif len(result) == 0:
            return self.__涉害(ke)  # 俱不比
        else:
            return self.__涉害(result)  # 多个俱比

    def __涉害(self, ke):

        '''
        格式
        [
        [[干阳神, 干],2],
        ]
        '''
        __课的涉害深度 = []

        for __ke in ke:
            临地盘 = self.__天盘.临(__ke[0])
            count = 0
            for i in range(0, 12):
                __d = 临地盘 + i
                if __d == __ke[0]:
                    break
                天干List = 干Of寄宫(__d)
                # [干阳， 干 ]
                if __ke[1].wuxing.克(__ke[0].wuxing):
                    '''贼'''
                    if __d.wuxing.克(__ke[0].wuxing):
                        count = count + 1

                    for __g in 天干List:
                        if __g.wuxing.克(__ke[0].wuxing):
                            count = count + 1
                else:
                    if __ke[0].wuxing.克(__d.wuxing):
                        count = count + 1

                    for __g in 天干List:
                        if __ke[0].wuxing.克(__g.wuxing):
                            count = count + 1

            __课的涉害深度.append((__ke, count))

        __最大涉害深度 = 0
        __有最大涉害深度的支组 = []
        for i in __课的涉害深度:
            if i[1] > __最大涉害深度:
                __最大涉害深度 = i[1]
        for i in __课的涉害深度:
            if i[1] == __最大涉害深度:
                __有最大涉害深度的支组.append(i[0])

        if len(__有最大涉害深度的支组) == 1:
            __初 = __有最大涉害深度的支组[0][0]
            __中 = self.__天盘[__初]
            __末 = self.__天盘[__中]
            self.__type.append("涉害卦")
            return (__初, __中, __末)

        # 涉害深度相同
        for i in __有最大涉害深度的支组:
            临地盘 = self.__天盘.临(i[0])

            # 从孟发用
            if 临地盘 in [支("寅"), 支("巳"), 支("申"), 支("亥")]:
                __初 = i[0]
                __中 = self.__天盘[__初]
                __末 = self.__天盘[__中]
                self.__type.append("见机")
                return (__初, __中, __末)

        # 从仲发用
        for i in __有最大涉害深度的支组:
            临地盘 = self.__天盘.临(i[0])
            if 临地盘 in [支("子"), 支("卯"), 支("午"), 支("酉")]:
                __初 = i[0]
                __中 = self.__天盘[__初]
                __末 = self.__天盘[__中]
                self.__type.append("察微")
                return (__初, __中, __末)

        if self.__四课.干.属阳:
            __初 = self.__四课.干阳神
            __中 = self.__天盘[__初]
            __末 = self.__天盘[__中]
            self.__type.append("复等")
            return (__初, __中, __末)
        else:
            __初 = self.__四课.支阳神
            __中 = self.__天盘[__初]
            __末 = self.__天盘[__中]
            self.__type.append("复等")
            return (__初, __中, __末)

        # 俱是季
        raise NoSanchuan('所临皆四季，不能用涉害取三传')

    def __遥克(self):
        if 干支(self.__四课.干, self.__四课.支) in self.bazhuan:
            raise NoSanchuan('八传日不用遥克')
        ko = []
        if self.__四课.二课[0].wuxing.克(self.__四课.干.wuxing):
            ko.append(self.__四课.二课)
        if self.__四课.三课[0].wuxing.克(self.__四课.干.wuxing):
            ko.append(self.__四课.三课)
        if self.__四课.四课[0].wuxing.克(self.__四课.干.wuxing):
            ko.append(self.__四课.四课)

        if len(ko) == 0:
            if self.__四课.干.wuxing.克(self.__四课.二课[0].wuxing):
                ko.append(self.__四课.二课)
            if self.__四课.干.wuxing.克(self.__四课.三课[0].wuxing):
                ko.append(self.__四课.三课)
            if self.__四课.干.wuxing.克(self.__四课.四课[0].wuxing):
                ko.append(self.__四课.四课)
        if len(ko) == 0:
            raise NoSanchuan('无遥克，不能用遥克取三传')

        # 删除重复课
        list_tmp = []
        ko_tmp = []
        for i in ko:
            if i[0] not in list_tmp:
                list_tmp.append(i[0])
                ko_tmp.append(i)
        ko = ko_tmp
        if len(ko) == 1:
            __初 = ko[0][0]
            __中 = self.__天盘[__初]
            __末 = self.__天盘[__中]
            self.__type.append("遥克卦")
            return (__初, __中, __末)
        else:
            if len(ko) > 1:
                self.__type.append("遥克卦")
            return self.__比用(ko)

    def __昂星(self):
        ko = []
        list_tmp = []
        for i in (self.__四课.一课, self.__四课.二课, self.__四课.三课, self.__四课.四课):
            if i[0] not in list_tmp:
                list_tmp.append(i[0])
                ko.append(i)
        if len(ko) != 4:
            raise NoSanchuan('课不备，不能用昂星取三传')
        if self.__四课.干.属阳:
            chu = self.__天盘[支("酉")]
            zhong = self.__四课.支阳神
            mo = self.__四课.干阳神
            self.__type.append("虎视")
            return (chu, zhong, mo)
        else:
            chu = self.__天盘.临(支("酉"))
            zhong = self.__四课.干阳神
            mo = self.__四课.支阳神
            self.__type.append("冬蛇掩目")
            return (chu, zhong, mo)

    def __别责(self):
        ko = []
        list_tmp = []
        for i in (self.__四课.一课, self.__四课.二课, self.__四课.三课, self.__四课.四课):
            if i[0] not in list_tmp:
                list_tmp.append(i[0])
                ko.append(i)
        if len(ko) == 4:
            raise NoSanchuan('四课全备，不能用别责取三传')
        if len(ko) != 3:
            raise NoSanchuan('用别责用于三课备取三传')
        if self.__四课.干.属阳:
            chu = self.__天盘[寄宫(self.__四课.干 + 5)]
        else:
            chu = self.__四课.支 + 4
        zhong = self.__四课.干阳神
        mo = zhong
        self.__type.append("别责卦")
        return (chu, zhong, mo)

    def __八专(self):
        if 干支(self.__四课.干, self.__四课.支) not in self.bazhuan:
            raise NoSanchuan('不是八传日')
        if self.__四课.干.属阳:
            chu = self.__四课.干阳神 + 2
            self.__type.append("八专卦")
            return (chu, self.__四课.干阳神, self.__四课.干阳神)
        else:
            chu = self.__四课.支阴神 + (-2)
            self.__type.append("八专卦")
            return (chu, self.__四课.干阳神, self.__四课.干阳神)

    def __伏呤(self):
        # 六乙、六癸日
        if self.__四课.干 in (干("乙"), 干("癸")) or self.__四课.干.属阳:
            chu = self.__四课.干阳神
        else:
            # 阴日，非六乙日、六癸
            chu = self.__四课.支阳神
        for i in range(1, 13):
            if chu.刑(支(i)):
                zhong = 支(i)
                break

        # 初为自刑，阳日、六乙日、六癸日取支上神为中传
        if chu == zhong:
            if self.__四课.干 in (干("乙"), 干("癸")) or self.__四课.干.属阳:
                zhong = self.__四课.支阳神
            else:
                zhong = self.__四课.干阳神

        for i in range(1, 13):
            if zhong.刑(支(i)):
                mo = 支(i)
                break
        # 中传自刑，取中所冲之神
        if zhong == mo:
            mo = zhong + 6
        # 初、中互刑，如：子、卯，末取中所冲之神
        if zhong.刑(chu):
            mo = zhong + 6
        if self.__四课.干.属阳:
            self.__type.append("自任卦")
        else:
            self.__type.append("自信卦")
        return (chu, zhong, mo)

    def __返呤(self):
        try:
            return self.__贼克()
        except NoSanchuan as err:
            # 驿马计算
            zhi = self.__四课.支
            for i in range(0, 3):
                if zhi in [支("寅"), 支("巳"), 支("申"), 支("亥")]:
                    yiMa = zhi + 6
                    break
                zhi = zhi + 4
            chu = yiMa
            zhong = self.__四课.支阳神
            mo = self.__四课.干阳神
            self.__type.append("无依卦")
            return (chu, zhong, mo)

    def __str__(self):

        x = PrettyTable()

        x.header = False
        x.padding_width = 0
        x.border = 0

        for i in self.__table:
            x.add_row(i)
        return x.get_string()

    @property
    def __table(self):
        d = self.遁干
        x = []

        x.append(['', d[0], self.__初, ''])
        x.append(['', d[1], self.__中, ''])
        x.append(['', d[2], self.__末, ''])

        return x

    @property
    def 初(self):
        return self.__初

    @property
    def 中(self):
        return self.__中

    @property
    def 末(self):
        return self.__末

    @property
    def 遁干(self):
        d = []
        gan = self.__四课.干
        zhi = self.__四课.支
        jia = 干("甲")

        delta = gan - jia

        xunShou = zhi + (-1 * delta)

        for i in (self.初, self.中, self.末):
            zhiDelta = (i - xunShou + 12) % 12
            if zhiDelta == 10 or zhiDelta == 11:
                d.append('')
            else:
                d.append(jia + zhiDelta)
        return d

    @property
    def 六亲(self):
        luQing = []
        gan = self.__四课.干
        sc = [self.初, self.中, self.末]
        for i in sc:
            if gan.wuxing.克(i.wuxing):
                luQing.append("财")
            elif i.wuxing.克(gan.wuxing):
                luQing.append("官")
            elif gan.wuxing.生(i.wuxing):
                luQing.append("子")
            elif i.wuxing.生(gan.wuxing):
                luQing.append("父")
            else:
                luQing.append("兄")
        return luQing

    @property
    def 格局(self):
        return self.__type

    def __eq__(self, other):
        if not isinstance(other, SanChuan):
            raise ValueError('{0}不是三传'.format(other))
        return self.__初 == other.初 \
            and self.__中 == other.中 \
            and self.__末 == other.末

    def __nq__(self, other):
        if not isinstance(other, SanChuan):
            raise ValueError('{0}不是三传'.format(other))
        return not self.__eq__(other)


class 天将(Base):
    numToName = ['贵', '蛇', '雀', '合', '勾', '龙', '空', '虎', '常', '玄', '阴', '后']

    def __init__(self, num):
        if isinstance(num, int) and (num > 0 or num < 13):
            n = num
        elif isinstance(num, str) and (num in self.numToName):
            n = self.numToName.index(num) + 1
        else:
            raise ValueError('输入的值为%s，输入值必是大于等于1小于等于12间的整数' % num)
        super().__init__(n)

    @property
    def 吉将(self):
        return self.num in [1, 4, 6, 9, 11, 12]

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError('%s 必须是整数' % other)
        tmp = (self.num + other + 12) % 12
        tmp = 12 if tmp == 0 else tmp
        return 天将(tmp)

    def __sub__(self, other):
        if not isinstance(other, 天将):
            raise ValueError('%s 必须是天将' % other)
        return self.num - other.num

    def __eq__(self, other):
        if not isinstance(other, 天将):
            raise ValueError('%s 必须是天将' % other)
        return self.num == other.num


class 天将盘():
    zhouGui = {"甲": 支("未"),
               "乙": 支("申"),
               "丙": 支("酉"),
               "丁": 支("亥"),
               "戊": 支("丑"),
               "己": 支("子"),
               "庚": 支("丑"),
               "辛": 支("寅"),
               "壬": 支("卯"),
               "癸": 支("巳")}
    yeGui = {"甲": 支("丑"),
             "乙": 支("子"),
             "丙": 支("亥"),
             "丁": 支("酉"),
             "戊": 支("未"),
             "己": 支("申"),
             "庚": 支("未"),
             "辛": 支("午"),
             "壬": 支("巳"),
             "癸": 支("卯")}

    def __init__(self, t, s, 昼占=True):
        if not isinstance(t, TianPan):
            raise ValueError("{0} 不是天盘".format(t))
        if not isinstance(s, SiKe):
            raise ValueError("{0} 不是四课".format(s))
        self.__天盘 = t
        self.__四课 = s
        self.__gan = self.__四课.干
        self.__guiren = None  # 贵人所乘地支
        self.__mi = False  # 天将逆布

        if 昼占:
            self.__guiren = self.zhouGui[str(self.__gan)]
        else:
            self.__guiren = self.yeGui[str(self.__gan)]

        guiRenDiPan = 支("子") + (self.__guiren - self.__天盘[支("子")])  # 贵人地盘之支

        si = 支("巳")
        xu = 支("戌")
        if guiRenDiPan - si >= 0 and xu - guiRenDiPan >= 0:
            self.__mi = True

    @property
    def 逆(self):
        return self.__mi

    def __getitem__(self, key):
        '''
        获取某地支的天将
        '''
        if not isinstance(key, 支):
            raise ValueError('只有支才有天将')
        if self.逆:
            return 天将("贵") + (self.__guiren - key)
        else:
            return 天将("贵") + (key - self.__guiren)

    def 临(self, tj):
        if not isinstance(tj, 天将):
            raise ValueError('只有天将才有所临地支')
        if self.逆:
            return self.__guiren + (天将("贵") - tj)
        else:
            return self.__guiren + (tj - 天将("贵"))


class MinGPan(ShiPan):
    def __init__(self, year, month, day, hour, minutes,
                 second, 月将, 占时, 昼占=True, 占测的事="", 性别=0, 生年=2018):
        super().__init__(year, month, day, hour, minutes,
                         second, 月将, 占时, 昼占, 占测的事, 性别=0, 生年=2018)
        self.命宫 = self.四柱与节气[0].支
        self.三限 = self.__三限
        self.大运流年 = self.__大运流年()
#         print(self.三限)

    @property
    def __三限(self):
        __sx = []
        __sc = (self.sc.初, self.sc.中, self.sc.末)
        for i in range(0, 3):
            __临 = self.tp[__sc[i]]
            __sx.append((__临.太玄数 * __sc[i].太玄数) / 2 + __临.太玄数)
        return __sx

    def __大运流年(self):
        __dL = [self.命宫.太玄数]
        for i in range(1, 12):
            __dL.append(__dL[-1] + (self.命宫 + (-1 * i)).太玄数)

#         __流年积数 = 0
        __daYun = []
        for i in range(0, len(__dL)):
            __第一年Num = self.year + __dL[i] - 1
            __第一年干支 = self.四柱与节气[0] + (__dL[i] - 1)
            __流年List = []
            for j in range(0, (self.命宫 + (-1 * i - 1)).太玄数):
                __流年List.append([__第一年Num + j, __第一年干支 + j])
            __daYun.append({"xian": __dL[i], "liunian": __流年List})
        return __daYun

    def __str__(self):
        __pan = super().__str__()

        x = PrettyTable()

        x.header = False
        x.padding_width = 0
        x.border = 0

        x.add_row(["命宫", "财帛", "兄弟", "田宅", "男女", "奴仆", "夫妻",
                  "疾厄", "迁移", "官禄", "福德", "相貌"])

        __daYun = []
        for i in range(0, 12):
            __daYun.append(self.命宫 + (-1 * i))
        x.add_row(__daYun)
        xian = []
        for i in self.大运流年:
            xian.append(i["xian"])
        x.add_row(xian)

        liuNian = []
        for i in self.大运流年:
            __tmp = ""
            for j in i["liunian"]:
                __tmp = "{}\n{}{}".format(__tmp, j[0], j[1])
            liuNian.append(__tmp)
        x.add_row(liuNian)

        return "{}\n{}".format(__pan, x.get_string())

    @property
    def toHml(self):
        __html = super().toHml

        x = PrettyTable()

        x.header = False
        x.padding_width = 0
        x.border = 0

        x.add_row(["命宫", "财帛", "兄弟", "田宅", "男女", "奴仆", "夫妻",
                  "疾厄", "迁移", "官禄", "福德", "相貌"])

        __daYun = []
        for i in range(0, 12):
            __daYun.append(self.命宫 + (-1 * i))
        x.add_row(__daYun)
        xian = []
        for i in self.大运流年:
            xian.append(i["xian"])
        x.add_row(xian)

        liuNian = []
        for i in self.大运流年:
            __tmp = ""
            for j in i["liunian"]:
                __tmp = "{}\n{}{}".format(__tmp, j[0], j[1])
            liuNian.append(__tmp)
        x.add_row(liuNian)
        liuNianTable = x.get_html_string()
        liuNianTable = regex.sub(r'<tr>', '<tr valign="top">', liuNianTable)
        __三限html = "<div>三限：<div>初限：{0[0]}</div><div>中限：{0[1]}</div><div>末限：{0[2]}</div></div>".format(self.__三限)
        html = regex.sub(r'</body></html>', __三限html + liuNianTable, __html)
        return "{}</body></html>".format(html)


if __name__ == "__main__":
#     a = MinGPan(2018, 6, 15,13, 22, 7, "申", "未", True, "abc")
    a = ShiPan(2018, 8, 29,13, 22, 7, "巳", "酉", True, "abc",0,2018)
    print(a.toHml)