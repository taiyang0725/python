#python stat
'''
 3     ������ʹ��os.stat(path)��ȡһ���ļ�(��)��Ϣ��ʱ��
 4     os.stat(path)�����ص���һ��Ԫ���磺
 5     
 6     nt.stat_result(st_mode=33206, st_ino=203224933185146561, st_dev=0,
 7     st_nlink=1, st_uid=0, st_gid=0, st_size=21090, st_atime=1376373336,
 8     st_mtime=1376534141, st_ctime=1376373336)
 9 
10     �����Ԫ���У�������10�����ԣ�
11     st_mode    -- protection bits(ģʽ)
12     st_ino     -- inode number(������)
13     st_dev     -- device(�豸)
14     st_nlink   -- number of hard links(Ӳ���Ӻ�)
15     st_uid     -- user id of owner(�û�id)
16     st_gid     -- group id of owner (��id)
17     st_size    -- size of file,in bytes (��С)
18     st_atime   -- time of most recent access expressed in seconds (����ʱ��)
19     st_mtime   -- time of most recent content modificatin expressed in seconds (�޸�ʱ��)
20     st_ctime   -- platform dependent;time of most recent metadata change on Unix,
21                   or the teime of creation on Windows,expressed in senconds (���ݲ�ͬ����ϵͳ����)
22 
23     #############################################################
24     ��stat��������ʲô�����أ�
25     ������java�ж����һЩ������
26     �磺
27         os.stat(path).st_size
28         os.stat(path)[stat.ST_SIZE]
29         �����ֱ�ʾ������һ���ġ�
'''
import os
import time
import stat
 
def get_file_stat(path):
    '''��ȡһ���ļ�(��)��Ϣ������Ϣ����һ��Ԫ�����ʽ����'''
    if os.path.exists(path):
       return os.stat(path)
    else:
        print('the path [{}] is not exist!'.format(path))
 
def print_info(file_stat):
'''��ӡ��Ϣ'''
    if file_stat != None:
       file_info = {
           'Size' : file_stat [ stat.ST_SIZE ],                         #��ȡ�ļ���С
           'LastModified' : time.ctime( file_stat [ stat.ST_MTIME ] ),  #��ȡ�ļ�����޸�ʱ��
           'LastAccessed' : time.ctime( file_stat [ stat.ST_ATIME ] ),  #��ȡ�ļ�������ʱ��
           'CreationTime' : time.ctime( file_stat [ stat.ST_CTIME ] ),  #��ȡ�ļ�����ʱ��
           'Mode' : file_stat [ stat.ST_MODE ],                         #��ȡ�ļ���ģʽ
           'Device' : file_stat [stat.ST_DEV],                          #�豸
           'UserID' : file_stat [stat.ST_UID],
           'GroupID' : file_stat [stat.ST_GID]
             }
       for key in file_info:
             print('{} : {}'.format(key, file_info[key]))
    else:
         print('the stat is None!')

def main():
    path_dir = 'e:\\Download'
    path_file = 'e:\\test.html'
    print('Ŀ¼��Ϣ��')
    file_stat = get_file_stat(path_dir)
    print_info(file_stat)
    print('#' * 50)
    print('�ļ���Ϣ��')
    file_stat = get_file_stat(path_file)
    print_info(file_stat)
 
if __name__ == '__main__':
    main()
