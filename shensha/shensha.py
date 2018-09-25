from ganzhiwuxin import 干, 支


def do_驿马(sp, shenShaJson):
    sk = sp.四课
    __支 = sk.支
    __月建 = sp.四柱与节气[1].支
    zhi = __月建
    for i in range(0, 3):
        if zhi in [支("寅"), 支("巳"), 支("申"), 支("亥")]:
            yiMa = zhi + 6
            break
        zhi = zhi + 4
    shenShaJson["月"]["驿马"] = yiMa

    zhi = __支
    for i in range(0, 3):
        if zhi in [支("寅"), 支("巳"), 支("申"), 支("亥")]:
            yiMa = zhi + 6
            break
        zhi = zhi + 4
    shenShaJson["日"]["驿马"] = yiMa

    __岁 = sp.四柱与节气[0].支
    zhi = __岁
    for i in range(0, 3):
        if zhi in [支("寅"), 支("巳"), 支("申"), 支("亥")]:
            yi_ma = zhi + 6
            break
        zhi = zhi + 4
    shenShaJson["年"]["驿马"] = yi_ma


def do_月合(sp, shenShaJson):
    pass


def do_天印(sp, shenShaJson):
    pass


def do_成神(sp, shenShaJson):
    pass


def do_皇书(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    if __月建 in [支("寅"), 支("卯"), 支("辰")]:
        shenShaJson["月"]["皇书"] = 支("寅")
        return
    if __月建 in [支("巳"), 支("午"), 支("未")]:
        shenShaJson["月"]["皇书"] = 支("巳")
        return
    if __月建 in [支("申"), 支("酉"), 支("戌")]:
        shenShaJson["月"]["皇书"] = 支("申")
        return
    shenShaJson["月"]["皇书"] = 支("亥")


def do_皇恩(sp, shenShaJson):
    寅 = 支("寅")
    __月建 = sp.四柱与节气[1].支
    he = 支("未") + (__月建 - 寅) * 2
    shenShaJson["月"]["皇恩"] = he


def do_天诏飞魂(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    he = __月建 + (-3)
    shenShaJson["月"]["天诏"] = he
    shenShaJson["月"]["飞魂"] = he


def do_福星(sp, shenShaJson):
    pass


def do_天喜(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    if __月建 in [支("寅"), 支("卯"), 支("辰")]:
        shenShaJson["月"]["天喜"] = 支("戌")
        return
    if __月建 in [支("巳"), 支("午"), 支("未")]:
        shenShaJson["月"]["天喜"] = 支("丑")
        return
    if __月建 in [支("申"), 支("酉"), 支("戌")]:
        shenShaJson["月"]["天喜"] = 支("辰")
        return
    shenShaJson["月"]["天喜"] = 支("未")


def do_天赦(sp, shenShaJson):
    pass


def do_生气(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    shenShaJson["月"]["生气"] = __月建 + (-2)


def do_天马(sp, shenShaJson):
    寅 = 支("寅")
    __月建 = sp.四柱与节气[1].支
    he = 支("午") + (__月建 - 寅) * 2
    shenShaJson["月"]["天马"] = he


def do_三丘五墓(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    zhi = __月建
    for i in range(0, 3):
        if zhi in [支("寅"), 支("巳"), 支("申"), 支("亥")]:
            三丘 = zhi + (-1)
            break
        zhi = zhi + (-1)
    shenShaJson["月"]["三丘"] = 三丘
    shenShaJson["月"]["五墓"] = 三丘 + 6


def do_死气(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    s = __月建 + 4
    shenShaJson["月"]["死气"] = s
    shenShaJson["月"]["谩语"] = s


def do_孤辰寡宿(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    zhi = __月建
    for i in range(0, 3):
        if zhi in [支("寅"), 支("巳"), 支("申"), 支("亥")]:
            寡宿 = zhi + (-1)
            break
        zhi = zhi + (-1)
    shenShaJson["月"]["寡宿"] = 寡宿
    shenShaJson["月"]["孤辰"] = 寡宿 + 4


def do_四废(sp, shenShaJson):
    pass


def do_天医地医(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    天医 = __月建 + 2
    地医 = 天医 + 6
    shenShaJson["月"]["天医"] = 天医
    shenShaJson["月"]["地医"] = 地医
    shenShaJson["月"]["天巫"] = 天医
    shenShaJson["月"]["地巫"] = 地医


def do_金神(sp, shenShaJson):
    pass


def do_破碎(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    if (__月建 - 支("寅")) % 3 == 0:
        shenShaJson["月"]["破碎"] = 支("酉")
        return
    if (__月建 - 支("卯")) % 3 == 0:
        shenShaJson["月"]["破碎"] = 支("巳")
        return
    if (__月建 - 支("辰")) % 3 == 0:
        shenShaJson["月"]["破碎"] = 支("丑")


def do_月厌(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    月厌 = 支("子") + (支("子") - __月建)
    shenShaJson["月"]["月厌"] = 月厌


def do_劫杀(sp, shenShaJson):
    pass


def do_大耗小耗(sp, shenShaJson):
    __岁 = sp.四柱与节气[0].支
    shenShaJson["年"]["大耗"] = __岁 + 6
    shenShaJson["年"]["小耗"] = __岁 + 5


def do_病符(sp, shenShaJson):
    __岁 = sp.四柱与节气[0].支
    shenShaJson["年"]["病符"] = __岁 + (-1)


def do_血支血忌(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    shenShaJson["月"]["血支"] = __月建 + (-1)
    if (__月建 - 支("寅")) % 2 == 0:
        shenShaJson["月"]["血忌"] = 支("丑") + (__月建 - 支("寅")) // 2
    else:
        shenShaJson["月"]["血忌"] = 支("未") + (__月建 - 支("卯")) // 2


def do_大煞小煞(sp, shenShaJson):
    pass


def do_丧车(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    n = (__月建 - 支("寅") + 12) % 12
    n = n // 3
    s = [支("酉"), 支("子"), 支("卯"), 支("午")]
    shenShaJson["月"]["丧车"] = s[n]


def do_游都(sp, shenShaJson):
    # TODO
    return


def do_奸神(sp, shenShaJson):
# TODO
    return

def do_奸私(sp, shenShaJson):
# TODO
    return


def do_信神天鸡(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    shenShaJson["月"]["信神"] = 支("酉") + (__月建 - 支("寅"))
    shenShaJson["月"]["天鸡"] = 支("酉") + (支("寅") - __月建)


def do_丧魂(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    zhi = __月建
    for i in range(0, 3):
        if zhi in [支("寅"), 支("巳"), 支("申"), 支("亥")]:
            __丧魂 = zhi + 5
            break
        zhi = zhi + 4
    shenShaJson["月"]["丧魂"] = __丧魂


def do_天鬼(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    zhi = __月建
    for i in range(0, 3):
        if zhi in [支("寅"), 支("巳"), 支("申"), 支("亥")]:
            __天鬼 = zhi + 7
            break
        zhi = zhi + 4
    shenShaJson["月"]["天鬼"] = __天鬼


def do_桃花绳索(sp, shenShaJson):
    # TODO
    return

def do_大时(sp, shenShaJson):
    __月建 = sp.四柱与节气[1].支
    zhi = __月建
    for i in range(0, 3):
        if zhi in [支("子"), 支("卯"), 支("午"), 支("酉")]:
            __大时 = zhi +(-3)
            break
        zhi = zhi + 4
    shenShaJson["月"]["大时"] = __大时

def do_小时(sp, shenShaJson):
    shenShaJson["月"]["小时"] = sp.四柱与节气[1].支

def do__旬奇(sp, shenShaJson):
    __kw = sp.空亡
    __xs = __kw[1] + 1
    if __xs in [支("戌"), 支("子")]:
        旬奇 = 支("丑")
    if __xs in [支("申"), 支("午")]:
        旬奇 = 支("子")
    if __xs in [支("寅"), 支("辰")]:
        旬奇 = 支("亥")
    shenShaJson["日"]["旬奇"] = 旬奇


def do__日奇(sp, shenShaJson):
    sk = sp.四课
    __g = sk.干
    d = __g - 干("甲")
    if d <= 5:
        日奇 = 支("午") + (-1 * d)
    else:
        日奇 = 支("未") + (__g - 干("庚"))
    shenShaJson["日"]["日奇"] = 日奇


def do__旬仪(sp, shenShaJson):
    __kw = sp.空亡
    __xs = __kw[1] + 1
    shenShaJson["日"]["旬仪"] = __xs


def do__支仪(sp, shenShaJson):
    sk = sp.四课
    __g = sk.支
    d = __g - 支("子")
    if d <= 5:
        日奇 = 支("午") + (-1 * d)
    else:
        日奇 = 支("未") + (__g - 支("午"))
    shenShaJson["日"]["支仪"] = 日奇
