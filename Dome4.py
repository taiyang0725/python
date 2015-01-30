#****************a三目运算符*********
'''
a='hello'
b='world'
c=True and a or b
print c
d=False and a or b
print d
strs='a.s.d.f.g.h.j.j.k'
print strs.join('pp')

print repr("hello,world!")#创建字符窜
print str("hello,world!")#转化为合理字符串
'''
#***************检验一个值是否存在次序列*********
'''
database=[['a','1'],['b','2'],['c','3'],['d','4']]
u=raw_input('User name:')
p=raw_input('PIN code:')
if[u,p] in database:
    print 'Access granted'
    '''
#**********list中的方法********************
'''
lst=[1,2,4,3,5,6,7,8,9]
lst.append(0)#列表尾部追加新的对象
#print lst
#print lst.count(2)#统计某个元素在列表中出现几次
a=['a','s','d']
lst.extend(a) #一次性追加一个序列
#print lst
#print lst.index(7)#返回元素的索引
lst.insert(3,'wang')#指定下标处插入相应的值
#print lst
#print a.pop()#移除指定元素并返回
lst.remove(8)#移除匹配项元素
lst.reverse()#将正序改为倒叙
lst1=lst[:]#将lst赋予lst1
lst.sort()#进行原始位置排序
print tuple(lst)#将列表转化为元祖，元祖不可改变
print lst
print lst1
'''
#***********字符串格式化***************
'''
format='Hello %s,%s enough for ya?'
values=('world','Hot')
print format%values
#浮点型  %.3f  3表示保留三位小数
'''
#************String中的方法************
'''
seq=['A','S','s','a','c']
print '+'.join(seq)#拼接
str='Hello World'
print str.find('bit')#寻找，-1表示没有找到
print str.lower()#返回字符串小写字母版
print str.title()#返回首字母大写的字符串
print str.replace('World','wangan')#替换
'''
#**************字典***************
'''
items=[('name','cike'),('age','24')]
d=dict(items)#映射出这样的序列字典
print d
print d['age']
print len(d)#返回键值对的数量
x={}
x[4]='wangan'
print x
'''
#**********循环***************
'''
name=''
while not name:
    name=raw_input('Please enter your name')
print 'Hello.%s!' % name

words=['this','is','is','is','is']
for word in words:
    print word

for num in xrange(10):
    print num
print '**********************'
for num in range(10):
    print num
'''
#********字典遍历**********
'''
d={'x':1,'y':2,'z':3}
for key in d:
    print key,':',d[key]
'''
#******有序字典遍历*********并行迭代
'''
name=['zhangsan','lisi','wangwu','xiaoyi']
ages=[12,45,32,88]
for i in range(len(name)):
    print name[i],'is',ages[i]
print zip(name,ages)#把两个序列压缩在一起
for i in zip(name,ages):
    print i 

from math import sqrt
for n in range(99,81,-1):
    root=sqrt(n)
    if(root==int(root)):
        print n
        break
else:
    print '!!!!!!!!!!!!!'
'''
#*********斐波那契数列*********
'''
def fib(num):
    fibs=[0,1]
    for i in range(num-2):
         fibs.append(fibs[-2]+fibs[-1])#倒数第一项加倒是第二项
    return fibs

def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}
def store(data,full_name):
    names=full_name.split()
    if len(names)==2:
        names.insert(1,'')
    label='first','middle','last'

def  print_params(title,*params):
    print title
    print params
print_params('Params:',1,2,3)

for i in [j for j in range(125,132)]+[j for j in range(172,181)]:
    print i,
'''
#****递归思想**************
#########n的阶乘
'''
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

#3###幂运算
def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
        
print power(2,3)
print factorial(10)
'''
#**************类******
''''
_metaclass_=type#确定使用新式lei

class Person:#创建类

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def toString(self):
        print "Hello,World! I'm  %s" % self.name

info=Person()#初始化
info.setName('wangan')#赋值
info.toString()#方法的调用
'''
#***************多态*************
'''
print 'abc'.count('b')
class A:
    def calculate(self,expression):
        global value
        self.value=eval(expression)

class B:
    def talk(self):
        print 'Hi,my value is',self.value

class C(A,B):#c继承于A,B两个类
    pass
tc=C()
tc.calculate('1+2*3')
#tc.talk()

#issubclass(A,B)# 判断A是否是B的子类，返回一个布尔值
#A._bases_  #返回A的父类
_metaclass_=type#确定使用新式lei
class Bird:
    def _init_(self):
        self.hungry=Ture
    def eat(self):
        if self.hungry:
            print 'Aaaaaaaaaa...'
            self.hungry=False
        else:
            print 'No.thanks!'

class SongBird(Bird):
    def _init_(self):
        super(SongBird.self)._init_()
        self.sound='Squawk'
    def sing(self):
        print self.sound

sb=SongBird()
sb.sing()
'''














