import datetime
import math
from dalurenCalendar.lunar.elp82 import GetMoonEclipticLongitudeEC
from dalurenCalendar.util.julianday import GetJulianDayFromDateTime

t = datetime.datetime(2018, 9, 26, 12, 0, 0)
t -= datetime.timedelta(hours=8)
jd = GetJulianDayFromDateTime(t)
longitude = GetMoonEclipticLongitudeEC(jd)
longitude = math.degrees(longitude)
print(jd)
print(longitude)