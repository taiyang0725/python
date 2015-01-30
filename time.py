#date��
from  datetime  import  *  
import  time  
  
print   'date.max:' , date.max  
print   'date.min:' , date.min  
print   'date.today():' , date.today()  
print   'date.fromtimestamp():' , date.fromtimestamp(time.time())  
  
# # ---- ��� ----   
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
  
# # ---- ��� ----  
# date.max: 9999-12-31  
# date.min: 0001-01-01  
# date.today(): 2010-04-06  
# date.fromtimestamp(): 2010-04-06  
#date�ṩ��ʵ�����������ԣ�
now = date( 2010 ,  04 ,  06 )  
tomorrow = now.replace(day = 07 )  
print   'now:' , now,  ', tomorrow:' , tomorrow  
print   'timetuple():' , now.timetuple()  
print   'weekday():' , now.weekday()  
print   'isoweekday():' , now.isoweekday()  
print   'isocalendar():' , now.isocalendar()  
print   'isoformat():' , now.isoformat()  
  
# # ---- ��� ----   
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
  
# # ---- ��� ----  
# now: 2010-04-06 , tomorrow: 2010-04-07  
# timetuple(): (2010, 4, 6, 0, 0, 0, 1, 96, -1)  
# weekday(): 1  
# isoweekday(): 2  
# isocalendar(): (2010, 14, 2)  
# isoformat(): 2010-04-06

#date����ĳЩ�������������أ����������Ƕ����ڽ�������һЩ������
#date2 = date1 + timedelta  # ���ڼ���һ�����������һ���µ����ڶ���timedelta����������ܣ���ʾʱ������
#date2 = date1 - timedelta   # ���ڸ�ȥ���������һ���µ����ڶ���
#timedelta = date1 - date2   # �����������������һ��ʱ��������
#date1 < date2  # �������ڽ��бȽ�
now = date.today()  
tomorrow = now.replace(day = 7 )  
delta = tomorrow - now  
print   'now:' , now,  ' tomorrow:' , tomorrow  
print   'timedelta:' , delta  
print  now + delta  
print  tomorrow > now  
  
# # ---- ��� ----   
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
  
# # ---- ��� ----  
# now: 2010-04-06  tomorrow: 2010-04-07  
# timedelta: 1 day, 0:00:00  
# 2010-04-07  
# True  

#Time��
   # time���ʾʱ�䣬��ʱ���֡����Լ�΢�����
from  datetime  import  *  
tm = time(23 ,  46 ,  10 )  
print   'tm:' , tm  
print   'hour: %d, minute: %d, second: %d, microsecond: %d'\
        % (tm.hour, tm.minute, tm.second, tm.microsecond)  
tm1 = tm.replace(hour = 20 )  
print   'tm1:' , tm1  
print   'isoformat():' , tm.isoformat()  
  
# # ---- ��� ----   
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
  
# # ---- ��� ----  
# tm: 23:46:10  
# hour: 23, minute: 46, second: 10, microsecond: 0  
# tm1: 20:46:10  
# isoformat(): 23:46:10

#datetime��
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
  
# ---- ��� ----   
# datetime.max: 9999-12-31 23:59:59.999999   
# datetime.min: 0001-01-01 00:00:00   
# datetime.resolution: 0:00:00.000001   
# today(): 2010-04-07 09:48:16.234000   
# now(): 2010-04-07 09:48:16.234000   
# utcnow(): 2010-04-07 01:48:16.234000  # �й�λ��+8ʱ�䣬�뱾��ʱ�����8   
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

  
# ---- ��� ----  
# datetime.max: 9999-12-31 23:59:59.999999  
# datetime.min: 0001-01-01 00:00:00  
# datetime.resolution: 0:00:00.000001  
# today(): 2010-04-07 09:48:16.234000  
# now(): 2010-04-07 09:48:16.234000  
# utcnow(): 2010-04-07 01:48:16.234000  # �й�λ��+8ʱ�䣬�뱾��ʱ�����8  
# fromtimestamp(tmstmp): 2010-04-07 09:48:16.234000  
# utcfromtimestamp(tmstmp): 2010-04-07 01:48:16.234000 

