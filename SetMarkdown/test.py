#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from tkinter import *
import hashlib
import time

LOG_LINE_NUM = 0
LOG_LINE_NUMII = 0

# /Users/liupeng/Library/Mobile Documents/com~apple~CloudDocs/MarkDown/白日梦想家

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
        self.filePathList = []
        self.path = ''

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("文本处理工具_v1.2")           #窗口名
        # self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        # self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        # self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="路径")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="日志")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="文件列表")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=9)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=35)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_readflies_button = Button(self.init_window_name, text="读取文件", bg="lightblue", width=10,
                                                    command=self.readflies)  # 调用内部方法  加()为直接调用
        self.str_trans_to_readflies_button.grid(row=1, column=11)
        self.str_trans_to_md5_button = Button(self.init_window_name, text="Markdown合体", bg="lightblue", width=10,
                                              command=self.addFiles)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=5, column=11)


    #功能函数
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")

    # 读取文件夹
    def readflies(self):
        self.path = self.init_data_Text.get(1.0,END).strip()
        files = os.listdir(self.path)  # 得到文件夹下的所有文件名称
        s = []
        files.sort()
        for file in files:  # 遍历文件夹
            if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
                f = open(self.path + "/" + file)  # 打开文件
                self.filePathList.append(f.name)
                self.write_log_to_Text("INFO:" + f.name[len(self.path)+1:len(f.name)])
                iter_f = iter(f)  # 创建迭代器
                str = ""
                for line in iter_f:  # 遍历文件，一行行遍历，读取文本
                    str = str + line
                    s.append(str)  # 每个文件的文本存到list中

    def addFiles(self):
        allFilesName = self.path +'.markdown'
        self.write_doing_to_Text("INFO: 正在创建整体文件" + allFilesName + '...')
        newMDFile = open(allFilesName, 'a')
        self.write_doing_to_Text("INFO: 正在创建整体文件" + allFilesName + '完成')
        self.result_data_Text.delete(1.0, END)
        for file in self.filePathList:  # 遍历文件夹
            if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
                self.write_doing_to_Text("INFO: 文件" + file[len(self.path):len(file)] + '存在')
                self.write_doing_to_Text("INFO: 正在打开文件" + file[len(self.path):len(file)] + '...')
                f = open(file)  # 打开文件
                self.write_doing_to_Text("INFO: 打开文件" + file[len(self.path):len(file)] + '完成')
                iter_f = iter(f)  # 创建迭代器
                str = ""
                self.write_doing_to_Text("INFO: 正在将" + file[len(self.path):len(file)] + "内数据写入整体文件...")
                for line in iter_f:  # 遍历文件，一行行遍历，读取文本
                    str = str + line
                    newMDFile.write(line)
                newMDFile.write('\n')
                self.write_doing_to_Text("INFO: 写入完成")
                self.write_doing_to_Text("INFO: 正在关闭文件" + file[len(self.path):len(file)] + '...')
                f.close()
                self.write_doing_to_Text("INFO: 关闭打开文件" + file[len(self.path):len(file)] + '完成')
        self.write_doing_to_Text("INFO: 正在关闭整体文件" + allFilesName + '...')
        newMDFile.close()
        self.write_doing_to_Text("INFO: 关闭整体文件" + allFilesName + '完成')

    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time

    # 日志动态打印
    def write_doing_to_Text(self, logmsg):
        global LOG_LINE_NUMII
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUMII <= 200:
            self.result_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUMII = LOG_LINE_NUMII + 1
        else:
            self.result_data_Text.delete(1.0, 2.0)
            self.result_data_Text.insert(END, logmsg_in)

    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 50:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)



def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()