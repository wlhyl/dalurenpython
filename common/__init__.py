import os
import datetime
import eacal
from ganzhiwuxin import *

DB = os.path.dirname(os.path.realpath(__file__)) + '/data/lifa.db'
DiZHiList = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]


def GetShiChen(h):
    '''
    int((h+1)/2)+1 可以得到时辰数
    当h=23，得到13,即第二日子时
    '''
    s = (h + 1) // 2 + 1
    if s == 13:
        s = 1
    return 支(s)


# 取得占日的历法数据
# 返回 四柱 月将
def GetLi(y, m, d, h, minu, sec):
    timeString = "{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}".format(
        y, m, d, h, minu, sec)

    占时Time = datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S")
    前一节Time = None
    前一节Num = None
    后一节Time = None
    后一节Num = None
    c = eacal.EACal(zh_s=True)
    for x in c.get_annual_solar_terms(y):
        if x[1] % 2 == 0:
            前一节Time = 后一节Time
            后一节Time = x[2].replace(tzinfo=None)
            前一节Num = 后一节Num
            后一节Num = x[1]
        if 前一节Time is not None and 后一节Time is not None:
            if 占时Time >= 前一节Time and 占时Time <= 后一节Time:
                break
    气List = c.get_specified_solar_term(y, 前一节Num + 1)
    气Time = 气List[2].replace(tzinfo=None)

    气 = "{} {}".format(气List[0],
                       datetime.datetime.strftime(气List[2],
                                                  "%Y-%m-%d %H:%M:%S"))
#     气 = "{} {}".format(气List[0], 气List[2].replace(tzinfo=None))
    节 = c.get_specified_solar_term(y, 前一节Num)[0]
    节 = "{} {}".format(节, datetime.datetime.strftime(前一节Time,
                                                     "%Y-%m-%d %H:%M:%S"))

    __年干支, __月干支, __日干支 = c.get_cycle_ymd(datetime.datetime(y, m, d))
    年柱 = 干支(干(__年干支[0]), 支(__年干支[1]))
    月柱 = 干支(干(__月干支[0]), 支(__月干支[1]))
    日柱 = 干支(干(__日干支[0]), 支(__日干支[1]))

    for i in ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]:
        if 月柱.支.六合(支(i)):
            月将=支(i)
            break
    if 占时Time < 气Time:
        月将=月将 + 1

    时辰 = GetShiChen(h)
    if 日柱.干 == 干("甲") or 日柱.干 == 干("己"):
        子时天干 = 干("甲")
    if 日柱.干 == 干("乙") or 日柱.干 == 干("庚"):
        子时天干 = 干("丙")
    if 日柱.干 == 干("丙") or 日柱.干 == 干("辛"):
        子时天干 = 干("戊")
    if 日柱.干 == 干("丁") or 日柱.干 == 干("壬"):
        子时天干 = 干("庚")
    if 日柱.干 == 干("戊") or 日柱.干 == 干("癸"):
        子时天干 = 干("壬")
    时柱 = 干支(子时天干 + (时辰 - 支('子')), 时辰)
    if 时辰 == 支("子"):
        日柱 = 日柱 + 1
    return [年柱, 月柱, 日柱, 时柱, 月将, 节, 气]


class 旺衰():
    def __init__(self, w):
        self.ws = ["旺", "相", "休", "囚", "死"]
        if w not in self.ws:
            raise ValueError('{} 值错误'.format(w))
        self.__n = self.ws.index(w)

    @property
    def num(self):
        return self.__n

    def __str__(self):
        return self.ws[self.__n]

    def __eq__(self, other):
        if not isinstance(other, 旺衰):
            raise ValueError('{} 不是旺衰'.format(other))
        return self.num == other.num


def Get旺衰(yl, wx):
    if not isinstance(yl, 支):
            raise ValueError('{} 不是支'.format(yl))
    if not isinstance(wx, 五行):
            raise ValueError('{} 不是五行'.format(yl))
    if yl.wuxing.生(wx):
        return 旺衰("相")
    if yl.wuxing.克(wx):
        return 旺衰("死")
    if wx.生(yl.wuxing):
        return 旺衰("休")
    if wx.克(yl.wuxing):
        return 旺衰("囚")
    return 旺衰("旺")


if __name__ == "__main__":
    w = 五行("水")
    for i in range(1, 13):
        z = 支(i)
        print("{} {} {}".format(w, Get旺衰(z, w), z))
    # for i in range(0,24):
    #     print("{}  {}".format(i,GetShiChen(i)))
#     a=GetLi(2018, 8, 13, 23, 23, 22)
#     for i in a:
#         print(i)
