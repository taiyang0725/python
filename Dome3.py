#sentence = 'I am an Englist sentence'

#print sentence.split("a")#字符串的拆分

'''
s=""
li=['w','a','n','g']
print s.join(li)#字符串的链接
#********************************************
word = 'helloworld' #遍历字符串
for c in word: 
    print c
    '''
#**************读取本地文件******************************
'''

f = file('E:\wangan.txt','re') #读取本地文件
data = f.read() 

out=file('F:\wangan.txt','w')
out.write(data)

f1 = open('F:\wangan.txt','re')
print f1.read()

f.close()
out.close()
'''


#************将String写入本地文件****************************************
'''
data = '王安，加油！' 
out = file('E:\wangan.txt', 'w') 
out.write(data) 
out.close()
'''
#*******************从一个文件中读出内容，保存至另一个文件
'''
f = file('E:\cike.txt') #读取本地文件
data = f.read()
out = open('E:\wangan.txt', 'w') 
out.write(data)
f.close()
out.close()'''
#************小Dome********************************************************
'''
f=file('E:\score.txt')
lines=f.readlines()
f.close()

results=[]#初始化

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
#****************练习1+23+4...+100=?********************
'''
data=range(1,101)
sum=0
for b in data:
    sum+=int(b)
    print sum#在for循环之内
print sum#在for循环之外
'''
#*************循环********************************
'''
for j in range(1,3):
    print j
    '''
#try...except#异常处理相当于try...catch
#******************Dome*************************
'''
#字典 dictionary 相当于map集合
score={'张三':90,'李四':95,'王五':50}

print score['张三']#取值
print score['王五']

score['wangan']=120#添加
score['王五']=100#修改
del score['张三']#删除
for name in score:#遍历
    print  name,score[name]
'''
#************网络**************************************
'''
import urllib2
web=urllib2.urlopen('http://www.baidu.com')
content=web.read()
out = open('E:\output.html', 'w') 
out.write(content) 
out.close()
print content
'''
#****************a三目运算符*********
'''
a='hello'
b='world'
c=True and a or b
print c
d=False and a or b
print d
'''
#*****************数学运算*************
'''
import math
print math.pi
print math.e
print math.ceil(1.2)#对x向上取整，例如：x=1.2，返回2
print math.floor(1.2)#向下取整
'''
#********************正则表达式****************
'''
import re #正则表达式所在的包
text='199999999999999999'
m=re.findall(r'[0-9]{1,3}',text)
if m:
    print m
else:
    print 'not match'
a='site sea sue sweet see case sse ssee lsses'
b=re.findall(r'\bs\S?e\b',a)#以s开头以e结束
#print b
'''
#***********练习 excel*************
'''
import xlrd
def readXls(path):
    rtn_list=[]
    book = xlrd.open_workbook(path)#获取excel的book对象
    
    sheet = book.sheet_by_index(0)#通过sheet索引获取sheet对象
   
    rows = sheet.nrows#行总数
    cols = sheet.ncols#列总数
    for r in range(2,rows):
        row = []
        for c in range(cols):
            val = sheet.cell_value(r,c)#只有cell的值内容
            val =get_col_value(val)
            row.append(val)
        rtn_list.append(row)
    return rtn_list
readXls('C:\Users\Administrator\Desktop\test\report.xlsx')
'''

print range._doc_









