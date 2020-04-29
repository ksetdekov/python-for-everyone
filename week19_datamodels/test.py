import sqlite3
genre = 'stupic'
conn = sqlite3.connect('assignment.sqlite')
cur = conn.cursor()
cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
genre_id = cur.fetchone()
print(genre_id)
print(type(genre_id))
