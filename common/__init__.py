import sqlite3
import os
import datetime
from ganzhiwuxin import *

DB = os.path.dirname(os.path.realpath(__file__)) + '/data/lifa.db'
DiZHiList = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]


def GetShiChen(h):
    '''
    int((h+1)/2)+1 可以得到时辰数
    当h=23，得到13,即第二日子时
    '''
    s = (h + 1) // 2 + 1
    if s == 13:
        s = 1
    return 支(s)


# 取得占日的历法数据
# 返回 四柱 月将
def GetLi(y, m, d, h, minu, sec):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    queryString = 'select  id,jiqi,solaryear, solarmonth, solarday, solarhours, ganzhimonth,ganzhiyear,ganzhiday from litable where solaryear = {} and solarmonth = {} and ' \
                  'jiqi in ("冬至","大寒","雨水","春分","谷雨","小满","夏至","大暑","处暑","秋分","霜降","小雪") '.format(y, m)

    cursor = c.execute(queryString)
    for row in cursor:
        中气=row

    queryString = 'select  id,jiqi,solaryear, solarmonth, solarday, solarhours, ganzhimonth,ganzhiyear,ganzhiday from litable where id={}'.format(中气[0]-1)
    cursor = c.execute(queryString)
    for row in cursor:
        前一节=row

    queryString = 'select  id,jiqi,solaryear, solarmonth, solarday, solarhours, ganzhimonth,ganzhiyear,ganzhiday from litable where id={}'.format(中气[0]-2)
    cursor = c.execute(queryString)
    for row in cursor:
        前一气=row

    queryString = 'select  id,jiqi,solaryear, solarmonth, solarday, solarhours, ganzhimonth,ganzhiyear,ganzhiday from litable where id={}'.format(中气[0] + 1)
    cursor = c.execute(queryString)
    for row in cursor:
        後一节 = row

    queryString = 'select  id,jiqi,solaryear, solarmonth, solarday, solarhours, ganzhimonth,ganzhiyear,ganzhiday from litable where id={}'.format(中气[0] + 2)
    cursor = c.execute(queryString)
    for row in cursor:
        後一气 = row
        #     ={
        #     "id":int(row[0]),
        #     "jiqi": row[1],
        #     "solaryear": int(row[2]),
        # }

        # cursor = c.execute('select solaryear, solarmonth, solarday, solarhours, ganzhiyear, ganzhimonth from   litable where id={}'.format(id))
        # for row in cursor:

        # solarmonth = int(row[3])
        # solarday = int(row[4])
        # solarhours = row[5]
        # ganzhimonth = row[6][0:2]
    #     ganzhiyear = row[4][0:2]

    conn.close()
    timeString = "{0}-{1:02d}-{2:02d} {3}".format(中气[2], 中气[3], 中气[4], 中气[5])
    中气Time = datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S")

    timeString = "{0}-{1:02d}-{2:02d} {3}".format(前一节[2], 前一节[3], 前一节[4], 前一节[5])
    前一节Time = datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S")

    timeString = "{0}-{1:02d}-{2:02d} {3}".format(前一气[2], 前一气[3], 前一气[4], 前一气[5])
    前一气Time = datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S")

    timeString = "{0}-{1:02d}-{2:02d} {3}".format(後一节[2], 後一节[3], 後一节[4], 後一节[5])
    後一节Time = datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S")

    timeString = "{0}-{1:02d}-{2:02d} {3}".format(後一气[2], 後一气[3], 後一气[4], 後一气[5])
    後一气Time = datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S")

    timeString = "{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}".format(
        y, m, d, h, minu, sec)
    占时Time = datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S")
    中气月支=支(中气[6][1:2])
    for i in ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]:
        if 中气月支.六合(支(i)):
            月将=支(i)
            break

    if 占时Time >= 後一气Time:
        月将=月将-1
        年柱=干支(干(後一气[7][0:1]), 支(後一气[7][1:2]))
        月柱=干支(干(後一气[6][0:1]), 支(後一气[6][1:2]))
        # 日柱=干支(干(後一气[8][0:1]),支(後一气[8][1:2])) + (占时Time-後一气Time).days

        节 = "{} {}".format(後一节[1], 後一节Time)
        气 = "{} {}".format(後一气[1], 後一气Time)

    if 占时Time >= 中气Time:
        # 月将 = 月将 - 1
        if 占时Time >= 後一节Time:
            年柱 = 干支(干(後一节[7][0:1]), 支(後一节[7][1:2]))
            月柱 = 干支(干(後一节[6][0:1]), 支(後一节[6][1:2]))

            # 日柱 = 干支(干(後一节[8][0:1]), 支(後一节[8][1:2])) + (占时Time - 後一节Time).days
            节 = "{} {}".format(後一节[1], 後一节Time)
            气 = "{} {}".format(後一气[1], 後一气Time)
        else:
            年柱 = 干支(干(中气[7][0:1]), 支(中气[7][1:2]))
            月柱 = 干支(干(中气[6][0:1]), 支(中气[6][1:2]))
            # 日柱 = 干支(干(中气[8][0:1]), 支(中气[8][1:2])) + (占时Time - 中气Time).days
            节 = "{} {}".format(前一节[1], 前一节Time)
            气 = "{} {}".format(中气[1], 中气Time)

    if 占时Time < 中气Time and 占时Time >= 前一节Time:
        月将 = 月将 + 1
        年柱 = 干支(干(中气[7][0:1]), 支(中气[7][1:2]))
        月柱 = 干支(干(中气[6][0:1]), 支(中气[6][1:2]))
        # 日柱 = 干支(干(中气[8][0:1]), 支(中气[8][1:2])) + (占时Time - 中气Time).days

        节="{} {}".format(前一节[1], 前一节Time)
        气="{} {}".format(中气[1], 中气Time)

    if 占时Time < 前一节Time and 占时Time >= 前一气Time:
        月将 = 月将 + 1
        年柱 = 干支(干(前一气[7][0:1]), 支(前一气[7][1:2]))
        月柱 = 干支(干(前一气[6][0:1]), 支(前一气[6][1:2]))

        节="{} {}".format(前一节[1], 前一节Time)
        气="{} {}".format(前一气[1], 前一气Time)

    if 占时Time < 前一气Time:
        月将 = 月将 + 2
        年柱 = 干支(干(前一气[7][0:1]), 支(前一气[7][1:2]))
        月柱 = 干支(干(前一气[6][0:1]), 支(前一气[6][1:2]))

        节="{} {}".format(前一节[1], 前一节Time)
        气="{} {}".format(前一气[1], 前一气Time)

    if 占时Time.time() >= datetime.time(23, 0):
        占时Time = 占时Time+datetime.timedelta(hours=1)

    # 日柱 = 干支(干(中气[8][0:1]), 支(中气[8][1:2])) + (占时Time - 中气Time).days
    日柱 = 干支(干(中气[8][0:1]), 支(中气[8][1:2])) + (datetime.datetime(占时Time.year, 占时Time.month, 占时Time.day)-datetime.datetime(中气Time.year, 中气Time.month, 中气Time.day)).days
    时辰 = GetShiChen(h)
    if 日柱.干 == 干("甲") or 日柱.干 == 干("己"):
        子时天干 = 干("甲")
    if 日柱.干 == 干("乙") or 日柱.干 == 干("庚"):
        子时天干 = 干("丙")
    if 日柱.干 == 干("丙") or 日柱.干 == 干("辛"):
        子时天干 = 干("戊")
    if 日柱.干 == 干("丁") or 日柱.干 == 干("壬"):
        子时天干 = 干("庚")
    if 日柱.干 == 干("戊") or 日柱.干 == 干("癸"):
        子时天干 = 干("壬")
    时柱 = 干支(子时天干 + (时辰 - 支('子')), 时辰)
    return [年柱, 月柱, 日柱, 时柱, 月将, 节, 气]


if __name__ == "__main__":
    # for i in range(0,24):
    #     print("{}  {}".format(i,GetShiChen(i)))
    a=GetLi(2018, 4, 20, 23, 23, 22)
    for i in a:
        print(i)
