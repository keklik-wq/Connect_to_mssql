import random, xlwt,xlrd

rb=xlrd.open_workbook("employees.xls")
sheet = rb.sheet_by_index(0)

wb = xlwt.Workbook()
ws = wb.add_sheet('employees')
title = ["Series", "Number", "Hours", "Salary"]
for i in range(0, 4):
    ws.write(0, i, title[i])

for i in range(1, 100):

    series = sheet.row_values(i)[0]
    number = sheet.row_values(i)[1]
    if i>50:
        hours = random.randint(20, 40)
        salary = random.randint(2, 5) * 100 * hours
    else:
        hours = sheet.row_values(i)[2]
        salary = sheet.row_values(i)[3]
    values = [series, number, hours, salary]
    for j in range(0, 4):
        ws.write(i, j, values[j])

wb.save('employees.xls')