''' 
a=1,5,9,13,17
for i in [a[-1],a[-2],a[-3]]:
    if a[-3]+5==a[-2] and a[-2]+4==a[-1]:
        print 'hi'
for i in [9]+[j for j in range(42,46)]+[j for j in range(73,85)]+[j for j in range(89,92)]:
    print i
 

b=u''


a='1,2,3,5'
if a[1]==',':
    for i in range(1,len(a),2):
        print i
   


a='q,2w,3,5'
for i in a:
    if i==u'1'or'2'or'3':
        print '++++++++++'

a= ['00000001.jpg','00000005.jpg','00000009.jpg']
for i in [a[-1],a[-2],a[-3]]:
    print i
'''
#************时间模块datetime***********
'''
from  datetime  import  *  
import  time    
print   'date.max:' , date.max  
print   'date.min:' , date.min  
print   'date.today():' , date.today()  
print   'date.fromtimestamp():' , date.fromtimestamp(time.time())  
'''
'''


#1,3,45,66,21
def check_middle_comma(strs,mins,maxs):#多选逗号隔开的方法
    b=strs.split(',')
    for i in b:
a= ['00000001.jpg','00000005.jpg','00000009.jpg']
lst=[] 
for i in [a[-1],a[-2],a[-3]]:
    lst.append(i.split('.')[0])
print lst
print int(lst[0])-int(lst[1])
print int(lst[1])-int(lst[2])

a='1,4,1,3,25'
for i in a.split(','):
    print i
    if int(i)<9:
        print '++++++++++'
    else:
        print '**********'

def check_middle_comma0(strs):#多选逗号隔开的方法
    lst=[] 
    if len(strs)>1 and strs[0]!=',' and strs[-1]!=',':
        for i in range(1,len(strs),2):
            lst.append(i)
        for i in lst:
            if strs[i]==',':
               pass
            else:
                print '多选用逗号隔开'
    else:
        print '以逗号开始或结束'
def check_middle_comma1(strs):
     for i in strs.split(','):
         if len(i)>2:
             print '++++++++++++++++++'
    
def check_middle_comma(strs):
    for i in strs.split(','):
        if int(i)<9:
            check_middle_comma1(strs)
        else:
            check_middle_comma0(strs)
            
a = '1,2,2,122,2'
b = a.split(',')
for i in b:
   
    if int(i)>0 and int(i)<16:
       pass
    else:
        print i

for  i in '5'.split(','):
         if int(i)>0 and int(i)<11:
                pass
         else:
               print '*********',i

def check_middle_comma1(strs,minx,maxx,col):
    for  i in strs.split(','):
        print i[0],
        if int(i)>int(minx) and int(i)<int(maxx):
             
            pass
        else:
            print col,i 
try:
    check_middle_comma1('1,2,31,4,5,12','0','11',u'+++++++')
except:
    print '************'

'''
def check_middle_comma1(strs):
    for i in range(len(strs.split(','))):
        for j in range(len(strs.split(','))):
            if strs.split(',')[i]>strs.split(',')[j]:
                print strs.split(',')[i]
              


