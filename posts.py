import db

def add_post(title, description, category, user_id):
    sql = """INSERT INTO posts (title, description, category, user_id) VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, description, category, user_id])

def get_posts():
    sql = "SELECT id, title FROM posts ORDER BY id DESC"
    return db.query(sql)

def get_post(post_id):
    sql = """SELECT posts.id,
                    posts.title,
                    posts.description,
                    posts.category,
                    users.id user_id,
                    users.username
                FROM posts, users
                WHERE posts.user_id = users.id AND
                        posts.id = ?"""
    return db.query(sql, [post_id])[0]

def update_post(post_id, title, description, category):
    sql = """UPDATE posts SET title = ?,
                                description = ?,
                                category = ?
                                WHERE id = ?"""
    db.execute(sql, [title, description, category, post_id])