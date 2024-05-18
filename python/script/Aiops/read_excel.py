from openpyxl import load_workbook
# https://blog.csdn.net/yaos829/article/details/103594988


def read_excel(tbl_path):
    wb2 = load_workbook(tbl_path)
    ws = wb2["网络设备"] # sheet名
    rows, columns = ws.max_row, ws.columns
    for row in range(2, rows+1):
        brand = ws.cell(row, 3).value
        device_type = ws.cell(row, 4).value
    # ws.max_row # 从1开始
    # ws.max_column
    # ws.cell(row=row, column=column).value
    pass



if __name__ == '__main__':
    file_name = "./python/script/Aiops/网络设备表20240423.xlsx"
    read_excel(file_name)
