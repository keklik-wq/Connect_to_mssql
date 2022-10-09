import pyodbc,xlrd

s = 'edu7autmn.database.windows.net' #Your server name
d = 'db' #Your database name
u = 'Edu' #Your login
p = 'ASx#dsano@b4' #Your login password
str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+ p
conn = pyodbc.connect(str)
cursor = conn.cursor()

rb=xlrd.open_workbook('employees.xls')
sheet=rb.sheet_by_index(0)
for i in range(1,100):
    val=sheet.row_values(i)
    cursor.execute('INSERT INTO dudkovemployees (Series,Number,Hours,Salary) values (?,?,?,?)',
                   int(val[0]), int(val[1]), int(val[2]),int(val[3]))
    conn.commit()
if conn:
    print("yes")
else:
    print("no")