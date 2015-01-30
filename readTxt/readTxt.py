#-*- coding: utf8-*-
import os
import glob
import re
from string import *
import xlrd
import pyExcelerator as xlwd
import win32com.client
from datetime import datetime
from datetime import timedelta
import time


def to_unicode( s ):
    rtn = u''
    try:
        rtn = unicode(s,'cp932')
    except:
        try:
            rtn = unicode(s,'utf8')
        except:
            try:
                rtn = unicode(s,'utf16')
            except:
                return unicode(s,'cp936')
    return rtn
#---------------读excel---------------------
def readExcel(path,txt_dict):#com组件读取excel
    exit_list=[]
    try:
        app=win32com.client.Dispatch('Excel.Application')
        app.Visible=0
        active_filename=os.path.split(path)[1]
        app.Workbooks.Open(path)
        workSheet = app.Workbooks[0].Sheets[0]
        rows = workSheet.UsedRange.Rows.Count
        cols = workSheet.UsedRange.Columns.Count
        
        #print txt_dict
        for i in range(2,rows):
            #print workSheet.Cells(i,3).Value
            key1=(str(workSheet.Cells(i,2).Value)).replace(" ", "")#读
            #print key1
            if txt_dict.has_key(key1):
                workSheet.Cells(i,3).Value=txt_dict[key1]#写
                exit_list.append(txt_dict[key1])
            #print '.',
            print unicode('等待：','utf8'),'===>',i
            if len(exit_list)==len(txt_dict):
                break
            
    except Exception,msg:
        print unicode('异常','utf8'),msg
    finally:
        app.DisplayAlerts=False
        app.ActiveWorkbook.Close(SaveChanges=1)    
        app.Quit()
        app = None
       

#---------------读txt---------------------
def readTxt(filepath,code=1):
    sz = os.stat(filepath).st_size
    ifn = open(filepath,'rb')
    count = 0
    buf = ifn.read( sz )
    ifn.close
    if code==1:
        buf=to_unicode(buf)
    else:
        buf=unicode(buf,'utf16')
    ret_list=buf.split(u'\r\n')
    while len(ret_list[-1])==0:
        ret_list.pop(-1)
    
    return ret_list


def read_txt_content(path,title,length):
    print u'-------------'+title+u'-------------'
    path=glob.glob(path)
    path.sort()
    rtn_map={}
    for filename in path:
        Txt_filename=os.path.split(filename)[1]
        print '--->',Txt_filename
        read_txt_list =readTxt(filename)
        read_txt_list.pop(0)       
        if init_txt_map(rtn_map,read_txt_list,unicode(Txt_filename,'cp932'),length,title) is None:
            return None
    return rtn_map

def init_txt_map(maps,content_list,filename,length,title):
    for item in content_list:
       if len(item.strip())==0:
           continue
       temp = item.split('\t')
       if len(temp)<length:
           print '--->',filename,temp[0],'length is not ',length
           return None
       key=u'\\'.join(temp[0].split(u'\\')[-2:])
       if maps.has_key(key):
           maps[key].append(temp)
       else:
           maps[key]=[temp]
    return 0;

#---------------data_init---------------------


def get_data_dict(init_data,r1,r2,r3):#初始化数据，生成字典,key:时间
    data_dict={}
    for key0 in init_data:
        data=init_data[key0]
        for i in range(len(data)):
            t=time.strptime(data[i][r1],'%Y%m%d')#字符串转换为时间
            t_datetime=datetime(*t[:3])
            
            keyT=t_datetime+timedelta(hours=9)
            keyT1=keyT+timedelta(minutes=30)
            
            key=(keyT+timedelta(hours=i)).strftime('%m/%d/%y  %H:%M:%S')
            key=key.replace(" ", "")
            
            key1=(keyT1+timedelta(hours=i)).strftime('%m/%d/%y  %H:%M:%S')
            key1=key1.replace(" ", "")

            if data_dict.has_key(key):
                data_dict[key].append(data(i)[r2])
            else:
                data_dict[key]=[data[i][r2]]

            if data_dict.has_key(key1):
                data_dict[key1].append(data(i)[r3])
            else:
                data_dict[key1]=[data[i][r3]]

    return data_dict

def  get_data(init_data):#字典的合并
    data_dict={}
    dict1={}
    dict2={}
    dict3={}

    dict1=get_data_dict(init_data,1,2,3)
    dict2=get_data_dict(init_data,4,5,6)
    dict3=get_data_dict(init_data,7,8,9)
    
    dictMerged3 = dict1.copy()
    dictMerged3.update( dict2 )
    
    data_dict = dictMerged3.copy()
    data_dict.update( dict3 )

    #print data_dict
    return data_dict


#---------------com组件写入数据----------------------------

def write_data(cwd,dict1,list1,name):
    try:
        app=win32com.client.Dispatch('Excel.Application')
        app.Visible=0
        workbook=app.Workbooks.Open(cwd+'b.xls')
        workSheet = workbook.Sheets(1)
        for i in range(len(list)):
            workSheet.Cells(i+2,3).Value=list[i]
            
    except Exception,msg:
        print msg
    finally:
        app.ActiveWorkbook.Close(SaveChanges=1)    
        app.Quit()
        app = None

#-------------------------------------------------------    

def doWork():
    global active_filename
    
    cwd=os.getcwd()
    txt_map=read_txt_content(cwd+'/*.txt',u'part-s',0)#返回字典
    if txt_map is None:
        return
    
    txt_dict=get_data(txt_map)
    if txt_dict is None:
        return

    path=glob.glob(cwd+'/*.xls')
    path.sort()

    for filename in path:
        active_filename=os.path.split(filename)[1]
        readExcel(filename,txt_dict)
        
        
if __name__=='__main__':
    doWork()
    raw_input('Please input end!!!')

'''    
    try:
        doWork()
    except:
        print 'File Error!'
    raw_input('Please input end!!!')
'''
