import os, sys
import winshell

# winshell.desktop()获取桌面路径
link_filepath = os.path.join(winshell.desktop(), "srt.lnk")

with winshell.shortcut(link_filepath) as link:
    link.path = "D:\W32DasmV10.0\W32Dasm.exe"  # 更改目标文件
    link.working_directory = "D:\W32DasmV10.0"  # 更改起始位置

