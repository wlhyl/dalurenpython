J2000 = 2451545.0

# // GetJulianCentury 计算儒略世纪数
def GetJulianCentury(jd):
    #  100年的日数
    DaysOfCentury = 36525.0
    return (jd - J2000) / DaysOfCentury


# GetDeltaT 计算地球时和UTC的时差，算法摘自
# http://eclipse.gsfc.nasa.gov/SEhelp/deltatpoly2004.html NASA网站
# ∆T = TT - UT 此算法在-1999年到3000年有效
# 传入参数为整数
# 返回浮点数
def  GetDeltaT(year, month):
    y = year + (month-0.5)/12
    if year < -500:
        u = (year - 1820) / 100
        return -20 + 32*u*u

    if year < 500:
        u = y / 100
        u2 = u * u
        u3 = u2 * u
        u4 = u3 * u
        u5 = u4 * u
        u6 = u5 * u
        return 10583.6 - 1014.41*u + 33.78311*u2 - 5.952053*u3 - 0.1798452*u4 + 0.022174192*u5 + 0.0090316521*u6

    if year < 1600:
        u = (y - 1000) / 100
        u2 = u * u
        u3 = u2 * u
        u4 = u3 * u
        u5 = u4 * u
        u6 = u5 * u
        return 1574.2 - 556.01*u + 71.23472*u2 + 0.319781*u3 - 0.8503463*u4 - 0.005050998*u5 + 0.0083572073*u6

    if year < 1700:
        t = y - 1600
        t2 = t * t
        t3 = t2 * t
        return 120 - 0.9808*t - 0.01532*t2 + t3/7129

    if year < 1800:
        t = y - 1700
        t2 = t * t
        t3 = t2 * t
        t4 = t3 * t
        return 8.83 + 0.1603*t - 0.0059285*t2 + 0.00013336*t3 - t4/1174000

    if year < 1860:
        t = y - 1800
        t2 = t * t
        t3 = t2 * t
        t4 = t3 * t
        t5 = t4 * t
        t6 = t5 * t
        t7 = t6 * t
        return 13.72 - 0.332447*t + 0.0068612*t2 + 0.0041116*t3 - 0.00037436*t4 + 0.0000121272*t5 - 0.0000001699*t6 + 0.000000000875*t7

    if year < 1900:
        t = y - 1860
        t2 = t * t
        t3 = t2 * t
        t4 = t3 * t
        t5 = t4 * t
        return 7.62 + 0.5737*t - 0.251754*t2 + 0.01680668*t3 - 0.0004473624*t4 + t5/233174

    if year < 1920:
        t = y - 1900
        t2 = t * t
        t3 = t2 * t
        t4 = t3 * t
        return -2.79 + 1.494119*t - 0.0598939*t2 + 0.0061966*t3 - 0.000197*t4

    if year < 1941:
        t = y - 1920
        t2 = t * t
        t3 = t2 * t
        return 21.20 + 0.84493*t - 0.076100*t2 + 0.0020936*t3

    if year < 1961:
        t = y - 1950
        t2 = t * t
        t3 = t2 * t
        return 29.07 + 0.407*t - t2/233 + t3/2547

    if year < 1986:
        t = y - 1975
        t2 = t * t
        t3 = t2 * t
        return 45.45 + 1.067*t - t2/260 - t3/718

    if year < 2005:
        t = y - 2000
        t2 = t * t
        t3 = t2 * t
        t4 = t3 * t
        t5 = t4 * t
        return 63.86 + 0.3345*t - 0.060374*t2 + 0.0017275*t3 + 0.000651814*t4 + 0.00002373599*t5

    if year < 2050:
        t = y - 2000
        t2 = t * t
        return 62.92 + 0.32217*t + 0.005589*t2

    if year < 2150:
        u = (y - 1820) / 100
        u2 = u * u
        return -20 + 32*u2 - 0.5628*(2150-y)

    u = (y - 1820) / 100
    u2 = u * u
    return -20 + 32*u2