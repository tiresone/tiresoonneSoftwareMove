import os, sys
import re
import shutil
from tkinter import filedialog
import winshell


OldAddress = filedialog.askopenfilename()  # 快捷方式 的地址
NewAddress = filedialog.askdirectory()  # 软件 的目标文件夹


# 找到快捷方式文件指向的文件夹
# 搬动文件夹到目标文件夹
def change_software():
    with winshell.shortcut(OldAddress) as link:
        softwarePath = link.path
        print('softwarePath', softwarePath)
        split = re.split('\\\\', softwarePath)  # 主要是对文件名和路径名，地址之间的转换,
        # 两个反斜杠在字符串相当于一个，而re里也将一个反斜杠当作转义符，即字符串里四个斜杠在re里相当于两个，即代表一个斜杠
        fileName = str(split[-1])  # 保留文件名，等会重新指向要用
        print('fileName', fileName)
        del split[-1]  # split中删除文件名。del是python中的语法，删除指定位置的元素
        folderPath = '\\'.join(split)  # 这个时候就成了路径。join 是re.split 的逆函数，处处用/连接split剩下的元素
        print('folderPath', folderPath)
        NewAddress.replace('/', '\\')
        print('NewAddress', NewAddress)
        shutil.move(folderPath, NewAddress)  # 移动软件的所有文件到目标文件包
        #  下两步改变快捷方式指向
        link.path = os.path.join(NewAddress, fileName)  # 更改目标文件，其实是地址
        link.working_directory = NewAddress  # 路径（目标文件包）


change_software()

