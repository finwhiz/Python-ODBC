import pyodbc

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=servername;'
                      'Database=dbname;'
                      'Trusted_Connection=yes;')

cursor = cnxn.cursor()

cursor.execute("""
SELECT portfolio_name FROM portfolios
WHERE black_diamond_portfolio_code = 'Test';
""")

for row in cursor:
    print(row)
