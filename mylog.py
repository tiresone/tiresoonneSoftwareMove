import datetime as dt
import glob2
import os


# logLevel 0调试（显示全部信息）， 1信息（显示基本进程信息）， 2警告（显示可能会产生问题的信息），
# 3错误（报错）， 4， 5， 6， 7，8， 9静默
def my_log(*Buf, logLevel=0, logMethod='输出到控制台（control）', txtSwitch=0):  # loglevel 日志重要等级
    if logMethod == '不输出':
        logLevel = 9
    elif logMethod == '输出到控制台（control）':
        pass
    elif logMethod == '输出到文本框':
        pass
    else:
        pass

    if txtSwitch == 1:  # 开启日志记录
        logPath = glob2.glob('..\\Software_files\\' + '\\*.txt')
        filename = os.path.join(logPath, str(dt.datetime.now()))
        with open(filename, 'a')as txt:
            if logLevel >= 4:  # 从大到小，范围从小到大
                pass
            elif logLevel >= 3:  # 报错
                for i in Buf:
                    txt.write(i)
            elif logLevel >= 2:  # 警告
                for i in Buf:
                    txt.write(i)
            elif logLevel >= 1:  # 信息
                for i in Buf:
                    txt.write(i)
            elif logLevel >= 0:  # 最低级别的信息也输入，开发者模式
                for i in Buf:
                    txt.write(i)
            pass
    else:
        pass

    if logLevel >= 4:  # 从大到小，范围从小到大
        pass
    elif logLevel >= 3:  # 报错
        for i in Buf:
            print(i)
    elif logLevel >= 2:  # 警告
        for i in Buf:
            print(i)
    elif logLevel >= 1:  # 信息
        for i in Buf:
            print(i)
    elif logLevel >= 0:  # 最低级别的信息也输入，开发者模式
        for i in Buf:
            print(i)
    else:
        return 0


my_log('什么什么', logLevel=2)
