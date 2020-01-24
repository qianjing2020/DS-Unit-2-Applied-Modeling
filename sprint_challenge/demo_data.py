import sqlite3
# Establish connection
conn = sqlite3.connect('demo_data.sqlite3')
cur = conn.cursor()
# Create table
create_table_statement = """
CREATE TABLE demo
(s CHAR(1) PRIMARY KEY NOT NULL,
x INT,
y INT);"""
cur.execute(create_table_statement)
# Insert data into table
cur.execute("""INSERT INTO demo (s, x, y) VALUES ('g', 3, 9)""")
cur.execute("""INSERT INTO demo (s, x, y) VALUES ('v', 5, 7)""")
cur.execute("""INSERT INTO demo (s, x, y) VALUES ('f', 8, 7)""")
conn.commit()

print('Number of rows in table:')
print(cur.execute("""SELECT COUNT(*) FROM demo""").fetchall())
conn.commit()

print('Number of rows with both x and y =5:')
print(cur.execute("""SELECT COUNT(*) FROM demo
WHERE x=5 AND y=5""").fetchall())
conn.commit()

print('Count of unique values of y:')
print(cur.execute("""SELECT COUNT(DISTINCT y) FROM demo""").fetchall())
conn.commit()

conn.close()