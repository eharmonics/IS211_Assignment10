import sqlite3 as lite

conn = lite.connect('music.sqlite')

with conn:
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Artist")
    cur.execute("DROP TABLE IF EXISTS Genre")
    cur.execute("DROP TABLE IF EXISTS Album")
    cur.execute("DROP TABLE IF EXISTS Track")
    cur.execute(
        "CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT)")
    cur.execute(
        "CREATE TABLE Genre (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT)")
    cur.execute(
        "CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id INTEGER, title TEXT)")
    cur.execute("CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT, album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER)")

    cur.execute("INSERT INTO Artist (name) VALUES ('Led Zepplin')")
    cur.execute("INSERT INTO Artist (name) VALUES ('AC/DC')")

    cur.execute("INSERT INTO Genre (name) VALUES ('Rock')")
    cur.execute("INSERT INTO Genre (name) VALUES ('Metal')")

    cur.execute(
        "INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2)")
    cur.execute("INSERT INTO Album (title, artist_id) VALUES ('IV', 1)")

    cur.execute(
        "INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Black Dog', 2, 1, 297, 5, 0)")
    cur.execute(
        "INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Stairway', 2, 1, 482, 5, 0)")
    cur.execute(
        "INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('About to Rock', 1, 2, 313, 5, 0)")
    cur.execute(
        "INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Who Made Who', 1, 2, 207, 5, 0)")

    cur.execute("SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.ID and Track.album_id = Album.id and Album.artist_id = Artist.id")
    row = cur.fetchone()
    while row is not None:
        print(str(row[0]), str(row[1]), str(row[2]), str(row[3]))
        row = cur.fetchone()

    cur.execute("SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.ID and Track.album_id = Album.id and Album.artist_id = Artist.id ORDER BY Artist.name LIMIT 3")
    row = cur.fetchone()
    while row is not None:
        print(str(row[0]), str(row[1]), str(row[2]), str(row[3]))
        row = cur.fetchone()
