import datetime
from ganzhiwuxin import *
from shipan.shipan import ShiPan
#     a = MinGPan(2018, 6, 15,13, 22, 7, "申", "未", True, "abc")
t = datetime.datetime.now()
for k in range(0, 50):
    t0 = t + datetime.timedelta(days=k)
    for i in range(0, 12):
        a = ShiPan(t0.year, t0.month, t0.day,20, 22, 7, "午", str(支("子") + i), True, "abc",0,2018)
        if "微服卦" in a.格局:
            print(t0)