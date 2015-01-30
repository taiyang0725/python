#python stat
'''
 3     当我们使用os.stat(path)获取一个文件(夹)信息的时候，
 4     os.stat(path)本身返回的是一个元组如：
 5     
 6     nt.stat_result(st_mode=33206, st_ino=203224933185146561, st_dev=0,
 7     st_nlink=1, st_uid=0, st_gid=0, st_size=21090, st_atime=1376373336,
 8     st_mtime=1376534141, st_ctime=1376373336)
 9 
10     在这个元组中，包含了10个属性：
11     st_mode    -- protection bits(模式)
12     st_ino     -- inode number(索引号)
13     st_dev     -- device(设备)
14     st_nlink   -- number of hard links(硬链接号)
15     st_uid     -- user id of owner(用户id)
16     st_gid     -- group id of owner (组id)
17     st_size    -- size of file,in bytes (大小)
18     st_atime   -- time of most recent access expressed in seconds (访问时间)
19     st_mtime   -- time of most recent content modificatin expressed in seconds (修改时间)
20     st_ctime   -- platform dependent;time of most recent metadata change on Unix,
21                   or the teime of creation on Windows,expressed in senconds (根据不同操作系统而定)
22 
23     #############################################################
24     而stat在这里起到什么作用呢？
25     类似于java中定义的一些常量：
26     如：
27         os.stat(path).st_size
28         os.stat(path)[stat.ST_SIZE]
29         这两种表示方法是一样的。
'''
import os
import time
import stat
 
def get_file_stat(path):
    '''获取一个文件(夹)信息，该信息将以一个元组的形式返回'''
    if os.path.exists(path):
       return os.stat(path)
    else:
        print('the path [{}] is not exist!'.format(path))
 
def print_info(file_stat):
'''打印信息'''
    if file_stat != None:
       file_info = {
           'Size' : file_stat [ stat.ST_SIZE ],                         #获取文件大小
           'LastModified' : time.ctime( file_stat [ stat.ST_MTIME ] ),  #获取文件最后修改时间
           'LastAccessed' : time.ctime( file_stat [ stat.ST_ATIME ] ),  #获取文件最后访问时间
           'CreationTime' : time.ctime( file_stat [ stat.ST_CTIME ] ),  #获取文件创建时间
           'Mode' : file_stat [ stat.ST_MODE ],                         #获取文件的模式
           'Device' : file_stat [stat.ST_DEV],                          #设备
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
    print('目录信息：')
    file_stat = get_file_stat(path_dir)
    print_info(file_stat)
    print('#' * 50)
    print('文件信息：')
    file_stat = get_file_stat(path_file)
    print_info(file_stat)
 
if __name__ == '__main__':
    main()
