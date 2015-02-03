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
def readExcel(path,lst):#com组件读取excel
    print len(lst)
    try:
        app=win32com.client.Dispatch('Excel.Application')
        app.Visible=0
        active_filename=os.path.split(path)[1]
        app.Workbooks.Open(path)
        workSheet = app.Workbooks[0].Sheets[0]
        rows = workSheet.UsedRange.Rows.Count
        cols = workSheet.UsedRange.Columns.Count
        
        for r in range(len(lst)):
            #print lst[r]
            pass
            #workSheet.Cells(3,r).Value=lst[r]
                
                    
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
    lists=[]
    list=[]
    
    print len(lst)
    print len(lst1)
    for i in range(len(lst)):
        if 4>3:
            lists.extend(lst[i][:6])
            lists.append(u'')
            lists.append(find_point(lst[i][6]))
            lists.extend(lst[i][7:10])
            lists.append(find_point(lst[i][10]))
            lists.extend(insert_one_zero(lst[i][11],3))
            lists.append(lst1[i][1])#===>w1
            lists.extend(insert_one_zero(lst[i][12],5))
            lists.append(lst1[i][2])#===>w2
            lists.extend(insert_one_zero(lst[i][13],5))
            lists.append(lst1[i][3])#===>w3
            lists.extend(insert_one_zero(lst[i][14],3))
            lists.append(lst1[i][4])#===>w4
            lists.extend(insert_one_zero(lst[i][15],4))
            lists.extend(lst1[i][5:7])#===>w5-6
            lists.append(u'')
            lists.extend(lst[i][16:18])
            lists.extend(lst1[i][7])#===>w7
            lists.append(u'')
            lists.append(lst[i][18])
            lists.extend(find_point1(lst[i][19:24]))
            lists.append(lst1[i][8])#===>w8
            lists.append(u'')
            lists.append(find_point(lst[i][24]))
            lists.append(lst1[i][9])#===>w9
            lists.extend(insert_one_null(lst[i][25],5))
            lists.extend(insert_one_null(lst[i][26],5))
            lists.extend(insert_one_null(lst[i][27],5))
            lists.extend(insert_one_null(lst[i][28],4))
            lists.append(find_point(lst[i][29]))
            lists.extend(insert_one_zero(lst[i][30],25))
            lists.append(lst1[i][10])#===>w10
            lists.append(u'')
            lists.extend(find_point1(lst[i][31:35]))
            lists.extend(insert_one_zero(lst[i][35],8))
            lists.append(lst1[i][11])#===>w11
            lists.append(u'')
            lists.extend(find_point1(lst[i][36:40]))
            lists.append(u'')
            lists.extend(find_point1(lst[i][40:46]))
            lists.extend(insert_one_zero(lst[i][46],8))
            lists.append(find_point(lst[i][47]))
            lists.append(lst1[i][12])#===>w12
            lists.extend(find_point1(lst[i][48:50]))
            lists.append(u'')
            for j in range(50,61):
                lists.extend(find_slash(lst[i][j]))
            lists.extend(insert_one_null(lst[i][61],3))
            lists.append(u'')
            lists.extend(insert_one_null(lst[i][62],5))
            lists.append(u'')
            lists.extend(find_point1(lst[i][63:65]))
            lists.extend(insert_one_zero(lst[i][65],9))
            lists.append(lst1[i][13])#===>w13
            lists.extend(find_point1(lst[i][66:68]))
            lists.extend(insert_one_zero(lst[i][68],8))
            lists.append(lst1[i][14])#===>w14
            lists.extend(find_point1(lst[i][69:71]))
            lists.extend(insert_one_zero(lst[i][71],9))
            lists.append(lst1[i][15])#===>w15
            lists.append(find_point(lst[i][72]))
            lists.extend(insert_one_zero(lst[i][73],12))
            lists.append(lst1[i][16])#===>w16
            lists.extend(find_point1(lst[i][74:77]))
            lists.append(u'')
            lists.extend(find_point1(lst[i][77:80]))
            lists.append(u'')
            break
        
   
    
        
    return lists
            
#-------------------------------------------------------
def find_point(strs):
    if strs.find('.')==-1:
        return strs
    else:
        return str(99)
    
def find_point1(list):
    for i in range(len(list)):
        if list[i].find('.')>-1:
            list[i]=u'99'

    return list



def find_slash(strs):
    lst=[u'',u'']
    if strs.find('/')==-1:
        return lst
    
    a=strs.split('/')
    if len(a)!=2:
        return lst
    
    if a[0]!=u'*' and a[1]!=u'*':
        return [a[0],a[1]]

    if a[0]==u'*' and a[1]!=u'*':
        return [u'99',a[1]]

    if a[1]==u'*' and a[0]!=u'*':
        return [a[0],u'99']

    if a[1]==u'*' and a[0]==u'*':
        return [u'99',u'99']
    
def insert_one_null(strs,length):
    lst=[]
    if len(strs)<length:
        for i in range(length-len(strs)):
            lst.append(u'')
            
        for i in range(len(strs)):
            lst.append(strs[i])

        for i in range(len(lst)):
            if lst[i]==u'0':
               lst[i]=u''
               
        return lst
    
    if len(strs)==length:
        for i in range(len(strs)):
            lst.append(strs[i])

        for i in range(len(lst)):
            if lst[i]==u'0':
               lst[i]=u''
               
        return lst
    
    if  len(strs)>length:
        for i in range(length):
            lst.append(u'')
        return lst
   
def insert_one_zero(strs,length):
    lst=[]
    for i in range(length):
            lst.append(u'0')
            
    if strs.find('.')>-1:    
        st=strs.split('.')   
        for i in range(len(st)): 
            try:
                lst.pop(int(st[i])-1)
                lst.insert(int(st[i])-1,'1')    
            except:
                return lst
        return lst
    
    else:
        for i in range(len(strs)): 
            try:
                lst.pop(int(strs[i])-1)
                lst.insert(int(strs[i])-1,'1')    
            except:
                return lst
        return lst  
        
#-------------------------------------------------------    

def doWork():
    global active_filename
    lists=[]
    
    cwd=os.getcwd()
    txt_map,txt_map1=read_txt_content(cwd+'/*.txt',u'part-s',0)#返回字典
    if txt_map is None:
        return
    
    lists=processing_data(txt_map,txt_map1)
    print len(lists)
    
    
    path=glob.glob(cwd+'/*.xls')
    path.sort()

    for filename in path:
        active_filename=os.path.split(filename)[1]
        
        #readExcel(filename,lists)
    
        
        
if __name__=='__main__':
    doWork()
    
'''    
    try:
        doWork()
    except:
        print 'File Error!'
    raw_input('Please input end!!!')
'''
