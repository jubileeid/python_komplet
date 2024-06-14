from openpyxl import workbook, load_workbook

wb = load_workbook('datasales.xlsx')
ws = wb.active
print(ws)
