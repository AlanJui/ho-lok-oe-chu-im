# %%
# coding=utf-8
import xlwings as xw
# 打開活頁簿檔案
file_path = ('Han-Ggi.xlsx')
wb = xw.Book(file_path)

# %%
source_sheet = wb.sheets['source_data']

row_num = source_sheet.range('A' + str(wb.sheets[0].cells.last_cell.row)).end('up').row
print(f'row_num = {row_num}')

# row_num = wb.sheets[0].range('A1').end('down').row
# print(f'row_num = {row_num}')

# %%
sheet = wb.sheets['工作表1']

row_content = []
start_row = 1
end_row = row_num
row = 1
i = 1  # index for source_data sheet

while row < end_row:
    # Read data from source_sheet
    han_jji = str(source_sheet.range('A' + str(row)).value)
    ze_1 = han_jji.count('，')
    ze_2 = han_jji.count('；')
    gu = han_jji.count('。')
    if gu == 0:
        duan = ze_1 + ze_2 + 1
    else:
        duan = ze_1 + ze_2
    row += 1

    zu_im = ""
    for j in range(0, duan):
        buffer = str(source_sheet.range('A' + str(row)).value)
        buffer.strip()
        zu_im += (buffer + ' ')
        row += 1
    row += 1

    # Write to target cell
    sheet.range('A' + str(i)).value = han_jji
    sheet.range('B' + str(i)).value = zu_im
    i += 1
