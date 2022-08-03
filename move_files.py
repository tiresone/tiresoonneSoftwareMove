import os
import shutil


'''地址address包含文件名name和路径path'''

sourcefile_path = ''  # 后面要变成选择文件夹
target_path = ''  # 后面要变成选择文件夹  \转译 \\意思就是\
check_key = 1  # 检查要用
choice = 1
OldAddressList = []  # 不管单个多个都读在列表里，最后一起搬。单个的直接存进去，多个的最后开始的时候读
pathList = []
frame_count1 = 0
frame_count2 = 0


def check():
    pass


#  @ 功能：拿到文件夹列表
#  @ 参数：[I] :p 当前要查看的目录
def getDirList(p):  # 其实这个还没看太懂
    p = str(p)
    if p == "":
        print('p is none')
        return []
    p = p.replace("/", "\\")  # p不为空，就替换规范化一下
    if p[-1] != "\\":
        p = p + "\\"
    a = os.listdir(p)  # 找到p下的文件列表
    return a


def add_singleAddress_list(i):
    global OldAddressList
    if len(OldAddressList) != 0 and len(OldAddressList) >= i:  # 如果对应的位置存在
        OldAddressList[i] = sourcefile_path
    else:  # 如果对应位置没内容
        OldAddressList.append(sourcefile_path)  # 在后面加上


def add_pathList(i):
    global pathList
    if len(pathList) != 0 and len(pathList) >= i:
        pathList[i] = sourcefile_path
    else:
        pathList.append(sourcefile_path)


def workbegin():
    global pathList, OldAddressList
    for path in pathList:  # 遍历路径表
        filenameList = getDirList(path)  # 找到路径下的文件名列表
        for filename in filenameList:
            OldAddressList.append(os.path.join(path, filename))  # 将文件名加路径得到地址加入到地址列表
    for OldAddress in OldAddressList:
        shutil.move(OldAddress, target_path)
    print('搬完啦')

