import psycopg2

# connect to chinook database
# user and password necessary, use environment variable for it
connection = psycopg2.connect(database="chinook", user="postgres", password="postgresql")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records
# cursor.execute('SELECT * FROM "Artist"')
# Query 2 - select only the name column
# cursor.execute('SELECT "Name" FROM "Artist"')
# Query 3 - select only queen
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
# Query 4 - select only queen with id
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])
# Query 5 - select only albums with id 51
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])
# Query 6 - select tracks from queen
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])
# Query 7 - select tracks with no results
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Test"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)