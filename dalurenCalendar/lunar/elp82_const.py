# 月地心黄经系数
class MoonEclipticLongitudeCoeff():
    def __init__(self, D, M, Mp, F, EiA, ErA):
        self.D = D
        self.M = M
        self.Mp = Mp
        self.F = F
        self.EiA = EiA
        self.ErA = ErA


# 月球黄经周期项(ΣI)及距离(Σr).
# 黄经单位:0.000001度,距离单位:0.001千米.
# --------------------------------------------------
# 角度的组合系数  ΣI的各项振幅A  Σr的各项振幅A
# D  M  M' F        (正弦振幅)       (余弦振幅)
# --------------------------------------------------

MoonLongitude = [
    MoonEclipticLongitudeCoeff(0, 0, 1, 0, 6288744, -20905355),
    MoonEclipticLongitudeCoeff(2, 0, -1, 0, 1274027, -3699111),
    MoonEclipticLongitudeCoeff(2, 0, 0, 0, 658314, -2955968),
    MoonEclipticLongitudeCoeff(0, 0, 2, 0, 213618, -569925),
    MoonEclipticLongitudeCoeff(0, 1, 0, 0, -185116, 48888),
    MoonEclipticLongitudeCoeff(0, 0, 0, 2, -114332, -3149),
    MoonEclipticLongitudeCoeff(2, 0, -2, 0, 58793, 246158),
    MoonEclipticLongitudeCoeff(2, -1, -1, 0, 57066, -152138),
    MoonEclipticLongitudeCoeff(2, 0, 1, 0, 53322, -170733),
    MoonEclipticLongitudeCoeff(2, -1, 0, 0, 45758, -204586),
    MoonEclipticLongitudeCoeff(0, 1, -1, 0, -40923, -129620),
    MoonEclipticLongitudeCoeff(1, 0, 0, 0, -34720, 108743),
    MoonEclipticLongitudeCoeff(0, 1, 1, 0, -30383, 104755),
    MoonEclipticLongitudeCoeff(2, 0, 0, -2, 15327, 10321),
    MoonEclipticLongitudeCoeff(0, 0, 1, 2, -12528, 0),
    MoonEclipticLongitudeCoeff(0, 0, 1, -2, 10980, 79661),
    MoonEclipticLongitudeCoeff(4, 0, -1, 0, 10675, -34782),
    MoonEclipticLongitudeCoeff(0, 0, 3, 0, 10034, -23210),
    MoonEclipticLongitudeCoeff(4, 0, -2, 0, 8548, -21636),
    MoonEclipticLongitudeCoeff(2, 1, -1, 0, -7888, 24208),
    MoonEclipticLongitudeCoeff(2, 1, 0, 0, -6766, 30824),
    MoonEclipticLongitudeCoeff(1, 0, -1, 0, -5163, -8379),
    MoonEclipticLongitudeCoeff(1, 1, 0, 0, 4987, -16675),
    MoonEclipticLongitudeCoeff(2, -1, 1, 0, 4036, -12831),
    MoonEclipticLongitudeCoeff(2, 0, 2, 0, 3994, -10445),
    MoonEclipticLongitudeCoeff(4, 0, 0, 0, 3861, -11650),
    MoonEclipticLongitudeCoeff(2, 0, -3, 0, 3665, 14403),
    MoonEclipticLongitudeCoeff(0, 1, -2, 0, -2689, -7003),
    MoonEclipticLongitudeCoeff(2, 0, -1, 2, -2602, 0),
    MoonEclipticLongitudeCoeff(2, -1, -2, 0, 2390, 10056),
    MoonEclipticLongitudeCoeff(1, 0, 1, 0, -2348, 6322),
    MoonEclipticLongitudeCoeff(2, -2, 0, 0, 2236, -9884),
    MoonEclipticLongitudeCoeff(0, 1, 2, 0, -2120, 5751),
    MoonEclipticLongitudeCoeff(0, 2, 0, 0, -2069, 0),
    MoonEclipticLongitudeCoeff(2, -2, -1, 0, 2048, -4950),
    MoonEclipticLongitudeCoeff(2, 0, 1, -2, -1773, 4130),
    MoonEclipticLongitudeCoeff(2, 0, 0, 2, -1595, 0),
    MoonEclipticLongitudeCoeff(4, -1, -1, 0, 1215, -3958),
    MoonEclipticLongitudeCoeff(0, 0, 2, 2, -1110, 0),
    MoonEclipticLongitudeCoeff(3, 0, -1, 0, -892, 3258),
    MoonEclipticLongitudeCoeff(2, 1, 1, 0, -810, 2616),
    MoonEclipticLongitudeCoeff(4, -1, -2, 0, 759, -1897),
    MoonEclipticLongitudeCoeff(0, 2, -1, 0, -713, -2117),
    MoonEclipticLongitudeCoeff(2, 2, -1, 0, -700, 2354),
    MoonEclipticLongitudeCoeff(2, 1, -2, 0, 691, 0),
    MoonEclipticLongitudeCoeff(2, -1, 0, -2, 596, 0),
    MoonEclipticLongitudeCoeff(4, 0, 1, 0, 549, -1423),
    MoonEclipticLongitudeCoeff(0, 0, 4, 0, 537, -1117),
    MoonEclipticLongitudeCoeff(4, -1, 0, 0, 520, -1571),
    MoonEclipticLongitudeCoeff(1, 0, -2, 0, -487, -1739),
    MoonEclipticLongitudeCoeff(2, 1, 0, -2, -399, 0),
    MoonEclipticLongitudeCoeff(0, 0, 2, -2, -381, -4421),
    MoonEclipticLongitudeCoeff(1, 1, 1, 0, 351, 0),
    MoonEclipticLongitudeCoeff(3, 0, -2, 0, -340, 0),
    MoonEclipticLongitudeCoeff(4, 0, -3, 0, 330, 0),
    MoonEclipticLongitudeCoeff(2, -1, 2, 0, 327, 0),
    MoonEclipticLongitudeCoeff(0, 2, 1, 0, -323, 1165),
    MoonEclipticLongitudeCoeff(1, 1, -1, 0, 299, 0),
    MoonEclipticLongitudeCoeff(2, 0, 3, 0, 294, 0),
    MoonEclipticLongitudeCoeff(2, 0, -1, -2, 0, 8752),
]
