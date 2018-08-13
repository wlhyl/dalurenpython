from shipan import shipan
from common import Get旺衰, 旺衰

def do_伏呤(sp):
    sk = sp.四课
    __支 = sk.支
    __支阳 = sk.支阳神
    if __支 == __支阳:
        sp.setGuaTi("伏呤卦")


def do_返呤(sp):
    sk = sp.四课
    __支 = sk.支
    __支阳 = sk.支阳神
    if (__支 + 6) == __支阳:
        sp.setGuaTi("返呤卦")


def do_龙德(sp):
    __太岁 = sp.四柱与节气[0]
    __月将 = sp.yueJiang
    __三传 = sp.三传
    sc = [__三传.初, __三传.中, __三传.末]
    if sc[0] == __月将 and __太岁.支 in sc:
        print(1)
        sp.setGuaTi("龙德卦")


def do_三光(sp):
    pass


def do_三阳(sp):
    __发用 = sp.三传.初
    __月建 = sp.四柱与节气[1].支
    if Get旺衰(__月建, __发用.wuxing) not in [旺衰("旺"), 旺衰("相")]:
        return
    天将盘 = sp.tianJiang
    if 天将盘.逆:
        return
    sk = sp.四课
    __干 = sk.干
    __支 = sk.支
    __干天将 = 天将盘[shipan.寄宫(__干)]
    __支天将 = 天将盘[__支]
    t = [shipan.天将('蛇'), shipan.天将('雀'), shipan.天将('合'), shipan.天将('勾'),
         shipan.天将('龙')]
    if __干天将 in t and __支天将 in t:
        sp.setGuaTi("三阳卦")


def do_度厄(sp):
    sk = sp.四课
    __四课 = [sk.一课, sk.二课, sk.三课, sk.四课]
    z = 0
    y = 0
    for i in range(0, 4):
        if __四课[i][0].wuxing.克(__四课[i][1].wuxing):
            z = z + 1
        if __四课[i][1].wuxing.克(__四课[i][0].wuxing):
            y = y + 1
    if z == 3 or y == 3:
        sp.setGuaTi("度厄卦")


def do_无禄绝嗣(sp):
    sk = sp.四课
    __干 = sk.干
    __干阳神 = sk.干阳神
    __干阴神 = sk.干阴神
    __支 = sk.支
    __支阳神 = sk.支阳神
    __支阴神 = sk.支阴神
    if __干阳神.wuxing.克(__干.wuxing) and __干阴神.克(__干阳神) and __支阳神.克(__支) and \
            __支阴神.克(__支阳神):
        sp.setGuaTi("无禄绝嗣卦")
        return
    if __干.wuxing.克(__干阳神.wuxing) and __干阳神.克(__干阴神) and __支.克(__支阳神) and \
            __支阳神.克(__支阴神):
        sp.setGuaTi("无禄绝嗣卦")
        return


def do_罗网(sp):
    sc = sp.三传
    sk = sp.四课
    tp = sp.天盘
    __chu = sc.末
    __行年上神 = tp[sp.行年.支]
    __本命上神 = tp[sp.本命.支]

    __干上神 = sk.干阳神
    __支上神 = sk.支阳神

    zhiList = [__干上神, __支上神, __chu, __行年上神, __本命上神]
    天罗 = shipan.寄宫(sk.干) + 1
    地网 = 天罗 + 6

    if 天罗 in zhiList or 地网 in zhiList:
        sp.setGuaTi("罗网卦")

if __name__ == "__main__":
    shipan.ShiPan(2018, 4, 3, 11, 11,11, "戌","酉",yes, "占测的事")