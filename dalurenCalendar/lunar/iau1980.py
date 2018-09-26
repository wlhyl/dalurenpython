import math


# T 是  儒略世纪数
# 返回 弧度
def GetEarthNutationParameter(T):
    T2 = T * T
    T3 = T2 * T

    # 平距角（如月对地心的角距离）
    D = math.radians(297.85036 + 445267.111480 * T - 0.0019142 * T2 + T3 / 189474.0)

    # 太阳（地球）平近点角
    M = math.radians(357.52772 + 35999.050340 * T - 0.0001603 * T2 - T3 / 300000.0)

    # 月亮平近点角
    Mp = math.radians(134.96298 + 477198.867398 * T + 0.0086972 * T2 + T3 / 56250.0)

    # 月亮纬度参数
    F = math.radians(93.27191 + 483202.017538 * T - 0.0036825 * T2 + T3 / 327270.0)

    # 黄道与月亮平轨道升交点黄经
    Omega = math.radians(125.04452 - 1934.136261 * T + 0.0020708 * T2 + T3 / 450000.0)
    return D, M, Mp, F, Omega


# 天体章动系数类型变量
class NuationCoefficient():
    def __init__(self, D, M, Mp, F, Omega, Sine1, Sine2, Cosine1, Cosine2):
        self.D = D
        self.M = M
        self.Mp = Mp
        self.F = F
        self.Omega = Omega
        self.Sine1 = Sine1
        self.Sine2 = Sine2
        self.Cosine1 = Cosine1
        self.Cosine2 = Cosine2


