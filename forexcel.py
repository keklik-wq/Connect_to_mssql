import random, xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('employees')
title = ["Series", "Number", "Hours", "Salary"]
for i in range(0, 4):
    ws.write(0, i, title[i])

for i in range(1, 100):
    series = random.randint(1000, 9999)
    number = random.randint(100000, 999999)
    hours = random.randint(20, 40)
    salary = random.randint(2, 5) * 100 * hours
    values = [series, number, hours, salary]
    for j in range(0, 4):
        ws.write(i, j, values[j])

wb.save('employees.xls')
