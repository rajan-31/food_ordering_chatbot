import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("food.db")

cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM food_items;'):
    print(row)

# Be sure to close the connection
con.close()