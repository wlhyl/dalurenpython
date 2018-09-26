import math


# Mod2Pi 把角度限制在[0, 2π]之间
def Mod2Pi(r):
    while r < 0:
        r += math.pi * 2

    while r > 2*math.pi:
        r -= math.pi * 2
    return r