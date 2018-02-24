# -*- coding: utf-8 -*-

import json, xlwt


def read_score(jsonfile):
    with open(jsonfile, encoding='utf-8') as f:  # 将json文件转化为字典
        score_all = json.loads(f)

    book = xlwt.Workbook()  # 创建excel文件
    sheet = book.add_sheet('sheet1')  # 创建一个表
    title = ['职位名称', '职位链接', '职位类型', '工作地点', '发布时间']
    for col in range(len(title)):  # 存入第一行标题
        sheet.write(0, col, title[col])
    row = 1  # 定义行
    for k in score_all:
        data = score_all[k]  # data保存姓名和分数的list
        data.insert(0, k)  # 第一列加入序号
        for index in range(len(data)):  # 依次写入每一行
            sheet.write(row, index, data[index])
        row += 1
    path='D:/NutchWorkPlat/workspace/Tencent/Tencent/spiders/'
    book.save(path+'tencent.xls')


path='D:/NutchWorkPlat/workspace/Tencent/Tencent/spiders/'
read_score(path+'tencent.json')