def a_b(strs):
    for  i in strs.split(','):
         if int(i)>0 and int(i)<12 and len(strs.split(','))<3:
                pass
         else:
             print '++++++++***********'

def a_b_c(strs):
    for i in strs.split(','):
        #print i
        for j in i.split('.')[0]:
            for z in j:
                print z,
                
    
#a_b_c("'00000001.jpg','000005.jpg','00000009.jpg'")    
#or re.findall(u'[ \u3000]$',strs)or re.findall(u'[ ]{2}',strs)or re.findall(u'株',strs)


import re
def a_b_c_d(strs):
      if re.findall(u'^(1|2)[0-9*]{3}$',strs):
         print '+++++++'
         
      else:
          print '22222222222'
#a_b_c_d('2***')
#print re.findall(u'[~]+','23~5')


def a_b_c(strs):
      if strs.find('○')==-1:
         print '+++++++'
         
      else:
          print '22222222222'

#a_b_c('100 ')

def a(strs):
    print strs.split('_')[-1]

#a('安城市_Page_02.jpg')

          
'''
seq=['708', u'708', u'708']
print '/'.join(seq)#拼接

text={u'a':[u'708',u'709',u'701'],u'b':[u'708',u'700',u'705',u'706'],u'c':[u'708',u'704']}
list=[]
list1=[]
for key in text:
    list.append('/'.join(text[key]))

#print list    
    #print text[key][0],'/','/'.join(list)
name=['zhangsan','lisi','wangwu','xiaoyi']
ages=[12,45,32,88]
#print zip(name,ages)#把两个序列压缩在一起
d = {'vale1': 'aa', 'value2': 'bb'}  
  
  
x = {'value3': 'cc'}  

 
{'vale1': 'aa', 'value3': 'cc', 'value2': 'bb'}  
from datetime import *
import time
a = "2013-10-10 23:40:00"
b = "2013/10/10 23:40:00"
#timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
#otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)

dt = datetime.now()
#print dt    
#print dt.strftime('%m/%d/%y  %H:%M')
from datetime import datetime
from datetime import timedelta

for i in range(16):
    T=i+9
    a=u'20130401'
    b=a[:4]+'-'+a[4:6]+'-'+a[6:]+' '+'9:00:00'
    
    #print b
    #print b.strftime('%m/%d/%y  %H:%M')
    



d1=datetime.now()
print d1
d2 = d1 + timedelta(hours=1)#增加10小时
d2.strftime('%Y-%m-%d %H:%M')
print d2
print d1.strftime('%Y-%m-%d %H:%M')


import datetime
s1='20120125'
s2='20120216'
a=time.strptime(s1,'%Y%m%d')
b=time.strptime(s2,'%Y%m%d')
a_datetime=datetime.datetime(*a[:3])
b_datetime=datetime.datetime(*b[:3])
#print b_datetime.strip()
from string import *
print '12  21'.strip()

s='a b c'
s=s.replace(" ", "")
print s

for i  in range(100):
        print '.',
'''
#####测试专用########
#docheckoutrange(list[46],u'[\u0000-\u00ff\uff71-\uff9f]+',getColumn(46),u'出现半角字符')
#docheckoutrange(list[i],u'[\u3000\uff71-\uff9fｪｯｨｭｮｬｭｧｫｩ ]+',getColumn(i),u'只能全角片假名')
lst3=[1,2,3,4,5,6,7,6,8,6,9,9]
lst1=[]
lst=[6,6,2,2,2,5]
lst2=[]


for i in range(len(lst)):
    if i+1<len(lst):
        if lst[i]!=lst[i+1]:
            lst1.append(lst[i])
                
    
        
print lst1

    
        
        
    
            
            
                
          
    

    
    

        
            












