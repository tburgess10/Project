import sqlite3

# ** Enter your name and age here **
name = 'Cody'
age = 35

# Specify your SQLite file
db_file = 'names.sqlite'

# Connect to the SQLite database
conn = sqlite3.connect(db_file)

# Create a cursor object
cursor = conn.cursor()

# Insert a new record into the 'names' table
try:
    cursor.execute("INSERT INTO names (name, age) VALUES (?, ?);", (name, age))
    conn.commit()  # Commit the transaction
    print("Record inserted successfully.")
except sqlite3.Error as e:
    print(f"Error occurred: {e}")

# Retrieve and display all records from the 'names' table
try:
    cursor.execute("SELECT * FROM names;")
    rows = cursor.fetchall()

    # Display the rows
    print("\nContents of the 'names' table:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print(f"Error retrieving data: {e}")

# Close the connection
conn.close()
