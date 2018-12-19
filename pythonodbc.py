import pyodbc

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=mr-fap-svr;'
                      'Database=Investment;'
                      'Trusted_Connection=yes;')

cursor = cnxn.cursor()

cursor.execute("""
SELECT portfolio_name FROM portfolios
WHERE black_diamond_portfolio_code = 'z033296191';
""")

for row in cursor:
    print(row)
