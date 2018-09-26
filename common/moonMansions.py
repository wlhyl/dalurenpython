import datetime
import math
from ganzhiwuxin.ganzhiwuxin import 支
from dalurenCalendar.lunar.elp82 import GetMoonEclipticLongitudeEC
from dalurenCalendar.util.julianday import GetJulianDayFromDateTime


def getMoonMansion(y, m, d, h, minu, sec):
    t = datetime.datetime(y, m, d, h, minu, sec)
    t -= datetime.timedelta(hours=8)
    jd = GetJulianDayFromDateTime(t)
    longitude = GetMoonEclipticLongitudeEC(jd)
    longitude = math.degrees(longitude)
    DEGREES = 30
    if longitude < DEGREES:
        return 支("戌")
    if longitude < DEGREES*2:
        return 支("酉")
    if longitude < DEGREES*3:
        return 支("申")
    if longitude < DEGREES*4:
        return 支("未")
    if longitude < DEGREES*5:
        return 支("午")
    if longitude < DEGREES*6:
        return 支("巳")
    if longitude < DEGREES*7:
        return 支("辰")
    if longitude < DEGREES*8:
        return 支("卯")
    if longitude < DEGREES*9:
        return 支("寅")
    if longitude < DEGREES*10:
        return 支("丑")
    if longitude < DEGREES*11:
        return 支("子")
    return 支("亥")