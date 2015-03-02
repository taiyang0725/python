#-*- coding: utf8-*-
import os
import glob
import re
from string import *
import xlrd
import pyExcelerator as xlwd
import win32com.client
import xlwt

title_name=u'画像番号	資料番号1	資料番号2	指定番号	特別徴収人数	普通徴収人数	合計人数	支払者名称	資料番号1	資料番号2	住所カナコード	受給者番号	氏名カナ	支払金額	給与所得控除後に金額	所得税控除の額の合計額	源泉徴収税額	控除配偶者有無	老人配偶者有無	所得税配偶者特別控除額	特定扶養人数	扶養同居老人数	扶養老人数	その他扶養人数	同居特別障害人数	特別障害人数	その他障害人数	社会保険料等の金額	小規模共済（内書）	生命保険料の控除額	地震保険料の控除額	住宅借入金等特別控除の額	配偶者の合計所得	新生命保険料の金額	旧生命保険料の金額	介護医療保険料の金額	新個人年金保険料の金額	旧個人年金保険料の金額	旧長期損害保険料の金額	16歳未満扶養親族	未成年者	死亡退職	乙欄	本人特別障害	本人その他障害	寡婦一般	寡婦特別	寡夫	勤労学生	就職ビット	退職ビット	中途就退年月日	生年月日	前職給与支払額	普微希望	住宅借入金等特別控除可能額	居住開始年月日1	居住開始年月日2	年分	合算特徴フラグ	海外赴任・租税条約フラグ	訂正・無効フラグ	'.split('\t')
list4_name=u'項番	管理番号	資料番号(赤い番号)	画像ファイル名	項目	処理方法'.split('\t')

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
                workSheet.Cells(r+2,c+1).Value=lst[r][c]
              
    except Exception,msg:
        print unicode('异常','utf8'),msg
    finally:
        app.DisplayAlerts=False
        app.ActiveWorkbook.Close(SaveChanges=1)    
        app.Quit()
        app = None
       

#---------------读excel---------------------
def getColumn(index):
    if (index/26)==0:
        return unichr(65+index)
    mod = index%26
    return unichr(65+index/26-1)+unichr(65+mod)

def get_col_value(value):
    if value is None:
        return u''
    if isinstance(value,float):
        value = getstr(str(value))
    if not isinstance(value,unicode):
        value = str(value).strip(' ')
        value = to_unicode(value)
    return value

def readFiles(path):
    rtn_list=[]
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    for r in range(rows):
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

        if folder==u'-zs':
            if os.path.isdir(cwd+'/'+folder):
                path=glob.glob(cwd+'/'+folder+'/*')
                path.sort()
                for filename in path:
                    active_filename=unicode(filename,'cp932').split(u'\\')[-1]
                    #print '==>',active_filename
                    read_txt_list =readTxt(filename)
                    read_txt_list.pop(0)       
                    if init_txt_map(mapZS,read_txt_list,active_filename,length,title) is None:
                       return None

        if folder==u'-zw':
            if os.path.isdir(cwd+'/'+folder):
                path=glob.glob(cwd+'/'+folder+'/*')
                path.sort()
                for filename in path:
                    active_filename=unicode(filename,'cp932').split(u'\\')[-1]
                    #print '==>',active_filename
                    read_txt_list =readTxt(filename)
                    read_txt_list.pop(0)       
                    if init_txt_map(mapZW,read_txt_list,active_filename,length,title) is None:
                       return None
        if folder==u'base':
            if os.path.isdir(cwd+'/'+folder):
                path=glob.glob(cwd+'/'+folder+'/*')
                path.sort()
                for filename in path:
                    active_filename=unicode(filename,'cp932').split(u'\\')[-1]
                    read_list = readFiles(filename)
                    read_list.pop(0)
        
    return mapW,mapS,mapZS,mapZW,read_list
     
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
def processing_data(mapW,mapS,mapZs,mapZw,base_list):#mapS,mapW,mapZS,mapZW
    wList=[]
    sList=[]
    zsList=[]
    zwList=[]
   
    zwLists=[]
    lsts=[]
    lstsh=[]
    zsXing=[]
    
    for key in mapW:
        lst=mapW[key][0]
        wList.append(lst)
    
    for key in mapS:
        lst=mapS[key][0]
        sList.append(lst)

    for key in mapZs:
        lst=mapZs[key][0]
        zsList.append(lst)

    for key in mapZw:
        lst=mapZw[key][0]
        zwList.append(lst)
    
    for i in range(len(zwList)):
        #print len(zwList[i]),2
        zwLists=zwList[i]
    
        for j in range(len(wList)):
            #print len(wList[i]),3
            if zwList[i][0]==wList[j][0]:
                zwLists.extend(wList[j])
                
        for j in range(len(sList)):
            #print len(sList[i]),52
            if zwList[i][0]==sList[j][0]:
                zwLists.extend(sList[j])
                    
        for j in range(len(zsList)):
         
            if zwList[i][0]==zsList[j][0]:
                zwLists.extend(zsList[j])
        
        if len(zwLists)==64:
            lsts.append(zwLists)
        else:
            lstsh.append(zwLists)
            
    #lsts=sorted(lsts, key=lambda lsts: lsts[0])     
    
    return merge_data(lsts,base_list)
    
