import re
import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

filename = input('Enter file name: ')
if len(filename) < 1:
    filename = '../files/mbox.txt'
fh = open(filename)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    domain = re.findall('^From.*[a-zA-Z0-9]\S+@(\S+[a-zA-Z])', line)[0]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))  # this is a one tuple
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org,count)
        VALUES (?,1)''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))
conn.commit()  # commit is the slowest part

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()
