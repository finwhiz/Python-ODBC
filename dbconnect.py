import pyodbc

# note that servername and dbname should be edited
# to be the actual database local connection you are using
# Driver and Trusted_Connection may change depending
# on the type database you are using


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
