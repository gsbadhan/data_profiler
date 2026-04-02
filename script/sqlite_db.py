import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER,
    name TEXT,
    age INTEGER,
    salary REAL
)
""")

cursor.executemany(
    "INSERT INTO users VALUES (?, ?, ?, ?)",
    [
        (1, "Alice", 25, 50000),
        (2, "Bob", 30, 60000),
        (3, "Charlie", 35, None),
        (4, "David", None, 70000),
    ]
)

conn.commit()
conn.close()