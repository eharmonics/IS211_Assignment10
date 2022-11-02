import sqlite3 as lite

conn = lite.connect('pets.sqlite')

with conn:
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Person")
    cur.execute("DROP TABLE IF EXISTS Pet")
    cur.execute("DROP TABLE IF EXISTS Person_Pet")
    cur.execute(
        "CREATE TABLE Person (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, first_name TEXT, last_name TEXT, age INTEGER)")
    cur.execute(
        "CREATE TABLE Pet (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, breed TEXT, age INTEGER, dead INTEGER)")
    cur.execute(
        "CREATE TABLE Person_Pet (person_id INTEGER, pet_id INTEGER)")
    
    # Insert Data into Person Table
    cur.execute("INSERT INTO Person VALUES(1, 'James', 'Smith', 41)")
    cur.execute("INSERT INTO Person VALUES(2, 'Diana', 'Greene', 23)")
    cur.execute("INSERT INTO Person VALUES(3, 'Sara', 'White', 27)")
    
    # Insert Data into Pet Table
    cur.execute("INSERT INTO Pet VALUES(1, 'Rusty', 'Dalmation', 4, 1)")
    cur.execute("INSERT INTO Pet VALUES(2, 'Bella', 'Alaskan Malamute', 3, 0)")
    cur.execute("INSERT INTO Pet VALUES(3, 'Max', 'Cocker Spaniel', 1, 0)")
    cur.execute("INSERT INTO Pet VALUES(4, 'Rocky', 'Beagle', 7, 0)")
    cur.execute("INSERT INTO Pet VALUES(5, 'Rufus', 'Cocker Spaniel', 1, 0)")
    cur.execute("INSERT INTO Pet VALUES(6, 'Spot', 'Bloodhound', 2, 1)")

    # Insert Data into Person_Pet Table
    cur.execute("INSERT INTO Person_Pet VALUES(1, 1)")
    cur.execute("INSERT INTO Person_Pet VALUES(1, 2)")
    cur.execute("INSERT INTO Person_Pet VALUES(2, 3)")
    cur.execute("INSERT INTO Person_Pet VALUES(2, 4)")
    cur.execute("INSERT INTO Person_Pet VALUES(3, 5)")
    cur.execute("INSERT INTO Person_Pet VALUES(3, 6)")
    
