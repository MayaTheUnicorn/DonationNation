import openpyxl as op


wb = op.load_workbook(r'C:\Users\kotbe\OneDrive\Desktop\Donation_Nation.xlsx')
ws = wb['Sheet1']
# print(ws['B2'].value)
ws['B2'].value = 5
wb.save(r'C:\Users\kotbe\OneDrive\Desktop\Donation_Nation.xlsx')
#
# print(ws.cell(row=2, column=3).value)
