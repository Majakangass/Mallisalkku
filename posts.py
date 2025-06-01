import db

def add_post(title, description, category, user_id):
    sql = """INSERT INTO posts (title, description, category, user_id) VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, description, category, user_id])