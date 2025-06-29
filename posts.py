import db
from collections import defaultdict

def get_all_classes():
    sql = """SELECT title, value FROM classes ORDER BY id"""
    result = db.query(sql)

    classes = defaultdict(list)
    for title, value in result:
        classes[title].append(value)

    return dict(classes)

def add_post(title, description, category, user_id, classes):
    sql = """INSERT INTO posts (title, description, category, user_id) VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, description, category, user_id])

    post_id = db.last_insert_id()

    sql = """INSERT INTO post_classes (post_id, title, value) VALUES (?, ?, ?)"""
    for class_title, class_value in classes:
        db.execute(sql, [post_id, class_title, class_value])

    return post_id

def add_comment(post_id, user_id, comment):
    sql = """INSERT INTO comments (post_id, user_id, comment) VALUES (?, ?, ?)"""
    db.execute(sql, [post_id, user_id, comment])

def get_comments(post_id):
    sql = """SELECT comments.comment, users.id user_id, users.username
                FROM comments
                    JOIN users ON comments.user_id = users.id
                WHERE comments.post_id = ?
                ORDER BY comments.id DESC"""
    return db.query(sql, [post_id])

def get_images(post_id):
    sql = """SELECT id FROM images WHERE post_id = ?"""
    return db.query(sql, [post_id])

def add_image(post_id, image):
    sql = """INSERT INTO images (post_id, image) VALUES (?, ?)"""
    db.execute(sql, [post_id, image])

def get_image(image_id):
    sql = """SELECT image FROM images WHERE id = ?"""
    result = db.query(sql, [image_id])
    return result[0][0] if result else None

def remove_image(post_id, image_id):
    sql = """DELETE FROM images WHERE id = ? AND post_id = ?"""
    db.execute(sql, [image_id, post_id])

def get_classes(post_id):
    sql = """SELECT title, value FROM post_classes WHERE post_id = ?"""
    return db.query(sql, [post_id])

def get_posts():
    sql = """SELECT posts.id, posts.title, users.id user_id, users.username,
                    COUNT(comments.id) comment_count
                FROM posts JOIN users ON posts.user_id = users.id
                    LEFT JOIN comments ON posts.id = comments.post_id
                GROUP BY posts.id
                ORDER BY posts.id DESC"""
    return db.query(sql)

def get_post(post_id):
    sql = """SELECT posts.id, posts.title, posts.description,
                    posts.category, users.id user_id, users.username
                FROM posts, users
                WHERE posts.user_id = users.id AND posts.id = ?"""
    result = db.query(sql, [post_id])
    return result[0] if result else None

def update_post(post_id, title, description, category, classes):
    sql = """UPDATE posts SET title = ?,
                    description = ?,
                    category = ?
                WHERE id = ?"""
    db.execute(sql, [title, description, category, post_id])

    sql = """DELETE FROM post_classes WHERE post_id = ?"""
    db.execute(sql, [post_id])

    sql = """INSERT INTO post_classes (post_id, title, value) VALUES (?, ?, ?)"""
    for class_title, class_value in classes:
        db.execute(sql, [post_id, class_title, class_value])

def remove_post(post_id):
    sql = """DELETE FROM post_classes WHERE post_id = ?"""
    db.execute(sql, [post_id])
    sql = """DELETE FROM comments WHERE post_id = ?"""
    db.execute(sql, [post_id])
    sql = """DELETE FROM images WHERE post_id = ?"""
    db.execute(sql, [post_id])
    sql = """DELETE FROM posts WHERE id = ?"""
    db.execute(sql, [post_id])

def find_posts(query):
    sql = """SELECT id, title
                FROM posts
                WHERE title LIKE ? OR description LIKE ? OR category LIKE ?
                ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like, like])

def get_posts_index(page, page_size):
    sql = """SELECT posts.id, posts.title, COUNT(posts.id) total, users.id user_id, users.username,
                    COUNT(comments.id) comment_count
                FROM posts JOIN users ON posts.user_id = users.id
                    LEFT JOIN comments ON posts.id = comments.post_id
                GROUP BY posts.id
                ORDER BY posts.id DESC
                LIMIT ? OFFSET ?"""

    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, [limit, offset])

def post_count():
    sql = "SELECT COUNT(*) FROM posts"
    return db.query(sql)[0][0]