#date类
from  datetime  import  *  
import  time  
  
print   'date.max:' , date.max  
print   'date.min:' , date.min  
print   'date.today():' , date.today()  
print   'date.fromtimestamp():' , date.fromtimestamp(time.time())  
  
# # ---- 结果 ----   
# date.max: 9999-12-31   
# date.min: 0001-01-01   
# date.today(): 2010-04-06   
# date.fromtimestamp(): 2010-04-06


from datetime import *  
import time  
  
print 'date.max:', date.max  
print 'date.min:', date.min  
print 'date.today():', date.today()  
print 'date.fromtimestamp():', date.fromtimestamp(time.time())  
  
# # ---- 结果 ----  
# date.max: 9999-12-31  
# date.min: 0001-01-01  
# date.today(): 2010-04-06  
# date.fromtimestamp(): 2010-04-06  
#date提供的实例方法和属性：
now = date( 2010 ,  04 ,  06 )  
tomorrow = now.replace(day = 07 )  
print   'now:' , now,  ', tomorrow:' , tomorrow  
print   'timetuple():' , now.timetuple()  
print   'weekday():' , now.weekday()  
print   'isoweekday():' , now.isoweekday()  
print   'isocalendar():' , now.isocalendar()  
print   'isoformat():' , now.isoformat()  
  
# # ---- 结果 ----   
# now: 2010-04-06 , tomorrow: 2010-04-07   
# timetuple(): (2010, 4, 6, 0, 0, 0, 1, 96, -1)   
# weekday(): 1   
# isoweekday(): 2   
# isocalendar(): (2010, 14, 2)   
# isoformat(): 2010-04-06


now = date(2010, 04, 06)  
tomorrow = now.replace(day = 07)  
print 'now:', now, ', tomorrow:', tomorrow  
print 'timetuple():', now.timetuple()  
print 'weekday():', now.weekday()  
print 'isoweekday():', now.isoweekday()  
print 'isocalendar():', now.isocalendar()  
print 'isoformat():', now.isoformat()  
  
# # ---- 结果 ----  
# now: 2010-04-06 , tomorrow: 2010-04-07  
# timetuple(): (2010, 4, 6, 0, 0, 0, 1, 96, -1)  
# weekday(): 1  
# isoweekday(): 2  
# isocalendar(): (2010, 14, 2)  
# isoformat(): 2010-04-06

#date还对某些操作进行了重载，它允许我们对日期进行如下一些操作：
#date2 = date1 + timedelta  # 日期加上一个间隔，返回一个新的日期对象（timedelta将在下面介绍，表示时间间隔）
#date2 = date1 - timedelta   # 日期隔去间隔，返回一个新的日期对象
#timedelta = date1 - date2   # 两个日期相减，返回一个时间间隔对象
#date1 < date2  # 两个日期进行比较
now = date.today()  
tomorrow = now.replace(day = 7 )  
delta = tomorrow - now  
print   'now:' , now,  ' tomorrow:' , tomorrow  
print   'timedelta:' , delta  
print  now + delta  
print  tomorrow > now  
  
# # ---- 结果 ----   
# now: 2010-04-06  tomorrow: 2010-04-07   
# timedelta: 1 day, 0:00:00   
# 2010-04-07   
# True

now = date.today()  
tomorrow = now.replace(day = 7)  
delta = tomorrow - now  
print 'now:', now, ' tomorrow:', tomorrow  
print 'timedelta:', delta  
print now + delta  
print tomorrow > now  
  
# # ---- 结果 ----  
# now: 2010-04-06  tomorrow: 2010-04-07  
# timedelta: 1 day, 0:00:00  
# 2010-04-07  
# True  

#Time类
   # time类表示时间，由时、分、秒以及微秒组成
from  datetime  import  *  
tm = time(23 ,  46 ,  10 )  
print   'tm:' , tm  
print   'hour: %d, minute: %d, second: %d, microsecond: %d'\
        % (tm.hour, tm.minute, tm.second, tm.microsecond)  
tm1 = tm.replace(hour = 20 )  
print   'tm1:' , tm1  
print   'isoformat():' , tm.isoformat()  
  
