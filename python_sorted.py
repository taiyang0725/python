#排序算法
'''
通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1
'''
lst=[12,5,3,9,45,66,0,4,99]
'''
Python内置的sorted()函数就可以对list进行排序:
'''
print sorted(lst)#从小到大，升序
'''
此外，sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。
比如，如果要倒序排序，我们就可以自定义一个reversed_cmp函数
'''
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted(lst,reversed_cmp)#从大到小，降序

'''字符串排序的例子'''
lsts=['bob', 'about', 'Zoo', 'Credit']
print sorted(lsts)#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
'''
现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，
只要我们能定义出忽略大小写的比较算法就可以
'''
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

print sorted(lsts,cmp_ignore_case)#首字母自然顺序排序




