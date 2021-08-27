import xlrd
import time
time1 = time.process_time()
file_name = "/home/huawei/Desktop/testcase_level_classify.md"
origin_file = "/home/huawei/Desktop/kbox用例分级.xls"

data = xlrd.open_workbook(origin_file)
table = data.sheet_by_index(0)
subtitle1 = "#### " + table.row_values(0)[1] + '\n'
subtitle2 = "#### " + table.row_values(0)[2] + '\n'
subtitle3 = "#### " + table.row_values(0)[3] + '\n'
subtitle4 = "#### " + table.row_values(0)[4] + '\n'

with open(file_name, "w+") as f:
    for row in range(1, table.nrows):
        f.write('\n\n')
        f.write("### ")
        f.write(table.row_values(row)[0] + '\n')
        f.write(subtitle1)
        f.write(table.row_values(row)[1] + '\n')
        f.write(subtitle2)
        f.write(table.row_values(row)[2] + '\n')
        f.write(subtitle3)
        f.write(table.row_values(row)[3] + '\n')
        f.write(subtitle4)
        f.write(table.row_values(row)[4] + '\n')
time2 = time.process_time()
print("耗费的时间是：%s" % (time2 - time1))
