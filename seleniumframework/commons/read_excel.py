import xlrd
import os
def readExcel(sheet,row,col):
    file = xlrd.open_workbook("d://seleniumframework//data//readexcel.xlsx")
    a=file.sheet_by_name(sheet)
    b=a.cell_value(row,col)
    #print(b)
    return b


#print(os.path.abspath('..'+"\data//readexcel.xlsx"))
#readExcel("name", 2, 0)
#phonenumber=readExcel("phonenumber",1,0)
#print(phonenumber)