nuation = [
    NuationCoefficient(0, 0, 0, 0, 1, -171996, -174.2, 92025, 8.9),
    NuationCoefficient(-2, 0, 0, 2, 2, -13187, -1.6, 5736, -3.1),
    NuationCoefficient(0, 0, 0, 2, 2, -2274, -0.2, 977, -0.5),
    NuationCoefficient(0, 0, 0, 0, 2, 2062, 0.2, -895, 0.5),
    NuationCoefficient(0, 1, 0, 0, 0, 1426, -3.4, 54, -0.1),
    NuationCoefficient(0, 0, 1, 0, 0, 712, 0.1, -7, 0),
    NuationCoefficient(-2, 1, 0, 2, 2, -517, 1.2, 224, -0.6),
    NuationCoefficient(0, 0, 0, 2, 1, -386, -0.4, 200, 0),
    NuationCoefficient(0, 0, 1, 2, 2, -301, 0, 129, -0.1),
    NuationCoefficient(-2, -1, 0, 2, 2, 217, -0.5, -95, 0.3),
    NuationCoefficient(-2, 0, 1, 0, 0, -158, 0, 0, 0),
    NuationCoefficient(-2, 0, 0, 2, 1, 129, 0.1, -70, 0),
    NuationCoefficient(0, 0, -1, 2, 2, 123, 0, -53, 0),
    NuationCoefficient(2, 0, 0, 0, 0, 63, 0, 0, 0),
    NuationCoefficient(0, 0, 1, 0, 1, 63, 0.1, -33, 0),
    NuationCoefficient(2, 0, -1, 2, 2, -59, 0, 26, 0),
    NuationCoefficient(0, 0, -1, 0, 1, -58, -0.1, 32, 0),
    NuationCoefficient(0, 0, 1, 2, 1, -51, 0, 27, 0),
    NuationCoefficient(-2, 0, 2, 0, 0, 48, 0, 0, 0),
    NuationCoefficient(0, 0, -2, 2, 1, 46, 0, -24, 0),
    NuationCoefficient(2, 0, 0, 2, 2, -38, 0, 16, 0),
    NuationCoefficient(0, 0, 2, 2, 2, -31, 0, 13, 0),
    NuationCoefficient(0, 0, 2, 0, 0, 29, 0, 0, 0),
    NuationCoefficient(-2, 0, 1, 2, 2, 29, 0, -12, 0),
    NuationCoefficient(0, 0, 0, 2, 0, 26, 0, 0, 0),
    NuationCoefficient(-2, 0, 0, 2, 0, -22, 0, 0, 0),
    NuationCoefficient(0, 0, -1, 2, 1, 21, 0, -10, 0),
    NuationCoefficient(0, 2, 0, 0, 0, 17, -0.1, 0, 0),
    NuationCoefficient(2, 0, -1, 0, 1, 16, 0, -8, 0),
    NuationCoefficient(-2, 2, 0, 2, 2, -16, 0.1, 7, 0),
    NuationCoefficient(0, 1, 0, 0, 1, -15, 0, 9, 0),
    NuationCoefficient(-2, 0, 1, 0, 1, -13, 0, 7, 0),
    NuationCoefficient(0, -1, 0, 0, 1, -12, 0, 6, 0),
    NuationCoefficient(0, 0, 2, -2, 0, 11, 0, 0, 0),
    NuationCoefficient(2, 0, -1, 2, 1, -10, 0, 5, 0),
    NuationCoefficient(2, 0, 1, 2, 2, -8, 0, 3, 0),
    NuationCoefficient(0, 1, 0, 2, 2, 7, 0, -3, 0),
    NuationCoefficient(-2, 1, 1, 0, 0, -7, 0, 0, 0),
    NuationCoefficient(0, -1, 0, 2, 2, -7, 0, 3, 0),
    NuationCoefficient(2, 0, 0, 2, 1, -7, 0, 3, 0),
    NuationCoefficient(2, 0, 1, 0, 0, 6, 0, 0, 0),
    NuationCoefficient(-2, 0, 2, 2, 2, 6, 0, -3, 0),
    NuationCoefficient(-2, 0, 1, 2, 1, 6, 0, -3, 0),
    NuationCoefficient(2, 0, -2, 0, 1, -6, 0, 3, 0),
    NuationCoefficient(2, 0, 0, 0, 1, -6, 0, 3, 0),
    NuationCoefficient(0, -1, 1, 0, 0, 5, 0, 0, 0),
    NuationCoefficient(-2, -1, 0, 2, 1, -5, 0, 3, 0),
    NuationCoefficient(-2, 0, 0, 0, 1, -5, 0, 3, 0),
    NuationCoefficient(0, 0, 2, 2, 1, -5, 0, 3, 0),
    NuationCoefficient(-2, 0, 2, 0, 1, 4, 0, 0, 0),
    NuationCoefficient(-2, 1, 0, 2, 1, 4, 0, 0, 0),
    NuationCoefficient(0, 0, 1, -2, 0, 4, 0, 0, 0),
    NuationCoefficient(-1, 0, 1, 0, 0, -4, 0, 0, 0),
    NuationCoefficient(-2, 1, 0, 0, 0, -4, 0, 0, 0),
    NuationCoefficient(1, 0, 0, 0, 0, -4, 0, 0, 0),
    NuationCoefficient(0, 0, 1, 2, 0, 3, 0, 0, 0),
    NuationCoefficient(0, 0, -2, 2, 2, -3, 0, 0, 0),
    NuationCoefficient(-1, -1, 1, 0, 0, -3, 0, 0, 0),
    NuationCoefficient(0, 1, 1, 0, 0, -3, 0, 0, 0),
    NuationCoefficient(0, -1, 1, 2, 2, -3, 0, 0, 0),
    NuationCoefficient(2, -1, -1, 2, 2, -3, 0, 0, 0),
    NuationCoefficient(0, 0, 3, 2, 2, -3, 0, 0, 0),
    NuationCoefficient(2, -1, 0, 2, 2, -3, 0, 0, 0),
]

coefficient = math.radians(0.0001/3600)

# 计算某时刻的黄经章动干扰量
#  儒略世纪数
# 返回弧度
def CalcEarthLongitudeNutation(T):
    D, M, Mp, F, Omega = GetEarthNutationParameter(T)
    result=0
    for n in nuation:
        theta = n.D*D + n.M*M + n.Mp*Mp + n.F*F +n.Omega*Omega
        result += (n.Sine1 + n.Sine2*T) * math.sin(theta)

    # 乘以章动表的系数 0.0001 角秒
    return result * coefficient


# 计算某时刻的黄赤交角章动干扰量，dt是儒略千年数，返回值单位是度*

# 计算某时刻的黄赤交角章动干扰量
# dt 是儒略世纪数
# 返回弧度
def CalcEarthObliquityNutation(dt):
    D, M, Mp, F, Omega = GetEarthNutationParameter(dt)
    result=0

    for n in nuation:
        # sita 弧度
        theta = n.D*D + n.M*M + n.Mp*Mp + n.F*F +n.Omega*Omega
        result += (n.Cosine1 + n.Cosine2*dt) * math.cos(theta)

    # 乘以章动表的系数 0.0001 角秒
    return result * coefficient

