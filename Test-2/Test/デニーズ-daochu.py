#-*- coding: utf8-*-
import os
import glob
import re
from string import *
import xlrd
import pyExcelerator as xlwd
import win32com.client
import xlwt

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

def getColumn(index):
    if (index/26)==0:
        return unichr(65+index)
    mod = index%26
    return unichr(65+index/26-1)+unichr(65+mod)

#---------------写excel---------------------
def readExcel(path,lst):#com组件读取excel
    
    try:
        app=win32com.client.Dispatch('Excel.Application')
        app.Visible=0
        active_filename=os.path.split(path)[1]
        app.Workbooks.Open(path)
        workSheet = app.Workbooks[0].Sheets[0]
        for r in range(len(lst)):
            for c in range(len(lst[r])):
                workSheet.Cells(r+9,c+11).Value=lst[r][c]
              
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


def read_txt_content(cwd,title,length):
    print u'-------------'+title+u'-------------'
    mapW={}
    mapS={}
    mapZS={}
    mapZW={}
    for folder in os.listdir(cwd):
        print folder
        if folder==u'-s':
            if os.path.isdir(cwd+'/'+folder):
                path=glob.glob(cwd+'/'+folder+'/*')
                path.sort()
                for filename in path:
                    active_filename=unicode(filename,'cp932').split(u'\\')[-1]
                    #print '==>',active_filename
                    read_txt_list =readTxt(filename)
                    read_txt_list.pop(0)       
                    if init_txt_map(mapS,read_txt_list,active_filename,length,title) is None:
                       return None

        if folder==u'-w':
            if os.path.isdir(cwd+'/'+folder):
                path=glob.glob(cwd+'/'+folder+'/*')
                path.sort()
                for filename in path:
                    active_filename=unicode(filename,'cp932').split(u'\\')[-1]
                    #print '==>',active_filename
                    read_txt_list =readTxt(filename)
                    read_txt_list.pop(0)    
                    if init_txt_map(mapW,read_txt_list,active_filename,length,title) is None:
                       return None

        
    return mapW,mapS
     
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
def processing_data(mapW,mapS):#mapS,mapW
    wList=[]
    sList=[]

    wLists=[]
   

    lsts=[]
    lstsh=[]
   
    
    for key in mapW:
        lst=mapW[key][0]
        wList.append(lst)
    
    for key in mapS:
        lst=mapS[key][0]
        sList.append(lst)

    
    
    for i in range(len(wList)):
        #print len(wList[i]),6
        wLists=wList[i]
        for j in range(len(sList)):
            #print len(sList[i]),30
            if wList[i][0]==sList[j][0]:
                
                wLists.extend(sList[j])
                
       
        
        if len(wLists)==36:
            lsts.append(wLists)
        else:
            lstsh.append(wLists)
            
    lsts=sorted(lsts, key=lambda lsts: lsts[0][5:9])     
    
    return merge_data(lsts)
    
