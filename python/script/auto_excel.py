"""
解析用例excel文件，自动生成用例注释
author: lwx930245
modify_records:
    - 2020.12.29, lwx930245, create this
"""
import xlrd
import os
import time


class Excel:
    def __init__(self, author, dir_name):
        """
        解析用例excel文件，自动生成用例注释
        :param author: 生成注释文件所在目录
        :param dir_name:
        """
        self.data_dict = {}
        self.author = author
        self.dir_name = dir_name

    def read_file(self, test_case_excel):
        """
        读取excel中的内容
        :param test_case_excel: excel文件路径
        :return: None
        """
        data = xlrd.open_workbook(test_case_excel)

        # 通过索引获取表格
        table = data.sheet_by_index(0)
        rows = table.nrows
        for row in range(rows):
            row_data = table.row_values(row)
            # row_data索引0为excel第一列,以用例名number为键,name,level,condition,step,result组成的列表为值
            self.data_dict[row_data[4].replace("\n", "")] = [row_data[3], row_data[2], row_data[5], row_data[6],
                                                             row_data[7]]

        print(self.data_dict)

    def write_annotation(self):
        """
        根据excel中的内容，写用例中的注释
        :return: None
        """
        file_list = os.listdir(self.dir_name)
        for file_name in file_list:
            test_number = file_name.strip().split("_test")[0]
            if test_number in self.data_dict:
                with open("./{}/{}".format(self.dir_name, file_name), 'r+') as f:
                    self.do_write(f, test_number)

    def do_write(self, file_obj, test_number):
        """
        按照固定模板生成用例注释
        :param file_obj: 文件流对象
        :param test_number: 用例名
        :return: None
        """
        day_time = time.strftime("%Y.%m.%d", time.localtime(time.time()))
        content = file_obj.read()
        index = content.index("import")
        if not index:
            index = 0
        content = content[index:]
        file_obj.seek(0, 0)
        file_obj.write('"""\n')
        file_obj.write('TestCase_Number:{}\n'.format(test_number))
        file_obj.write('TestCase_Name:{}\n'.format(self.data_dict[test_number][0]))
        file_obj.write('TestCase_Level:{}\n'.format(self.data_dict[test_number][1]))
        file_obj.write('TestCase_Pretreatment Condition:\n')
        condition_list = self.data_dict[test_number][2].split("\n")
        for condition in condition_list:
            if condition != "":
                file_obj.write('    {}\n'.format(condition))
        file_obj.write('TestCase_Test Steps:\n')
        step_list = self.data_dict[test_number][3].split("\n")
        for step in step_list:
            if step != "":
                file_obj.write('    {}\n'.format(step))
        file_obj.write('TestCase_Expected Result:\n')
        result_list = self.data_dict[test_number][4].split("\n")
        for result in result_list:
            if result != "":
                file_obj.write('    {}\n'.format(result))
        file_obj.write('author:{}\n'.format(self.author))
        file_obj.write('modify_records:\n    -{}, {}, create this testcase'.format(day_time, self.author))
        file_obj.write('\n"""\n\n{}'.format(content))

    def run(self):
        """
        生成用例注释入口
        :return: None
        """
        self.read_file("excel.xlsx")
        self.write_annotation()


excel = Excel("jwx5319396", "testcase")
excel.run()