# # ---- 结果 ----   
# tm: 23:46:10   
# hour: 23, minute: 46, second: 10, microsecond: 0   
# tm1: 20:46:10   
# isoformat(): 23:46:10   
from datetime import *  
tm = time(23, 46, 10)  
print 'tm:', tm  
print 'hour: %d, minute: %d, second: %d, microsecond: %d'% (tm.hour, tm.minute, tm.second, tm.microsecond) 
          
tm1 = tm.replace(hour = 20)  
print 'tm1:', tm1  
print 'isoformat():', tm.isoformat()  
  
# # ---- 结果 ----  
# tm: 23:46:10  
# hour: 23, minute: 46, second: 10, microsecond: 0  
# tm1: 20:46:10  
# isoformat(): 23:46:10

#datetime类
from  datetime  import  *  
import  time  
  
print   'datetime.max:' , datetime.max  
print   'datetime.min:' , datetime.min  
print   'datetime.resolution:' , datetime.resolution  
print   'today():' , datetime.today()  
print   'now():' , datetime.now()  
print   'utcnow():' , datetime.utcnow()  
print   'fromtimestamp(tmstmp):' , datetime.fromtimestamp(time.time())  
print   'utcfromtimestamp(tmstmp):' , datetime.utcfromtimestamp(time.time())  
  
# ---- 结果 ----   
# datetime.max: 9999-12-31 23:59:59.999999   
# datetime.min: 0001-01-01 00:00:00   
# datetime.resolution: 0:00:00.000001   
# today(): 2010-04-07 09:48:16.234000   
# now(): 2010-04-07 09:48:16.234000   
# utcnow(): 2010-04-07 01:48:16.234000  # 中国位于+8时间，与本地时间相差8   
# fromtimestamp(tmstmp): 2010-04-07 09:48:16.234000   
# utcfromtimestamp(tmstmp): 2010-04-07 01:48:16.234000   
from datetime import *  
import time  
  
print 'datetime.max:', datetime.max  
print 'datetime.min:', datetime.min  
print 'datetime.resolution:', datetime.resolution  
print 'today():', datetime.today()  
print 'now():', datetime.now()  
print 'utcnow():', datetime.utcnow()  
print 'fromtimestamp(tmstmp):', datetime.fromtimestamp(time.time())  
print 'utcfromtimestamp(tmstmp):', datetime.utcfromtimestamp(time.time())

  
# ---- 结果 ----  
# datetime.max: 9999-12-31 23:59:59.999999  
# datetime.min: 0001-01-01 00:00:00  
# datetime.resolution: 0:00:00.000001  
# today(): 2010-04-07 09:48:16.234000  
# now(): 2010-04-07 09:48:16.234000  
# utcnow(): 2010-04-07 01:48:16.234000  # 中国位于+8时间，与本地时间相差8  
# fromtimestamp(tmstmp): 2010-04-07 09:48:16.234000  
# utcfromtimestamp(tmstmp): 2010-04-07 01:48:16.234000 

#格式字符串
'''
格式字符  意义

%a 星期的简写。如 星期三为Web
%A 星期的全写。如 星期三为Wednesday
%b 月份的简写。如4月份为Apr
%B月份的全写。如4月份为April 
%c:  日期时间的字符串表示。（如： 04/07/10 10:43:39）
%d:  日在这个月中的天数（是这个月的第几天）
%f:  微秒（范围[0,999999]）
%H:  小时（24小时制，[0, 23]）
%I:  小时（12小时制，[0, 11]）
%j:  日在年中的天数 [001,366]（是当年的第几天）
%m:  月份（[01,12]）
%M:  分钟（[00,59]）
%p:  AM或者PM
%S:  秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）
%U:  周在当年的周数当年的第几周），星期天作为周的第一天
%w:  今天在这周的天数，范围为[0, 6]，6表示星期天
%W:  周在当年的周数（是当年的第几周），星期一作为周的第一天
%x:  日期字符串（如：04/07/10）
%X:  时间字符串（如：10:43:39）
%y:  2个数字表示的年份
%Y:  4个数字表示的年份
%z:  与utc时间的间隔 （如果是本地时间，返回空字符串）
%Z:  时区名称（如果是本地时间，返回空字符串）
%%:  %% => %
'''
dt = datetime.now()  
print   '(%Y-%m-%d %H:%M:%S %f): ' , dt.strftime( '%Y-%m-%d %H:%M:%S %f' )  
print   '(%Y-%m-%d %H:%M:%S %p): ' , dt.strftime( '%y-%m-%d %I:%M:%S %p' )  
print   '%%a: %s '  % dt.strftime( '%a' )  
print   '%%A: %s '  % dt.strftime( '%A' )  
print   '%%b: %s '  % dt.strftime( '%b' )  
print   '%%B: %s '  % dt.strftime( '%B' )  
print   '日期时间%%c: %s '  % dt.strftime( '%c' )  
print   '日期%%x：%s '  % dt.strftime( '%x' )  
print   '时间%%X：%s '  % dt.strftime( '%X' )  
print   '今天是这周的第%s天 '  % dt.strftime( '%w' )  
print   '今天是今年的第%s天 '  % dt.strftime( '%j' )  
print   '今周是今年的第%s周 '  % dt.strftime( '%U' )
#04/01/13 09:00:00   20130401
print dt.strftime('%m/%d/%y  %H:%M:%S')
  
