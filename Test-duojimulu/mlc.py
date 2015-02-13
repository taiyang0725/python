#-*- coding:utf8-*-
#################################################################
# Author     :An
# Version    : 1.0.0.1
# Date       : 2015-1-15
# Description: 
#################################################################
import os
import glob
import re
from string import *
import pyExcelerator as xlwd
import win32com.client
import xlrd
import datetime


error_list=[]
def to_unicode( s ):
    rtn = u''
    try:
        rtn = unicode(s,'utf8')
    except:
        try:
            rtn = unicode(s,'cp932')
        except:
            try:
                rtn = unicode(s,'utf16')
            except:
                return unicode(s,'cp936')
    return rtn

def get_col_value(value):
    if value is None:
        return u''
    if isinstance(value,float):
        value = getstr(str(value))
    if not isinstance(value,unicode):
        value = str(value).strip(' ')
        value = to_unicode(value)
    return value

def readXls(path):
    rtn_list=[]
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    for r in range(1,rows):
        row = []
        for c in range(cols):
            val = sheet.cell_value(r,c)
            val =get_col_value(val)
            row.append(val)
        rtn_list.append(row)
    return rtn_list

def getstr(strs):
    tt = strs.split(u'.')
    if len(tt)==2:
       if tt[1]==u'0':
           return tt[0]
       else:
           return strs
    else:
        return strs

def getColumn(index):
    if (index/26)==0:
        return unichr(65+index)
    mod = index%26
    return unichr(65+index/26-1)+unichr(65+mod)

#-----------------------------------------------------------------------

#error_list.append([unicode(active_filename,'cp932'),g_image,g_line,col,u'此列不一致'])
                
        
            
def do_check_item(baseList,list):
    
    global g_image,g_line,g_code
    g_code=u''
    g_image=u''
    for i in range(len(list)):
        temp=list[i]
        g_line=i+2
        g_image=temp[0]
        
        
def read_content(path,cwd):

    for filename in path:
        base_filename=os.path.split(filename)[1]
        print '==> read base file'
        base_list = readXls(filename)
        
    for folder in os.listdir(cwd):
        
        if os.path.isdir(cwd+'/'+folder):
            path=glob.glob(cwd+'/'+folder+'/*.xls')
            path.sort()
            for filename in path:
                active_filename=os.path.split(filename)[1]
                 
                print '==>',active_filename.split('_')[1:]
                readList=readXls(filename)
                  
                
    
        
def doWork():
    global active_filename
    readList=[]
    readList1=[]
    base_list=[]
    
    cwd=os.getcwd()
    if os.path.isfile(cwd+'\\report.xls'):
      os.remove(cwd+'\\report.xls')
      
    path=glob.glob(cwd+"/*.xls")
    path.sort()
    
    #read_content(path,cwd)
    
    for folder in os.listdir(cwd):
        print '====>',folder
        if os.path.isdir(cwd+'/'+folder):
            path=glob.glob(cwd+'/'+folder+'/*.xls')
            path.sort()
            for filename in path:
                active_filename=os.path.split(filename)[1]
                print '===>',active_filename   
                readList=readXls(filename)
                error_list.append([unicode(active_filename,'cp932'),len(readList)])
             

    if len(error_list)>0:
        write(cwd,error_list,[u'name',u'much'],'report.xls')

def write(cwd,list1,table_title,name):
    wb = xlwd.Workbook()
    xlwd.UnicodeUtils.DEFAULT_ENCODING ='cp932'
    ws = wb.add_sheet('sheet')
    for i in range(len(table_title)):
        ws.write(0,i,table_title[i])
        
    for r in range(len(list1)):
        temp_item = list1[r]
        for c in range(len(temp_item)):
            temp=temp_item[c]
            ws.write(r+1,c,temp)
    wb.save(cwd+'\\'+name)

if __name__=='__main__':

    doWork()
    #try:
     #   doWork()
    #except:
     #   print 'File Error!'
    raw_input('Please input end!!!')

