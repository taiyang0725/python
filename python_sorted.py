#�����㷨
'''
ͨ���涨����������Ԫ��x��y�������Ϊx < y���򷵻�-1�������Ϊx == y���򷵻�0�������Ϊx > y���򷵻�1
'''
lst=[12,5,3,9,45,66,0,4,99]
'''
Python���õ�sorted()�����Ϳ��Զ�list��������:
'''
print sorted(lst)#��С��������
'''
���⣬sorted()����Ҳ��һ���߽׺������������Խ���һ���ȽϺ�����ʵ���Զ��������
���磬���Ҫ�����������ǾͿ����Զ���һ��reversed_cmp����
'''
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted(lst,reversed_cmp)#�Ӵ�С������

'''�ַ������������'''
lsts=['bob', 'about', 'Zoo', 'Credit']
print sorted(lsts)#Ĭ������£����ַ��������ǰ���ASCII�Ĵ�С�Ƚϵģ�����'Z' < 'a'���������д��ĸZ������Сд��ĸa��ǰ��
'''
���ڣ������������Ӧ�ú��Դ�Сд��������ĸ������Ҫʵ������㷨�����ض����д����ӸĶ���
ֻҪ�����ܶ�������Դ�Сд�ıȽ��㷨�Ϳ���
'''
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

print sorted(lsts,cmp_ignore_case)#����ĸ��Ȼ˳������




