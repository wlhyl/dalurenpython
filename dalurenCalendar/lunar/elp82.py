import math
from dalurenCalendar.util import GetJulianCentury
from dalurenCalendar.lunar.mathutil import Mod2Pi
from dalurenCalendar.lunar.elp82_const import MoonLongitude
from dalurenCalendar.lunar.iau1980 import CalcEarthLongitudeNutation


# 参数 T 儒略世纪数
# 返回 弧度
def GetMoonEclipticParameter(T):
    T2 = T * T
    T3 = T2 * T
    T4 = T3 * T

    # 月球平黄经
    Lp = Mod2Pi(math.radians(218.3164591 + 481267.88134236 * T - 0.0013268 * T2 + T3 / 538841.0 - T4 / 65194000.0))

    # 月日距角
    D = Mod2Pi(math.radians(297.8502042 + 445267.1115168 * T - 0.0016300 * T2 + T3 / 545868.0 - T4 / 113065000.0))

    # 太阳平近点角
    M = Mod2Pi(math.radians(357.5291092 + 35999.0502909 * T - 0.0001536 * T2 + T3 / 24490000.0))

    # 月亮平近点角
    Mp = Mod2Pi(math.radians(134.9634114 + 477198.8676313 * T + 0.0089970 * T2 + T3 / 69699.0 - T4 / 14712000.0))

    # 月球经度参数(到升交点的平角距离)
    F = Mod2Pi(math.radians(93.2720993 + 483202.0175273 * T - 0.0034029 * T2 - T3 / 3526000.0 + T4 / 863310000.0))

    # 反映地球轨道偏心率变化的辅助参量
    E = 1 - 0.002516 * T - 0.0000074 * T2
    return Lp, D, M, Mp, F, E


# 计算月球地心黄经周期项的和
def CalcMoonECLongitudePeriodic(D, M, Mp, F, E):
    EI = 0
    for l in MoonLongitude:
        theta = l.D * D + l.M * M + l.Mp * Mp + l.F * F
        EI += l.EiA * math.sin(theta) * math.pow(E, abs(l.M))

    # fmt.Printf("EI = %f\n", EI)
    return EI


# 计算金星摄动,木星摄动以及地球扁率摄动对月球地心黄经的影响, T 是儒略世纪数，Lp和F单位是弧度
#  A1 = 119.75 + 131.849 * T                                             （4.13式）
#  A2 = 53.09 + 479264.290 * T                                           （4.14式）
#  A3 = 313.45 + 481266.484 * T                                          （4.15式）
def CalcMoonLongitudePerturbation(T, Lp, F):
    A1 = Mod2Pi(math.radians(119.75 + 131.849 * T))
    A2 = Mod2Pi(math.radians(53.09 + 479264.290 * T))

    return 3958.0 * math.sin(A1) + 1962.0 * math.sin(Lp - F) + 318.0 * math.sin(A2)


# 计算月球地心黄经
# jd 儒略日
# 返回 弧度
def GetMoonEclipticLongitudeEC(jd):
    T = GetJulianCentury(jd)
    Lp, D, M, Mp, F, E = GetMoonEclipticParameter(T)

    # 计算月球地心黄经周期项
    EI = CalcMoonECLongitudePeriodic(D, M, Mp, F, E)

    # 修正金星,木星以及地球扁率摄动
    EI += CalcMoonLongitudePerturbation(T, Lp, F)

    longitude = Lp + math.radians(EI / 1000000.0)

    # 计算天体章动干扰
    longitude += CalcEarthLongitudeNutation(T)
    return longitude
