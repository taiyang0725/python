#sentence = 'I am an Englist sentence'

#print sentence.split("a")#�ַ����Ĳ��

'''
s=""
li=['w','a','n','g']
print s.join(li)#�ַ���������
#********************************************
word = 'helloworld' #�����ַ���
for c in word: 
    print c
    '''
#**************��ȡ�����ļ�******************************
'''

f = file('E:\wangan.txt','re') #��ȡ�����ļ�
data = f.read() 

out=file('F:\wangan.txt','w')
out.write(data)

f1 = open('F:\wangan.txt','re')
print f1.read()

f.close()
out.close()
'''


#************��Stringд�뱾���ļ�****************************************
'''
data = '���������ͣ�' 
out = file('E:\wangan.txt', 'w') 
out.write(data) 
out.close()
'''
#*******************��һ���ļ��ж������ݣ���������һ���ļ�
'''
f = file('E:\cike.txt') #��ȡ�����ļ�
data = f.read()
out = open('E:\wangan.txt', 'w') 
out.write(data)
f.close()
out.close()'''
#************СDome********************************************************
'''
f=file('E:\score.txt')
lines=f.readlines()
f.close()

results=[]#��ʼ��

for line in lines:
   # print line
    data=line.split()
    #print data

    sum=0
    for score in data[1:]:
        sum+=int(score)
    result='%s\t: %d\n' % (data[0],sum)
    print result
'''
#****************��ϰ1+23+4...+100=?********************
'''
data=range(1,101)
sum=0
for b in data:
    sum+=int(b)
    print sum#��forѭ��֮��
print sum#��forѭ��֮��
'''
#*************ѭ��********************************
'''
for j in range(1,3):
    print j
    '''
#try...except#�쳣�����൱��try...catch
#******************Dome*************************
'''
#�ֵ� dictionary �൱��map����
score={'����':90,'����':95,'����':50}

print score['����']#ȡֵ
print score['����']

score['wangan']=120#���
score['����']=100#�޸�
del score['����']#ɾ��
for name in score:#����
    print  name,score[name]
'''
#************����**************************************
'''
import urllib2
web=urllib2.urlopen('http://www.baidu.com')
content=web.read()
out = open('E:\output.html', 'w') 
out.write(content) 
out.close()
print content
'''
#****************a��Ŀ�����*********
'''
a='hello'
b='world'
c=True and a or b
print c
d=False and a or b
print d
'''
#*****************��ѧ����*************
'''
import math
print math.pi
print math.e
print math.ceil(1.2)#��x����ȡ�������磺x=1.2������2
print math.floor(1.2)#����ȡ��
'''
#********************������ʽ****************
'''
import re #������ʽ���ڵİ�
text='199999999999999999'
m=re.findall(r'[0-9]{1,3}',text)
if m:
    print m
else:
    print 'not match'
a='site sea sue sweet see case sse ssee lsses'
b=re.findall(r'\bs\S?e\b',a)#��s��ͷ��e����
#print b
'''
#***********��ϰ excel*************
'''
import xlrd
def readXls(path):
    rtn_list=[]
    book = xlrd.open_workbook(path)#��ȡexcel��book����
    
    sheet = book.sheet_by_index(0)#ͨ��sheet������ȡsheet����
   
    rows = sheet.nrows#������
    cols = sheet.ncols#������
    for r in range(2,rows):
        row = []
        for c in range(cols):
            val = sheet.cell_value(r,c)#ֻ��cell��ֵ����
            val =get_col_value(val)
            row.append(val)
        rtn_list.append(row)
    return rtn_list
readXls('C:\Users\Administrator\Desktop\test\report.xlsx')
'''

print range._doc_









