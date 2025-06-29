import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM users")
db.execute("DELETE FROM posts")
db.execute("DELETE FROM comments")

user_count = 1000
post_count = 10**6
comment_count = 10**7

for i in range(1, user_count + 1):
    db.execute("INSERT INTO users (username) VALUES (?)",
               ["user" + str(i)])

for i in range(1, post_count + 1):
    db.execute("INSERT INTO posts (title) VALUES (?)",
               ["post" + str(i)])

for i in range(1, comment_count + 1):
    user_id = random.randint(1, user_count)
    post_id = random.randint(1, comment_count)
    db.execute("""INSERT INTO comments (post_id, user_id, comment)
                  VALUES (?, ?, ?)""",
               ["message" + str(i), user_id, post_id])

db.commit()
db.close()