def merge_data(lsts,blsts):
    lists=[]

    list1=[]
    list4=[]
    '''
    zw,w,s,zs
    [u'10.1.0.246\\image\\image1\\\u4e16\u7530\u8c37\\20150107\\S010714003Y740\\00000001.jpg', u'\u82f1',===>ZW,2,1
    
     u'10.1.0.246\\image\\image1\\\u4e16\u7530\u8c37\\20150107\\S010714003Y740\\00000001.jpg', u'', u'',===>W,3,4
     
     u'10.1.0.246\\image\\image1\\\u4e16\u7530\u8c37\\20150107\\S010714003Y740\\00000001.jpg', u'', u'', u'3', u'', u'', u'6', u'', u'', u'',
              u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'',
              u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'', u'',===>S,52,56
              
    u'10.1.0.246\\image\\image1\\\u4e16\u7530\u8c37\\20150107\\S010714003Y740\\00000001.jpg', u'1400270434',
              u'0065012917', u'1', u'0', u'1', u'']=====>ZS,7,63
    '''
    if 4>3:
        for i in range(len(lsts)):
            
            lists.append(lsts[i][0].split('\\')[-1])#==>0
            lists.append(set_zs2_zs5(lsts[i][58][:2]))
            lists.append(set_zs2_zs5(lsts[i][58][2:]))
            lists.append(set_zs2_zs5(lsts[i][59]))
            lists.append(set_zs2_zs5(lsts[i][60]))
            lists.append(set_zs2_zs5(lsts[i][61]))
            lists.append(set_zs2_zs5(lsts[i][62]))
            lists.append(excel_zw1(lsts[i][1]))#===>1
            lists.append(lsts[i][6][:2])
            lists.append(lsts[i][6][2:])#s1
            lists.append(set_w1(lsts[i][3],blsts))#===>3
            lists.append(set_s2(lsts[i][7]))#s2,===>7
            lists.append(excel_w2(lsts[i][4]))#w2,3,38,====>4
            lists.extend(lsts[i][8:44])#s38
            lists.extend(excel_s39_s40(lsts[i][44],lsts[i][45]))
            lists.extend(lsts[i][46:50])#s44
            lists.extend(excel_s47_s49(lsts[i][11],lsts[i][50],lsts[i][51],lsts[i][52]))
            lists.extend(lsts[i][53:56])             
            lists.append(excel_s51(lsts[i][63],lsts[i][56]))
            
            if lsts[i][7].find(u',')!=-1 or lsts[i][7].find(u'，')!=-1:
               list1.append([lsts[i][0],lsts[i][7]])
               
            if lsts[i][3]!=u'':   
                isSome=True
                for j in range(len(blsts)):
                
                    if lsts[i][3][:-1]==blsts[j][1]:
                        isSome=False
                        break

                if  isSome:
                    list4.append([u'',lsts[i][0].split('\\')[5][5:10],lsts[i][6],lsts[i][0].split('\\')[-1],
                                        u'住所カナコード',lsts[i][3]])
                    
            
            list4=sorted(list4, key=lambda list4: list4[3])     
        
                    
            
               
    return lists,len(lsts),list1,list4    
       
            
                    
#-------------------------------------------------------
def excel_zw1(strs):
    
    if strs.find('*')>-1:
        strss=strs.replace("*","_")
        if len(strss)>5:
            return strss[:5]
        else:
            return strss
        
    else:
         if len(strs)>5:
            return strs[:5]
         else:
            return strs

def excel_w2(strs):
    if strs.find('*')>-1:
        return strs.replace("*"," ")
    else:
        return strs

def excel_s39_s40(s,ss):
    
    if s!=u'' and ss!=u'':
        return [u'',ss]

    if s==u'' and ss!=u'':
        return [u'',ss]
    
    if s!=u'' and ss==u'':
        return [s,u'']

    if s==u'' and ss==u'':
        return [u'',u'']
    

def excel_s47_s49(s6,s45,s46,s47):
                         
    if re.findall(u'[0-9]+',s6):
       if int(s6)>0:
            return [u'',u'',u'']
       else:
        return [s45,s46,s47]
    else:
        return [u'',u'',u'']
    if re.findall(u'[0-9]+',s46):
        if int(s46)>=4190101 and int(s46)<=4201231:
           return [u'',u'',u'']
        else:
           return [s45,s46,s47] 
                    
                         
    if re.findall(u'[0-9]+',s47):
        if int(s47)>=4190101 and int(s47)<=4201231:
           return [u'',u'',u'']                     
        else:
           return [s45,s46,s47]  
                        
                         
            
