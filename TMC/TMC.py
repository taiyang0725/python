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
    #print len(lst)
    try:
        app=win32com.client.Dispatch('Excel.Application')
        app.Visible=0
        active_filename=os.path.split(path)[1]
        app.Workbooks.Open(path)
        workSheet = app.Workbooks[0].Sheets[0]
        for r in range(len(lst)):
            for c in range(len(lst[r])):
                workSheet.Cells(r+3,c+1).Value=lst[r][c]
              
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
    mapW={}
    mapS={}
    mapBs={}
    mapBw={}
    for filename in path:
        Txt_filename=os.path.split(filename)[1]
        print '--->',Txt_filename
        if Txt_filename.split('-')[1]==u'w.txt':
            read_txt_list =readTxt(filename)
            read_txt_list.pop(0)       
            if init_txt_map(mapW,read_txt_list,unicode(Txt_filename,'cp932'),length,title) is None:
                return None
            
        if Txt_filename.split('-')[1]==u's.txt':
            read_txt_list =readTxt(filename)
            read_txt_list.pop(0)       
            if init_txt_map(mapS,read_txt_list,unicode(Txt_filename,'cp932'),length,title) is None:
                return None

        if Txt_filename.split('-')[1]==u'bs.txt':
            read_txt_list =readTxt(filename)
            read_txt_list.pop(0)       
            if init_txt_map(mapBs,read_txt_list,unicode(Txt_filename,'cp932'),length,title) is None:
                return None

        if Txt_filename.split('-')[1]==u'bw.txt':
            read_txt_list =readTxt(filename)
            read_txt_list.pop(0)       
            if init_txt_map(mapBw,read_txt_list,unicode(Txt_filename,'cp932'),length,title) is None:
                return None
    return mapW,mapS,mapBs,mapBw

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
def processing_data(mapW,mapS,mapBs,mapBw):
    wList=[]
    sList=[]
    bsList=[]
    bwList=[]
   
    bwLists=[]
    lsts=[]
    lstsh=[]
    
    for key in mapW:
        lst=mapW[key][0]
        wList.append(lst)
    
    for key in mapS:
        lst=mapS[key][0]
        sList.append(lst)

    for key in mapBs:
        lst=mapBs[key][0]
        bsList.append(lst)

    for key in mapBw:
        lst=mapBw[key][0]
        bwList.append(lst)
    
    for i in range(len(bwList)):
        bwLists=bwList[i]
    
        for j in range(len(wList)):
            #print len(wList[i])
            if bwList[i][0]==wList[j][0]:
                bwLists.extend(wList[j])
                
        for j in range(len(sList)):
            #print len(sList[i])
            if bwList[i][0]==sList[j][0]:
                bwLists.extend(sList[j])
                    
        for j in range(len(bsList)):
            #print len(bsList[i])
            if bwList[i][0]==bsList[j][0]:
                bwLists.extend(bsList[j])
       
        if len(bwLists)==25:
            lsts.append(bwLists)
        else:
            lstsh.append(bwLists)
            
    lsts=sorted(lsts, key=lambda lsts: lsts[0])     
    lstsh=sorted(lstsh, key=lambda lstsh: lstsh[0])
    return merge_data(lsts,lstsh)
    
def merge_data(lsts,lstsh):
    lists=[]
    listsh=[]
    
    if 4>3:
        for i in range(len(lsts)):
            lists.append(lsts[i][0])
            lists.extend(lsts[i][1:5])
            lists.extend(lsts[i][5:])

        for j in range(len(lstsh)):
            #print lstsh[j],len(lstsh[j])
            listsh.extend(lstsh[j])
            listsh.append('cike')
        
    return lists,len(lsts),listsh,len(lstsh)        
       
            
                    
#-------------------------------------------------------    

def doWork():
    global active_filename
    lists=[]
    data_list=[]
    l=0

    listsh=[]
    data_listh=[]
    lh=0
    
    cwd=os.getcwd()
    mapW,mapS,mapBs,mapBw=read_txt_content(cwd+'/*.txt',u'part-s',0)#返回字典                                    
    if mapW is None or mapS is None or mapBs is None or mapBw is None:
        return
    '''
    for key in mapBw:
        print mapBw[key]

    [u'141219FA1-0002.jpg', u'', u'', 'wangan',============>bw------------3
    u'141219FA1-0002.jpg', u'\u4e2d\u897f', u'\u4e45\u5b50', u'\u306a\u304b\u306b\u3057',==========>w-------9
               u'\u3072\u3055\u3053', u'5640012', u'\u5927\u962a\u5e9c\u5439\u7530\u5e02\u5357\u6b63\u96c02-37-2',
               u'', u'\u25a0i7777@ezweb.ne.jp', 'wangan',
    u'141219FA1-0002.jpg', u'73', u'5', u'9', u'2', u'', u'08053125045', u'', 'wangan',==========>s------8
    u'141219FA1-0002.jpg', u'', u'', u'', u'']============> bs---------5
    '''
        
    lists,l,listsh,lh=processing_data(mapW,mapS,mapBs,mapBw)

    for i in range(l):
        data_list.append(lists[(len(lists)*i)/l:(len(lists)*(i+1))/l])

    for i in range(lh):
        data_listh.append(listsh[(len(listsh)*i)/lh:(len(listsh)*(i+1))/lh])

    data_list.extend(data_listh)
    data_list=sorted(data_list, key=lambda data_list: data_list[0])
    
    for c in range(len(data_list)):
        print '\n*bw*',data_list[c][:3],'\n*w*',data_list[c][3:11],'\n*s*',data_list[c][12:19],'\n*bs*',data_list[c][20:]
        #print data_list[c]
        
        
    path=glob.glob(cwd+'/*.xls')
    path.sort()

    for filename in path:
        active_filename=os.path.split(filename)[1]
        #readExcel(filename,data_list)
    
        
        
if __name__=='__main__':
    
    doWork()
    
    '''    
    try:
        doWork()
    except:
        print 'File Error!'
    '''
    raw_input('Please input end!!!')

