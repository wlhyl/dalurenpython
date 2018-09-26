from astropy.time import Time
from dalurenCalendar.util import GetDeltaT

# GetJulianDayFromDateTime 将 datetime.datetime 转换为儒略日
# 其中包含了 UTC 到 TT 的转换
# 传入参数为UTC时间
# 返回力学时的儒略日，浮点数
def GetJulianDayFromDateTime(t):
    # t=datetime.datetime(2018,9,26,12,0,0)
    jd=Time(t).jd
    yy = t.year
    mm = t.month
    # yy, mm, dd = GetDateFromJulianDay(jd)
    # UTC -> TT
    jd += GetDeltaT(yy, mm) / 86400
    return jd
