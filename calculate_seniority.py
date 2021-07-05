#計算年資使用(到小數第二位)，天數換算年：
import math
import datetime
from decimal import Decimal
start_time = datetime.date(2018, 1, 23) #第一天(從這天開始算)
end_time = datetime.date(2021, 3, 21) #最後一天(輸入的日期會跑到當天)
Time_gap = (end_time - start_time).days
Time_gap_for_year = Time_gap/365
Time_gap_for_year_Decimal = '{:.2f}'.format(Decimal(str(Time_gap_for_year))) #四捨五入法
Time_gap_for_year_ceil = math.ceil(Time_gap_for_year*100) #進位
Time_gap_for_year_floor = math.floor(Time_gap_for_year*100) #捨去
Time_gap_for_year_ceil = Time_gap_for_year_ceil/100
Time_gap_for_year_floor = Time_gap_for_year_floor/100
print("Time_gap天數:",Time_gap)
# print("Time_gap_for_year型態:",type(Time_gap_for_year))
print("Time_gap_for_year天換算年:",Time_gap_for_year)
print("Time_gap_for_year四捨五入:",Time_gap_for_year_Decimal)
print("Time_gap_for_year無條件進位:",Time_gap_for_year_ceil)
print("Time_gap_for_year無條件捨去:",Time_gap_for_year_floor)