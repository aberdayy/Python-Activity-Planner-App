import datetime
import time

cizgisiz_zaman = "122723"
ay = cizgisiz_zaman[:2]
gun = cizgisiz_zaman[2:4]
a = cizgisiz_zaman[4:6]

str(a)
yil =   "20"+a
x = datetime.datetime(int(yil), int(ay), int(gun))
timestamp = time.mktime(x.timetuple())

print(timestamp)