#��ʽ�ַ���
'''
��ʽ�ַ�  ����

%a ���ڵļ�д���� ������ΪWeb
%A ���ڵ�ȫд���� ������ΪWednesday
%b �·ݵļ�д����4�·�ΪApr
%B�·ݵ�ȫд����4�·�ΪApril 
%c:  ����ʱ����ַ�����ʾ�����磺 04/07/10 10:43:39��
%d:  ����������е�������������µĵڼ��죩
%f:  ΢�루��Χ[0,999999]��
%H:  Сʱ��24Сʱ�ƣ�[0, 23]��
%I:  Сʱ��12Сʱ�ƣ�[0, 11]��
%j:  �������е����� [001,366]���ǵ���ĵڼ��죩
%m:  �·ݣ�[01,12]��
%M:  ���ӣ�[00,59]��
%p:  AM����PM
%S:  �루��ΧΪ[00,61]��Ϊʲô����[00, 59]���ο�python�ֲ�~_~��
%U:  ���ڵ������������ĵڼ��ܣ�����������Ϊ�ܵĵ�һ��
%w:  ���������ܵ���������ΧΪ[0, 6]��6��ʾ������
%W:  ���ڵ�����������ǵ���ĵڼ��ܣ�������һ��Ϊ�ܵĵ�һ��
%x:  �����ַ������磺04/07/10��
%X:  ʱ���ַ������磺10:43:39��
%y:  2�����ֱ�ʾ�����
%Y:  4�����ֱ�ʾ�����
%z:  ��utcʱ��ļ�� ������Ǳ���ʱ�䣬���ؿ��ַ�����
%Z:  ʱ�����ƣ�����Ǳ���ʱ�䣬���ؿ��ַ�����
%%:  %% => %
'''
dt = datetime.now()  
print   '(%Y-%m-%d %H:%M:%S %f): ' , dt.strftime( '%Y-%m-%d %H:%M:%S %f' )  
print   '(%Y-%m-%d %H:%M:%S %p): ' , dt.strftime( '%y-%m-%d %I:%M:%S %p' )  
print   '%%a: %s '  % dt.strftime( '%a' )  
print   '%%A: %s '  % dt.strftime( '%A' )  
print   '%%b: %s '  % dt.strftime( '%b' )  
print   '%%B: %s '  % dt.strftime( '%B' )  
print   '����ʱ��%%c: %s '  % dt.strftime( '%c' )  
print   '����%%x��%s '  % dt.strftime( '%x' )  
print   'ʱ��%%X��%s '  % dt.strftime( '%X' )  
print   '���������ܵĵ�%s�� '  % dt.strftime( '%w' )  
print   '�����ǽ���ĵ�%s�� '  % dt.strftime( '%j' )  
print   '�����ǽ���ĵ�%s�� '  % dt.strftime( '%U' )
#04/01/13 09:00:00   20130401
print dt.strftime('%m/%d/%y  %H:%M:%S')
  
# # ---- ��� ----   
# (%Y-%m-%d %H:%M:%S %f):  2010-04-07 10:52:18 937000   
# (%Y-%m-%d %H:%M:%S %p):  10-04-07 10:52:18 AM   
# %a: Wed    
# %A: Wednesday    
# %b: Apr    
# %B: April    
# ����ʱ��%c: 04/07/10 10:52:18    
# ����%x��04/07/10    
# ʱ��%X��10:52:18    
# ���������ܵĵ�3��    
# �����ǽ���ĵ�097��    
# �����ǽ���ĵ�14��   
dt = datetime.now()  
print '(%Y-%m-%d %H:%M:%S %f): ', dt.strftime('%Y-%m-%d %H:%M:%S %f')  
print '(%Y-%m-%d %H:%M:%S %p): ', dt.strftime('%y-%m-%d %I:%M:%S %p')  
print '%%a: %s ' % dt.strftime('%a')  
print '%%A: %s ' % dt.strftime('%A')  
print '%%b: %s ' % dt.strftime('%b')  
print '%%B: %s ' % dt.strftime('%B')  
print '����ʱ��%%c: %s ' % dt.strftime('%c')  
print '����%%x��%s ' % dt.strftime('%x')  
print 'ʱ��%%X��%s ' % dt.strftime('%X')  
print '���������ܵĵ�%s�� ' % dt.strftime('%w')  
print '�����ǽ���ĵ�%s�� ' % dt.strftime('%j')  
print '�����ǽ���ĵ�%s�� ' % dt.strftime('%U')  
  
# # ---- ��� ----  
# (%Y-%m-%d %H:%M:%S %f):  2010-04-07 10:52:18 937000  
# (%Y-%m-%d %H:%M:%S %p):  10-04-07 10:52:18 AM  
# %a: Wed   
# %A: Wednesday   
# %b: Apr   
# %B: April   
# ����ʱ��%c: 04/07/10 10:52:18   
# ����%x��04/07/10   
# ʱ��%X��10:52:18   
# ���������ܵĵ�3��   
# �����ǽ���ĵ�097��   
# �����ǽ���ĵ�14��  

#----------------.���ַ�����ʱ��ת��Ϊʱ���---------------
a = "2013-10-10 23:40:00"
#����ת��Ϊʱ������
import time
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
#ת��Ϊʱ���:
timeStamp = int(time.mktime(timeArray))
timeStamp == 1381419600


#-------------��ʽ����---------------------------
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)

#---------------ʱ���ת��Ϊָ����ʽ����-------------------
timeStamp = 1381419600
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
otherStyletime == "2013-10-10 23:40:00"

'''
>>>import datetime
>>> d1 = datetime.datetime.now()
>>> d1.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:11:07'
>>> d2 = d1 + datetime.timedelta(seconds=10)#����10��
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:11:17'
>>> d2 = d1 + datetime.timedelta(minutes=10)#����10����
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:21:07'
>>> d2 = d1 + datetime.timedelta(hours=10)#����10Сʱ
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-03 03:11:07'
>>> d2 = d1 + datetime.timedelta(days=10)#����10��
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-12 17:11:07'
>>> d2 = d1 - datetime.timedelta(seconds=10)#��ȥ10��
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:11:57'
>>> d2 = d1 - datetime.timedelta(minutes=10)#����10����
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 17:01:07'
>>> d2 = d1 - datetime.timedelta(hours=10)#��ȥ10Сʱ
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-09-02 07:11:07'
>>> d2 = d1 - datetime.timedelta(days=10)#��ȥ10��
>>> d2.strftime("%Y-%m-%d %H:%M:%S")
'2013-08-23 17:11:07'
'''








