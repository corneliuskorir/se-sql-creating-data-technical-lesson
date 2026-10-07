import sqlite3
import pandas as pd

conn = sqlite3.connect("my_db.sqlite")
cur = conn.cursor()


# remove table entirely (delete table with all the data)

# cur.execute("""
# DROP TABLE users;
# """)

# define data model using CREATE TABLE

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
sign_date DATE DEFAULT CURRENT_DATE
);
""")

# alter table to add new row

# cur.execute("""
# ALTER TABLE users ADD COLUMN phone_number TEXT;
# """)


#!! all the above commands need only to be run once
# ....................................................

# cur.execute("""
# INSERT INTO users (name , email)
# VALUES ('Cornelius Korir','cone@gmail.com'),
# ('Mathew korir','mat@mat.com');
# """)

# conn.commit()

# select users from users table
# cur.execute("""SELECT * FROM users;""")

# modify data using UPDATE
# print("before edit\n", cur.fetchall())

# cur.execute("""UPDATE users
# SET email = 'mat@mathew.com' WHERE email = 'mat@mat.com'""")

# cur.execute("""SELECT * FROM users;""")

# print("afters edit\n", cur.fetchall())

# remove unessesary data, delete
# cur.execute("""
# INSERT INTO users (name, email) VALUES ('Test User', 'test@test.com');""")

# conn.commit()

cur.execute("""SELECT * FROM users;""")
print(cur.fetchall())

# cur.execute("""DELETE FROM users
# WHERE name = 'Test User';""")

# conn.commit()

print(cur.fetchall())

conn.close()
