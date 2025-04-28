import sqlite3

# 1. Connect to a database (it will create StarTrekDB.db if it doesn't exist)
conn = sqlite3.connect('StarTrekDB.db')
cursor = conn.cursor()

# 2. Create the Roster table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# 3. Insert the given values
cursor.executemany('''
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
''', [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

# 4. Update the Name of 'Jadzia Dax' to 'Ezri Dax'
cursor.execute('''
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
''')

# 5. Display the Name and Age of everyone classified as 'Bajoran'
cursor.execute('''
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
''')

# 6. Fetch and print the result
results = cursor.fetchall()
for row in results:
    print(f"Name: {row[0]}, Age: {row[1]}")

# 7. Commit changes and close the connection
conn.commit()
conn.close()
