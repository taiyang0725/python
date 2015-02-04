#-*- coding: utf8-*-
#################################################################
# Author     :An                                            
# Version    : 1.0.0.0                                         
# Date       : 2015-2-4                                      
# Description:                                                 
#################################################################
import os
import glob
import re
from string import *
import xlrd
import pyExcelerator as xlwd
import win32com.client
import xlwt


count_list=[]
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
#-------------------------------------------------------    

def doWork():
    global active_filename
    lst=[]
    lst0=[]
    a=0
    b=0
    
    a1=0
    b1=0
    
    
    cwd=os.getcwd() 
    path=glob.glob(cwd+'/*.txt')
    path.sort()
    rtn_map={}
    for filename in path:
        Txt_filename=os.path.split(filename)[1]
        print '--->',Txt_filename
        lists =readTxt(filename)
        lists.pop(0)
        
        for i in range(len(lists)):
             data=lists[i].split('\t')
             try:
               lst.append(data[2])
               lst.append(data[5])
               lst.append(data[8])
               lst.remove(u'')
             except:
                pass
             try:
               lst0.append(data[3])
               lst0.append(data[6])
               lst0.append(data[9])
               lst0.remove(u'')
              
             except:
                pass
             
        #print len(lst),len(lst0)
        
        if a!=0:
           b=len(lst)-a
        else:
            b=len(lst)
        a=len(lst)
        
        if a1!=0:
           b1=len(lst0)-a1
        else:
            b1=len(lst0)
        a1=len(lst0)

        count_list.append([unicode(Txt_filename,'cp932'),b,b1])

        if len(count_list)>0:
            write(cwd,count_list,[u'文本名字',u'整点',u'半点'],'report.xls')
        
#-------------------------------------------------------            
        
def write(cwd,list1,table_title,name):
    
    book=xlwt.Workbook(encoding='utf-8')

    alignment=xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    style=xlwt.XFStyle()
    style.alignment = alignment
    
    sheet=book.add_sheet('count')
    sheet.col(0).width = 8000

    for i in range(len(table_title)):
        sheet.write(0,i,table_title[i],style)
   
    for r in range(len(list1)):
        for c in range(len(list1[r])):
            sheet.write(1+r,c,list1[r][c],style)     

    book.save(cwd+'\\'+name)    
if __name__=='__main__':
    doWork()
    raw_input('Please input end!!!')


