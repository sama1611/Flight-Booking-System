import sqlite3

con = sqlite3.connect('flights.db')
cursor = con.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservations (
        Name TEXT,
        flightnumber TEXT,
        departure TEXT,
        destination TEXT,
        date DATETIME,
        seatnumber TEXT
    )
''')
con.commit()
con.close()

print("Database and table created successfully!")
