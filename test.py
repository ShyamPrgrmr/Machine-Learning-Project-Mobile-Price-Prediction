from prettytable import PrettyTable
import mysql.connector
x = PrettyTable()
x.field_names = ["Mobile name", "Battery Power", "Clock Speed", "Front Camera","Internal Mem.","Processor Core","Primary Camera","Ram","price"]

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="Shyam123@@"
)

sql_select_Query = "select * from mobile.mob"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()

for row in records:
    x.add_row([row[0],row[1],row[2],row[3],row[5],row[6],row[7],row[10],row[14]])

print(x)
