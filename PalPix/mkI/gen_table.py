from db_utils import db_connect

con = db_connect()
cur = con.cursor()

users_sql = """
CREATE TABLE users (
    id integer PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL)"""
cur.execute(users_sql)

movies_sql = """
CREATE TABLE movies (
    id integer PRIMARY KEY,
    title text NOT NULL)"""
cur.execute(movies_sql)


cur.execute('SELECT name FROM sqlite_master WHERE type="table"')
print(cur.fetchall())

