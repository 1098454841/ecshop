
import xlrd  #对excel进行读


def read_excel():
    file_path = r"D:\software\Gitroot\zhuceProject\data\data.xlsx"
    workbook = xlrd.open_workbook(file_path) #实例化工作簿对象
    sheet_names = workbook.sheet_names()  #获取所有工作表的名字
    print("工作表的名字",sheet_names)
    sheet = workbook.sheet_by_name("register")
    rows = sheet.nrows #获取总行数
    cols = sheet.ncols #获取总列数
    print("总行数",rows,"总列数",cols)
    # second = sheet.row(2)
    content = []
    for line in range(1,rows):
        lines = sheet.row_values(line, 0, 10)
        lines[2] = str(int(lines[2]))
        lines[3] = str(int(lines[3]))
        lines[5] = str(int(lines[5]))
        lines[6] = str(int(lines[6]))
        lines[7] = str(int(lines[7]))
        lines[8] = str(int(lines[8]))
        content.append(lines)
    return content
