import openpyxl as excel


wbname = "2021_05_11.xlsx"
msg = "Hello"
wb = excel.Workbook()

ws = wb.active

ws["A1"] = msg

wb.save("2021_05_11.xlsx")

