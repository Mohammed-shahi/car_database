import sqlite3

conn = sqlite3.connect('car.db')
cursor = conn.cursor()

# table
cursor.execute('''CREATE TABLE IF NOT EXISTS car (
                    id INTEGER PRIMARY KEY,
                    make TEXT NOT NULL,
                    model TEXT NOT NULL,
                    year INTEGER,
                    color TEXT,
                    price REAL
                    )''')

# insert here the data 
def insert_data():
    make = input("Enter car's makers: ")
    model = input("Enter car's model: ")
    year = int(input("Enter car's year: "))
    color = input("Enter car's color: ")
    price = float(input("Enter car's price: "))

    cursor.execute('''INSERT INTO car (make, model, year, color, price)
                      VALUES (?, ?, ?, ?, ?)''', (make, model, year, color, price))
    conn.commit()
    print("Data inserted successfully.")

#  display rows in the CARs table
def display_data():
    cursor.execute('''SELECT * FROM car''')
    rows = cursor.fetchall()
    if not rows:
        print("No data found in the database.")
    else:
        print("\nCAR Database:")
        print("ID  | Make  | Model  | Year  | Color  | Price")
        print("-----------------------------------------------")
        for row in rows:
            print(row[0], "|", row[1], "|", row[2], "|", row[3], "|", row[4], "|", row[5])


def main():
    while True:
        print("\n1. Insert Data\n2. Display Data\n3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            insert_data()
        elif choice == '2':
            display_data()
        elif choice == '3':
            print("DONE BUDDY ")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

conn.close()
