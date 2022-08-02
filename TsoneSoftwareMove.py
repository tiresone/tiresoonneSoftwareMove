import os
import shutil
import tkinter as tk
from tkinter import Button, Label, filedialog
import pyautogui

'''地址address包含文件名name和路径path'''

sourcefile_path = 'C:/Users/24856/Desktop/test'  # 后面要变成选择文件夹
target_path = 'H:/test2'  # 后面要变成选择文件夹  \转译 \\意思就是\
check_key = 1  # 检查要用
windowName = 'TsoneSoftwareMove'
choice = 1
filenameList = []  # 不管单个多个都读在列表里，最后一起搬


def check():
    global check_key
    if sourcefile_path == '':
        print('源路径不能为空')
        check_key = 0
    if target_path == '':
        print('目标路径不能为空')
        check_key = 0
    else:
        print('检查无误')


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
    print('return a', a)
    return a


def add_filename_list():
    global filenameList
    if check_key == 1:
        if choice == 1:  # choice是字符串形式
            single_move()
        if choice == 2:
            filenameList.append(getDirList(sourcefile_path))


def list_move():  # 将文件夹中的所有内容移动到目标文件夹
    global sourcefile_path, target_path
    filenameList = getDirList.(sourcefile_path)  # 找到文件地址，这里filename是个列表

    for filename in filenameList:
        OldAddress = os.path.join(sourcefile_path, filename)
        print('old address is ', OldAddress)
        NewAddress = os.path.join(target_path, filename)
        print('new address is ', NewAddress)
        shutil.move(OldAddress, NewAddress)
        print('移动完成')


def single_move():
    global sourcefile_path, target_path
    OldAddress = sourcefile_path  # 因为要共用一个选项框，这里选择的时候会直接选到具体文件
    print('old address is ', OldAddress)
    if OldAddress.count('/') != 0:
        filename = OldAddress.split('/')[-1]
    elif OldAddress.count('/') != 0:
        filename = OldAddress.split('/')[-1]
    else:
        return 0
    NewAddress = os.path.join(target_path, filename)
    print('new address is ', NewAddress)
    shutil.move(OldAddress, NewAddress)
    print('移动完成')


def workbegin():
    global check_key, choice
    check()


# def multi_move():  # 复选文件进行移动，可以弄个+号，点一次加一个文件，到有交互之后实现
#     global sourcefile_path, target_path

# 以下函数为窗口功能
def tobedeveloped():
    pyautogui.alert('该功能还未开发')


def singleFW():  # single file window
    global sourcefile_path, choice
    choice = 1
    btn_1.configure(bg='lightgray')
    btn_2.configure(bg='orange')

    Frame_singleFW = tk.Frame(Frame_middle1, width=700, height=49, padx=1, pady=1, bd=1)
    Frame_singleFW.pack()  # 分区放在

    def findpath1():
        print('find path1')
        global sourcefile_path
        sourcefile_path = filedialog.askopenfilename()
        print(sourcefile_path)
        txt1.delete(1.0, "end")
        txt1.insert("end", sourcefile_path)

    lbl1 = Label(Frame_singleFW, text="单个文件")  # 标签1 放在frm_package 中
    lbl1.place(x=5, y=4, width=120)
    # 源文件的格式不同所以单独列，目标地址都是文件夹，放在下面一起写了
    txt1 = tk.Text(Frame_singleFW, relief="solid")  # 创建文本框
    txt1.place(x=120, y=4, width=400, height=40)  # 放置
    txt1.insert("end", sourcefile_path)
    btn1 = Button(Frame_singleFW, text="打开文件位置", command=findpath1)
    btn1.place(x=550, y=4, width=120)


