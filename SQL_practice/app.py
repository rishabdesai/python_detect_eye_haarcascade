import pypyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME="."
DATABASE_NAME="Students"

connection_string=f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Truse_Connection=yes;
"""

conn = odbc.connect(connection_string)
print(conn)

cursor = conn.cursor()
cursor.execute('SELECT TOP (10) FirstName from Students')

for i in cursor:
    print(i)
