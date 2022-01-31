# encoding: utf-8
"""
@author: jaredyuan
@contact: jared.yuan@aihuishou.com
@file: ReadExcel.py
@time: 2018/10/31 16:45
"""
import xlrd


def get_cases(filepath, sheetname):
    cases = {}
    file = xlrd.open_workbook(filepath)
    table = file.sheet_by_name(sheetname)
    nrows = table.nrows

    for i in range(1, nrows):
        cases[str(int(table.cell(i, 0).value))] = {'name': table.cell(i, 1).value,
                                                   'method': table.cell(i, 2).value,
                                                   'url': table.cell(i, 3).value,
                                                   'headers': table.cell(i, 4).value,
                                                   'params': table.cell(i, 5).value,
                                                   'expected': table.cell(i, 6).value}
    return cases

# import os
#
# filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\Params\\Param\\Excel\\case.xlsx'
# cases = get_cases(filepath, '官网创建订单')
# print(cases)