def merge_data(lsts):
    
    
    '''
    for i in range(len(lsts)):
         print lsts[i],len(lsts[i])

    
    0 + ﻿Image, 1 + Q16_郵便番号1, 2 + Q16_郵便番号2, 3 + Q16_丁目1, 4 + Q16_住所, 5 + Q16_丁目2,
          3.1415 926  5358 9793    3.1415926 5358 9793
    6 + ﻿Image, 7 + サンプル, 8 + Q1, 9 + Q1_その他, 10 + Q2, 11 + Q3, 12 + Q3_その他, 13 + Q4, 14 + Q5,
    15 + Q6, 16 + Q7_人数, 17 + Q7_一緒に来店, 18 + Q8_女性_1-7, 19 + Q8_男性_1-7, 20 + Q8_女性_8-14,
    21 + Q8_男性_8-14, 22 + Q9, 23 + Q9_その他, 24 + Q10_1-4, 25 + Q10_5-8, 26 + Q11, 27 + Q12,
    28 + Q12_その他, 29 + Q13, 30 + Q14, 31 + Q14SQ, 32 + Q15, 33 + 店番, 34 + 利用日, 35 + 時間帯
    
    '''

    lists=[]
    if 4>3:
        for i in range(len(lsts)):
            
            lists.append(lsts[i][0])
            lists.append(set_l(lsts[i][7],7))#L
            lists.extend(lsts[i][8:16])
            lists.append(set_l(lsts[i][16],2))#U
            lists.append(lsts[i][17])
            lists.extend(find_num_what(lsts[i][18],7))
            lists.extend(find_num_what(lsts[i][19],7))
            lists.extend(find_num_what(lsts[i][20],7))
            lists.extend(find_num_what(lsts[i][21],7))
            lists.extend(lsts[i][22:24])
            lists.extend(set_Q10(lsts[i][24],4))
            lists.extend(set_Q10(lsts[i][25],4))
            lists.extend(lsts[i][26:33])
            lists.extend(lsts[i][1:4])
            lists.append(strB2Q(lsts[i][4]))
            lists.append(lsts[i][5])
            lists.append(set_l(lsts[i][33],4))#BU
            lists.extend(lsts[i][34:36])
            
            #lists.append(lists)
            
            
        
                         
        return lists,len(lsts) 
       
            
                    
#-------------------------------------------------------
def set_l(strs,l):
    lists=[]
    if 4>3:
        if len(strs)>l:
            return strs
        else:
            for i in range(l-len(strs)):
                lists.append(u'0')
            for i in range(len(strs)):
                lists.append(strs[i])
            return u''.join(lists)

def set_Q10(strs,l):
    lsts=[]
    if 4>3:
        s=strs.split('.')
        for i in range(len(s)):
            if s[i]==u'0':
                s[i]=u''
            if len(s[i])>1:
                for j in range(len(s[i])):
                    lsts.append(s[i][j])
                    lsts=sorted(lsts, key=lambda lsts: lsts[0])
                s[i]=u''.join(lsts)
        if len(s)==l:
            return s
        if len(s)<l:
            for i in range(l-len(s)):
                s.append(u'')
            return s
        if len(s)>l:
            return s[:l]

def strB2Q(ustring):
    """半角转全角"""
    if ustring==u'':
        return u''
    
    rstring = u''
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 32:                                 #半角空格直接转化                  
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:        #半角字符（除空格）根据关系转化
            inside_code += 65248

        rstring += unichr(inside_code)
    return rstring


def find_xing(lst):
    lsts=[]
    for i in range(len(lst)):
        if lst[i].find('*')>-1:
            lsts.append(getColumn(i+11)+u'9')
    return u','.join(lsts)        
            
def find_num_what(strs,l):
    lst=[]
    lse=[]
    ls=strs.split(',')
    for i in range(l):
       lst.append(u'')
    for i in range(len(ls)):
       if ls[i]!=u'':
           try:
              lse=ls[i].split('/')
              lst.pop(int(lse[0])-1)
              lst.insert(int(lse[0])-1,lse[1])
           except:
               pass
    return lst
   
   
    

    
#-------------------------------------------------------

#-------------------------------------------------------    

def doWork():
    global active_filename
    lists=[]
    data_list=[]
    l=0

    cwd=os.getcwd()
    path=glob.glob(cwd+'/*.xls')
    path.sort()

    mapW,mapS=read_txt_content(cwd,u'part-s',0)#返回字典                                    
    if mapW is None or mapS is None :
        return
     
    lists,l=processing_data(mapW,mapS)
    
    for i in range(l):
        data_list.append(lists[(len(lists)*i)/l:(len(lists)*(i+1))/l])

    for c in range(len(data_list)):
        #print data_list[c],len(data_list[c]),len(data_list)
        pass
        
    for filename in path:
        active_filename=os.path.split(filename)[1]
        readExcel(filename,data_list)
    

   
             
if __name__=='__main__':
    
    doWork()
    
    '''    
    try:
        doWork()
    except:
        print 'File Error!'
    '''
    raw_input('Please input end!!!')

