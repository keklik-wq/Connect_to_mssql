import pyodbc
from russian_names import RussianNames
import random
import datetime

conn = pyodbc.connect('''Driver={SQL Server};
                        Server=LAPTOP-E727VLM9;
                        Database=aspex2;
                        ''')
if conn:
    print("Yes")
else:
    print("No")


def Read(conn, table):
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    for row in cursor:
        print(row)
    conn.commit()


def Create(conn):
    cursor = conn.cursor()

    cursor.execute(" ")
    return "Create Success!"


def Redact(conn):
    return "Redact Success!"


def Write_Bicycle(conn):
    for i in range(0, 16):
        cursor = conn.cursor()
        brands = ["Stels", "Scott", "Stern", "Denton"]
        stamps = [["VN-02", "VN-01"], ["XY-3", "XY-4"], ["BB-22", "BB-23"], ["DR-01", "DR-00"]]
        rent_prices = [[150, 150], [220, 250], [300, 340], [175, 195]]
        brand = random.randint(0, 3)
        stamp = random.randint(0, 1)
        brand_insert = brands[brand]
        stamp_insert = stamps[brand][stamp]
        rent_price_insert = rent_prices[brand][stamp]

        cursor.execute('INSERT INTO Bicycle (Brand,RentPrice,Stamp) values (?,?,?)',
                       brand_insert, rent_price_insert, stamp_insert)
        conn.commit()
    return "Bicycle Success"


def Write_Client(conn):
    cursor = conn.cursor()
    all_names = RussianNames(count=10000)
    for one_name in all_names:
        one_name_split = one_name.split()
        series = random.randint(1000, 9999)
        number = random.randint(100000, 999999)

        cursor.execute('INSERT INTO Client (Name,Surname,Patronymic,Series_passport,Number_passport,Country) '
                       'values (?,?,?,?,?,?)', one_name_split[0], one_name_split[2], one_name_split[1], series, number,
                       'Russian Federation')
        conn.commit()
    return "Client Success!"


def Write_RentBook(conn):
    cursor = conn.cursor()

    id_bicycles = []
    id_clients = []

    cursor.execute('SELECT * FROM Bicycle')
    for bicycle in cursor:
        id_bicycles.append(bicycle[0])

    cursor.execute('SELECT * FROM Client')
    for client in cursor:
        id_clients.append(client[0])

    data = datetime.date(2010, 5, 1)

    for client in id_clients:
        if random.randint(1, 10) % 10 == 0:
            data += datetime.timedelta(days=1)
        fine = (random.randint(1, 10) // 10) * (random.randint(1, 4))
        bicycle_insert = id_bicycles[random.randint(0, len(id_bicycles) - 1)]
        random_hour = random.randint(1, 8)
        random_paid = random.randint(1, 50) // 49
        cursor.execute('INSERT INTO RentBook (Date,Time,Paid,BicycleID,ClientID,Fine)'
                       'values (?,?,?,?,?,?)', str(data), random_hour, random_paid, bicycle_insert, client, fine)
        cursor.commit()
    return "RentBook Success!"


def New_client_from_concole(conn):
    def str_to_int(str):
        try:
            str = int(str)
        except:
            print("Введён неправильный формат числа")
        return str

    cursor = conn.cursor()
    enter_values = ["Имя", "Фамилия", "Отчество", "Страна", "Серия паспорта", "Номер паспорта"]
    enter_values_from_console = [0, 0, 0, 0, 0, 0]
    for i in range(len(enter_values)):
        print(enter_values[i] + ":", end="")
        enter_values_from_console[i] = input()
        if i < 4:
            assert enter_values_from_console[i].isalpha() == 1
        else:
            assert enter_values_from_console[i].isdigit() == 1
            if i == 4:
                enter_values_from_console[i] = str_to_int(enter_values_from_console[i])

                assert enter_values_from_console[i] > 999 and enter_values_from_console[i] < 10000
            if i == 5:
                enter_values_from_console[i] = str_to_int(enter_values_from_console[i])

                assert enter_values_from_console[i] > 99999 and enter_values_from_console[i] < 1000000
    cursor.execute('INSERT INTO Client (Name,Surname,Patronymic,Country, Series_passport,Number_passport) '
                   'values (?,?,?,?,?,?)', enter_values_from_console[0], enter_values_from_console[1],
                   enter_values_from_console[2], enter_values_from_console[3], enter_values_from_console[4],
                   enter_values_from_console[5]
                   )
    conn.commit()


Write_Bicycle(conn)
Write_Client(conn)
Write_RentBook(conn)
New_client_from_concole(conn)
Read(conn, "Client")
