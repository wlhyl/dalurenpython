import datetime
from ganzhiwuxin import *
from shipan.shipan import ShiPan
from common import GetLi
#     a = MinGPan(2018, 6, 15,13, 22, 7, "申", "未", True, "abc")
t = datetime.datetime.now()
for k in range(0, 50):
    t0 = t + datetime.timedelta(days=k)
    for i in range(0, 12):
        __月将 = GetLi(t0.year, t0.month, t0.day, t0.hour, t0.minute, t0.second)[4]
        a = ShiPan(t0.year, t0.month, t0.day,20, 22, 7, str(__月将), str(支("子") + i), True, "abc",0,2018)
        if "二烦卦" in a.格局:
            print("{} {}".format(t0, str(支("子") + i)))