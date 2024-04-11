import os
import sqlite3

connextions = sqlite3.connect("database.db")

cursor = connextions.cursor()

cursor.execute(
    """
               CREATE TABLE user (
    id AUTO_INCREMENT PRIMARY KEY NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    age INTEGER DEFAULT 0)"""
)

cursor.execute(
    "insert into user(id, username, password, age) values (1, 'a', 'app', 18)"
)
cursor.execute(
    "insert into user(id, username, password, age) values (2, 'b', 'bpp', 28)"
)


def select_all(cursor):
    cursor = cursor.execute("select id, username, password, age from user")

    for row in cursor:
        print(row)


print("select all. There should be two lines of data.")
select_all(cursor)
connextions.commit()

print("Update one")
cursor.execute("update user set username = 'new_name_a' where id = 1")
connextions.commit()

select_all(cursor)

print("Delete one")
cursor.execute("delete from user where id = 2")
connextions.commit()
select_all(cursor)

connextions.close()


os.remove("database.db")