# # ---- 结果 ----   
# (%Y-%m-%d %H:%M:%S %f):  2010-04-07 10:52:18 937000   
# (%Y-%m-%d %H:%M:%S %p):  10-04-07 10:52:18 AM   
# %a: Wed    
# %A: Wednesday    
# %b: Apr    
# %B: April    
# 日期时间%c: 04/07/10 10:52:18    
# 日期%x：04/07/10    
# 时间%X：10:52:18    
# 今天是这周的第3天    
# 今天是今年的第097天    
# 今周是今年的第14周   
dt = datetime.now()  
print '(%Y-%m-%d %H:%M:%S %f): ', dt.strftime('%Y-%m-%d %H:%M:%S %f')  
print '(%Y-%m-%d %H:%M:%S %p): ', dt.strftime('%y-%m-%d %I:%M:%S %p')  
print '%%a: %s ' % dt.strftime('%a')  
print '%%A: %s ' % dt.strftime('%A')  
print '%%b: %s ' % dt.strftime('%b')  
print '%%B: %s ' % dt.strftime('%B')  
print '日期时间%%c: %s ' % dt.strftime('%c')  
print '日期%%x：%s ' % dt.strftime('%x')  
print '时间%%X：%s ' % dt.strftime('%X')  
print '今天是这周的第%s天 ' % dt.strftime('%w')  
print '今天是今年的第%s天 ' % dt.strftime('%j')  
print '今周是今年的第%s周 ' % dt.strftime('%U')  
  
# # ---- 结果 ----  
# (%Y-%m-%d %H:%M:%S %f):  2010-04-07 10:52:18 937000  
# (%Y-%m-%d %H:%M:%S %p):  10-04-07 10:52:18 AM  
# %a: Wed   
# %A: Wednesday   
# %b: Apr   
# %B: April   
# 日期时间%c: 04/07/10 10:52:18   
# 日期%x：04/07/10   
# 时间%X：10:52:18   
# 今天是这周的第3天   
# 今天是今年的第097天   
# 今周是今年的第14周  

#----------------.将字符串的时间转换为时间戳---------------
a = "2013-10-10 23:40:00"
#将其转换为时间数组
import time
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
#转换为时间戳:
timeStamp = int(time.mktime(timeArray))
timeStamp == 1381419600


#-------------格式更改---------------------------
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)

#---------------时间戳转换为指定格式日期-------------------
timeStamp = 1381419600
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
otherStyletime == "2013-10-10 23:40:00"

'''
>>>import datetime
>>> d1 = datetime.datetime.now()
>>> d1.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:11:07'
>>> d2 = d1 + datetime.timedelta(seconds=10)#增加10秒
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:11:17'
>>> d2 = d1 + datetime.timedelta(minutes=10)#增加10分钟
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:21:07'
>>> d2 = d1 + datetime.timedelta(hours=10)#增加10小时
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-03 03:11:07'
>>> d2 = d1 + datetime.timedelta(days=10)#增加10天
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-12 17:11:07'
>>> d2 = d1 - datetime.timedelta(seconds=10)#减去10秒
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:11:57'
>>> d2 = d1 - datetime.timedelta(minutes=10)#增加10分钟
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:01:07'
>>> d2 = d1 - datetime.timedelta(hours=10)#减去10小时
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 07:11:07'
>>> d2 = d1 - datetime.timedelta(days=10)#减去10天
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-08-23 17:11:07'
'''








