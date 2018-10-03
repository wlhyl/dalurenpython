import eacal
from ganzhiwuxin import *
from shipan.shipan import ShiPan
from common import GetLi

y = 2018
# t = datetime.datetime.now()
for k in range(0, 50):
    c = eacal.EACal(zh_s=True)
    year = y + k
    liChun = c.get_specified_solar_term(year, 0)[2].replace(tzinfo=None)
    liXiao = c.get_specified_solar_term(year, 6)[2].replace(tzinfo=None)
    liQiu = c.get_specified_solar_term(year, 12)[2].replace(tzinfo=None)
    liDong = c.get_specified_solar_term(year, 18)[2].replace(tzinfo=None)
    # t0 = t + datetime.timedelta(days=k)
    for j in [liChun, liXiao, liQiu, liDong]:
        __月将 = GetLi(j.year, j.month, j.day, j.hour, j.minute, j.second)[4]
        for i in range(0, 12):
            a = ShiPan(j.year, j.month, j.day, 20, 22, 7, str(__月将), str(支("子") + i), True, "abc", 0, 2018)
            if "天祸卦" in a.格局:
                print("{} {}".format(j, str(支("子") + i)))
