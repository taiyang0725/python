#-*- coding: utf8-*-
import os
import glob
import re
from string import *
import xlrd
import pyExcelerator as xlwd
import win32com.client

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
def readExcel(path,w):#com组件读取excel
    value_w=u''
    exit_list=[]
    try:
        app=win32com.client.Dispatch('Excel.Application')
        app.Visible=0
        active_filename=os.path.split(path)[1]
        app.Workbooks.Open(path)
        print path
        workSheet = app.Workbooks[0].Sheets[0]
        rows = workSheet.UsedRange.Rows.Count
        cols = workSheet.UsedRange.Columns.Count
        print w[0]
        for r in range(len(w)):
            for c in range(len(w[r])):
                value_w=w[r][c]#,16,22,28,32,37,38,42,50,53,99,113,135,182,193,205,219
                if c in [1,16,22,28,32,37,38,42,50,53,99,113,135,182,193,205,219]:
                    print r+3,c,value_w
                    #workSheet.Cells(r+3,c).Value=value_w
                #for r in [1]:
                    #print i+3,r,u'=============',value_w
                    #workSheet.Cells(i+3,r).Value=value_w#写'''
                        #pass
                         
           
        
    
            
            
    except Exception,msg:
        print unicode('异常','utf8'),msg
    finally:
        print '---------------------'
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
    rtn_map1={}
    for filename in path:
        Txt_filename=os.path.split(filename)[1]
        print '--->',Txt_filename
        if Txt_filename==u'-s(46).txt':
            read_txt_list =readTxt(filename)
            read_txt_list.pop(0)       
            if init_txt_map(rtn_map,read_txt_list,unicode(Txt_filename,'cp932'),length,title) is None:
                return None
        if Txt_filename==u'-w(37).txt':
            read_txt_list =readTxt(filename)
            read_txt_list.pop(0)       
            if init_txt_map(rtn_map1,read_txt_list,unicode(Txt_filename,'cp932'),length,title) is None:
                return None
    return rtn_map,rtn_map1

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

#-------------------------------------------------------
def processing_data(dict1,dict2):
    sList=[]
    wList=[]
    sList1=[]
    wList1=[]
    for key in dict1:
        lst=dict1[key][0]
        sList.append(lst)
    
    for key in dict2:
        lst=dict2[key][0]
        wList.append(lst)
        
    for i in range(len(sList)):
        isExists=False
        for j in range(len(wList)):
            if sList[i][0]==wList[j][0]:
                wList1.append(wList[j])
                isExists=True
                break    
            else:
                 pass
        if  isExists:
            sList1.append(sList[i])
            
    return merge_data(sList1,wList1)
    
    
def merge_data(lst,lst1):
   # print lst1
    final_list=[]
    for i in range(len(lst)):
        final_list.extend(lst[i][:6])
        final_list.append(u'')
        final_list.append(find_point(lst[i][6]))
        final_list.extend(lst[i][7:10])
        final_list.append(find_point(lst[i][10]))
        continue
        
    
    print final_list
    
        
    
    
    
            
           
            
        
        
   
            
         
        
#-------------------------------------------------------
def find_point(strs):
    if strs.find('.')==-1:
        return strs
    else:
        return str(99)


def find_slash(strs):

    if strs.find('/')==-1:
        return
    a=strs.split('/')
    if len(a)!=2:
        return
    b=a[0]
    c=a[1]
    return b,c
    
def insert_one_zero(strs,length):
    lst=[]
    if len(strs)<length:
        for i in range(length-len(strs)):
            lst.append(u'')
        for i in range(len(strs)):
            lst.append(strs[i])    
        return lst
    
    if len(strs)==length:
        for i in range(len(strs)):
            lst.append(strs[i])    
        return lst
    
    if  len(strs)>length:
        for i in range(length):
            lst.append(u'')
        return lst
   
def insert_one_zero1(strs,length):
    lst=[]
    if strs.find('.')>-1:
        st=strs.split('.')
        for i in range(len(st)):
            if re.findall(u'^[0-9]+$',st[i]):
                lst.insert(int(st[i]),'1')
            
    






















#-------------------------------------------------------    

def doWork():
    global active_filename
    w_list=[]
    
    cwd=os.getcwd()
    txt_map,txt_map1=read_txt_content(cwd+'/*.txt',u'part-s',0)#返回字典
    if txt_map is None:
        return
    
    processing_data(txt_map,txt_map1)
    
    
    
    path=glob.glob(cwd+'/*.xls')
    path.sort()

    for filename in path:
        active_filename=os.path.split(filename)[1]
        #print filename
        #readExcel(filename,w_list)
    
        
        
if __name__=='__main__':
    doWork()
    
'''    
    try:
        doWork()
    except:
        print 'File Error!'
    raw_input('Please input end!!!')
'''
