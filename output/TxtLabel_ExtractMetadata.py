# 该程序实现将txt标签文件中的数据的源文件抽取出来存放到指定文件夹下的功能
'''
	- Domain_Dir  # txt标签数据路径
	- metaData_path # 源图像文件路径
	- save_path  # 目标文件路径
'''

import os
import shutil

# 列出所有txt记录文件
Domain_Dir = './'
# 对图像数据进行分类   
with open(Domain_Dir + 'annotations_xml_object_train.txt', 'r') as f: 
    for i in f:	
        # 获取txt中图片的名称
        picture_name = i.strip('\n')+'.jpg'
        # 移动图片到分类的文件夹
        metaData_path = 'your_path/YOLOX/datasets/Objects365_VOCdevkit_112/VOC2007/JPEGImages/'	# 源图片文件所在路径
        save_path = './train_JPEGImages/'
        # 不存在则创建目录
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            print('文件目录已创建！正在进行数据文件移动中，请稍候......')
        if picture_name in os.listdir(metaData_path):  
            file_path = metaData_path + picture_name    
            # newpath表示目标文件目录
            newpath = save_path
            #移动
            shutil.copy(file_path, newpath)
    print('数据文件抽取完成！')
