import tkinter as tk
from tkinter import Button, Label, filedialog
import pyautogui
from move_files import add_singleAddress_list, add_pathList, workbegin


windowName = 'TsoneSoftwareMove'


# 以下函数为窗口功能
def tobedeveloped():
    pyautogui.alert('该功能还未开发')


def singleFW():  # single file window
    global frame_count1, sourcefile_path
    i = frame_count1
    print(i)
    frame_count1 += 1
    btn_1.configure(bg='lightgray')
    btn_2.configure(bg='orange')
    Frame_singleFW = tk.Frame(Frame_middle1, width=700, height=49, padx=1, pady=1, bd=1)
    Frame_singleFW.pack()  # 分区放在

    def findpath1():
        global sourcefile_path
        sourcefile_path = filedialog.askopenfilename()  # 选择了文件地址
        add_singleAddress_list(i)  # 这里读了上面刚改过的地址
        txt1.delete(1.0, "end")  # 删除旧的
        txt1.insert("end", sourcefile_path)  # 显示新的
    lbl1 = Label(Frame_singleFW, text="单个文件")  # 标签1 放在frm_package 中
    lbl1.place(x=5, y=4, width=120)
    # 源文件的格式不同所以单独列，目标地址都是文件夹，放在下面一起写了
    txt1 = tk.Text(Frame_singleFW, relief="solid")  # 创建文本框
    txt1.place(x=120, y=4, width=400, height=40)  # 放置
    txt1.insert("end", sourcefile_path)
    btn1 = Button(Frame_singleFW, text="打开文件位置", command=findpath1)
    btn1.place(x=550, y=4, width=120)


def multiFW():  # multiple file window
    global frame_count2, sourcefile_path
    i = frame_count2
    frame_count2 += 1
    btn_1.configure(bg='orange')
    btn_2.configure(bg='lightgray')
    Frame_multiFW = tk.Frame(Frame_middle1, width=900, height=49, padx=1, pady=1, bd=1)
    Frame_multiFW.pack()  # 分区放在

    def findpath2():
        global sourcefile_path
        sourcefile_path = filedialog.askdirectory()  # 选择了文件地址
        add_pathList(i)  # 这里读了上面刚改过的地址
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
    global target_path
    target_path = filedialog.askdirectory()
    txt_1.delete(1.0, "end")
    txt_1.insert("end", target_path)


# def renew():
#     if choice == 1:
#         pass
#     else:
#         pass


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
