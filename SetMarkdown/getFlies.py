
import os
path = "/Users/liupeng/Library/Mobile Documents/com~apple~CloudDocs/MarkDown/白日梦想家" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
files.sort()
for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
        f = open(path+"/"+file) #打开文件
        print(f.name)
        iter_f = iter(f) #创建迭代器
        str = ""
        for line in iter_f: #遍历文件，一行行遍历，读取文本
            str = str + line
            s.append(str) #每个文件的文本存到list中