def excel_s51(zs6,s51):
    if zs6==u'1':                     
        return u'1'
    if zs6==u'': 
        return s51

def set_w1(w1,blst):
    isSome=False
    for i in range(len(blst)):
        if w1[:-1]==blst[i][1]:
            isSome=True
            return blst[i][3]+w1[-1]
    if not isSome:
        return w1
        
        

def set_s2(strs):
    if len(strs)>25:
        s=strs[:25]
        if s.find(u',')!=-1:
            return s.replace(u',',u' ') 

        elif s.find(u'，')!=-1:
            return  s.replace(u'，',u' ')
        else:
            return s
    else:
        if  strs.find(u'，')!=-1  :
            return strs.replace(u'，',u' ')  
        
        elif strs.find(u',')!=-1:
            return   strs.replace(u',',u' ')
        
        else:
            return strs
       
        

def set_zs2_zs5(strs):
    if strs.find('*')>-1:
        return u''
    else:
        return strs
    
        
    

#-------------------------------------------------------
def export_list3(dicts):
    lsts=[]
    lst=[]
    for key in dicts:
         lst.append(dicts[key][0])
    lst=sorted(lst, key=lambda lsts: lsts[0])     
    for i in range(len(lst)):
        
        isExists=False
        for j in range(len(lst[i])):
            
            if lst[i][j].find('*')!=-1:
                isExists=True
                break        
        if  isExists:
           lsts.append(lst[i])
    return lsts        
            

#-------------------------------------------------------    

def doWork():
    global active_filename
    lists=[]
    data_list=[]
    l=0

    cwd=os.getcwd()
    path=glob.glob(cwd+'/*.xls')
    path.sort()

    '''
    for i in range(len(base_list)):
        print base_list[i]
    '''
    mapW,mapS,mapZs,mapZw,base_list=read_txt_content(cwd,u'part-s',0)#返回字典                                    
    if mapW is None or mapS is None or mapZs is None or mapZw is None or base_list is None:
        return
    list3=export_list3(mapZs)
    lists,l,list1,list4=processing_data(mapW,mapS,mapZs,mapZw,base_list)
    
    
      
    for i in range(l):
        data_list.append(lists[(len(lists)*i)/l:(len(lists)*(i+1))/l])

    data_list=sorted(data_list, key=lambda data_list: data_list[0])
    
    if len(list1)>0 or len(list3)>0 or len(list4)>0 or len(data_list)>0:
        writeReport(cwd,list1,list3,data_list,list4,[u'画像番号',u'受給者番号'],
                    [u'画像番号',u'資料番号',u'指定番号',u'特別徴収人数',u'普通徴収人数',u'合計人数',u'訂正・無効フラグ'],title_name,
                    list4_name)
    
    for c in range(len(data_list)):
        #print '\n*bw*',data_list[c][:3],'\n*w*',data_list[c][3:11],'\n*s*',data_list[c][12:19],'\n*bs*',data_list[c][20:]
        #print data_list[c],len(data_list[c]),len(data_list)
        pass
        
        
    

    for filename in path:
        active_filename=os.path.split(filename)[1]
        #readExcel(filename,data_list)
    
def writeReport(cwd,list1,list3,data_list,list4,column_name1,column_name3,column_name,column_name4):
    book=xlwt.Workbook(encoding='utf-8')
    
    sheet=book.add_sheet('スペースに処理しました')
   
    for i in range(len(column_name1)):
        sheet.write(0,i,column_name1[i])#写入列名
    for r in range(len(list1)):
        for c in range(len(list1[r])):
            sheet.write(1+r,c,list1[r][c])

    sheet1=book.add_sheet('ブランク')
    for i in range(len(column_name3)):
        sheet1.write(0,i,column_name3[i])#写入列名
    for r in range(len(list3)):
        for c in range(len(list3[r])):
            sheet1.write(1+r,c,list3[r][c])

    sheet2=book.add_sheet('Data')
    for i in range(len(column_name)):
        sheet2.write(0,i,column_name[i])#写入列名
    for r in range(len(data_list)):
        for c in range(len(data_list[r])):
            sheet2.write(1+r,c,data_list[r][c])

    sheet4=book.add_sheet('list4')
    for i in range(len(column_name4)):
        sheet4.write(0,i,column_name4[i])#写入列名
    for r in range(len(list4)):
        for c in range(len(list4[r])):
            sheet4.write(1+r,c,list4[r][c])

            
    book.save(cwd+'\\export.xls')        
         
if __name__=='__main__':
    
    doWork()
    
    '''    
    try:
        doWork()
    except:
        print 'File Error!'
    '''
    raw_input('Please input end!!!')

