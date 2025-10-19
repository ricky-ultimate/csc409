import sqlite3

# Connect or create DB
conn = sqlite3.connect("students.db")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS Students (
    MatricNo TEXT PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    CGPA REAL
)
""")

# Insert data
data = [
    ('011', 'Tolu Fabiyi', 'Software Engineering', 3.8),
    ('012', 'Ruth Oluwa', 'IT', 4.5),
    ('013', 'David Chuks', 'Computer Science', 3.5),
    ('014', 'Hanna Abiodun', 'Software Engineering', 3.9),
]
cur.executemany("INSERT OR REPLACE INTO Students VALUES (?, ?, ?, ?)", data)
conn.commit()

# Run queries
print("\nAll Students:")
for row in cur.execute("SELECT * FROM Students"):
    print(row)

print("\nSearch by MatricNo = 012:")
for row in cur.execute("SELECT * FROM Students WHERE MatricNo='012'"):
    print(row)

print("\nStudents with CGPA > 3.5:")
for row in cur.execute("SELECT Name, CGPA FROM Students WHERE CGPA > 3.5"):
    print(row)

conn.close()