def multiFW():  # multiple file window
    global sourcefile_path, choice
    choice = 2
    btn_1.configure(bg='orange')
    btn_2.configure(bg='lightgray')

    Frame_multiFW = tk.Frame(Frame_middle1, width=900, height=49, padx=1, pady=1, bd=1)
    Frame_multiFW.pack()  # 分区放在

    def findpath2():
        print('find path2')
        global sourcefile_path
        sourcefile_path = filedialog.askdirectory()
        txt2.delete(1.0, "end")
        txt2.insert("end", sourcefile_path)
    lbl2 = Label(Frame_multiFW, text="文件夹内所有文件")  # 标签1 放在frm_package 中
    lbl2.place(x=104, y=4)
    txt2 = tk.Text(Frame_multiFW, relief="solid")  # 创建文本框
    txt2.place(x=300, y=4, width=400, height=40)  # 放置
    txt2.insert("end", sourcefile_path)
    btn2 = Button(Frame_multiFW, text="打开文件位置", command=findpath2)
    btn2.place(x=750, y=4, width=120)


def target_address_get():
    print('find target path')
    global target_path
    target_path = filedialog.askdirectory()
    print(target_path)
    txt_1.delete(1.0, "end")
    txt_1.insert("end", target_path)


def renew():
    if choice == 1:
        pass
    else:
        pass

    pass


if __name__ == '__main__':
    window = tk.Tk()
    window.title(windowName)
    # window.iconphoto()  # 图标
    window.geometry("1400x700+200+200")

    # -----------设置菜单栏-------------
    menu = tk.Menu(window)
    submenu_1 = tk.Menu(menu, tearoff=0)  # tearoff默认是否下拉
    submenu_1.add_command(label='账户', command=tobedeveloped)
    submenu_1.add_command(label='文件包位置', command=tobedeveloped)
    submenu_1.add_cascade(label='快捷键', command=tobedeveloped)
    menu.add_cascade(label='设置', menu=submenu_1)

    submenu_2 = tk.Menu(submenu_1)
    submenu_2.add_command(label='本色', command=tobedeveloped)  # command基本按键菜单
    submenu_2.add_command(label='其他颜色', command=tobedeveloped)
    menu.add_cascade(label='主题', menu=submenu_2)  # cascade 创建能继续下拉的菜单

    window.config(menu=menu)
    # ---------------------------------

    # -------------上方分区------------
    Frame_top = tk.Frame(window, width=700, height=40, padx=1, pady=1, bd=1)
    Frame_top.pack()  # 分区放在
    # ---------------------------------

    # ------------上方分区内容-------------
    btn_1 = Button(Frame_top, text="加选单个文件", bg="orange",
                   command=singleFW)  # 按钮
    btn_1.place(x=0, y=0, width=350)
    btn_2 = Button(Frame_top, text="加选多个文件", bg="orange",
                   command=multiFW)  # 按钮
    btn_2.place(x=350, y=0, width=350)
    # ---------------------------------

    # -------------中间分区------------
    Frame_middle1 = tk.Frame(window, width=700, height=0, padx=1, pady=1, bd=1, bg='lightgray')
    Frame_middle1.pack()  # 分区放在
    Frame_middle2 = tk.Frame(window, width=700, height=100, padx=1, pady=1, bd=1)
    Frame_middle2.pack()  # 分区放在
    # ---------------------------------

    # ------------中下分区内容-------------
    btn_3 = Button(Frame_middle2, text="目标路径选择", command=target_address_get)
    btn_3.place(x=550, y=10, width=120)
    lbl_1 = Label(Frame_middle2, text="移动到")  # 标签1 放在frm_package 中
    lbl_1.place(x=50, y=13, height=35)
    txt_1 = tk.Text(Frame_middle2, relief="solid")  # 创建文本框
    txt_1.place(x=120, y=10, width=400, height=40)  # 放置
    txt_1.insert("end", target_path)
    # ---------------------------------

    # -------------下方分区------------
    Frame_bottom = tk.Frame(window, width=700, height=40, padx=1, pady=1, bd=1)
    Frame_bottom.pack(side='bottom')  # 分区放在
    # ---------------------------------

    # ------------下方分区内容-------------
    btn_4 = Button(Frame_bottom, text="开始搬砖", bg="lightgreen",
                   command=workbegin)  # 按钮
    btn_4.place(x=350, y=20, anchor='center', width=240)
    # ---------------------------------

    window.mainloop()  # 窗口进入消息主循环，能随时接受命令
