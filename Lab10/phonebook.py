import psycopg2
import csv

def connect():
    return psycopg2.connect(
        database="lab10",
        user="postgres",
        password="12345678",
        host="localhost",
        port="5432"
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            surname VARCHAR(50),
            phone VARCHAR(20)
        )
    ''')
    conn.commit()
    conn.close()

def insert_from_csv(filename='Labs/Lab10/data.csv'):
    conn = connect()
    cur = conn.cursor()
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)",
                (row[0], row[1], row[2])
            )
    conn.commit()
    conn.close()
    print("📥 Data inserted from CSV")

def insert_from_console():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)",
        (name, surname, phone)
    )
    conn.commit()
    conn.close()
    print("✅ Inserted")

def update_user():
    name = input("Enter name to update: ")
    surname = input("Enter surname to update: ")
    new_phone = input("New phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE name = %s AND surname = %s",
        (new_phone, name, surname)
    )
    conn.commit()
    conn.close()
    print("🔁 Updated")

def query_data():
    print("\n📌 Filters:")
    print("1 - By name")
    print("2 - By surname")
    print("3 - By phone")
    print("4 - By part of name")

    option = input("Choose filter: ")
    conn = connect()
    cur = conn.cursor()

    if option == "1":
        value = input("Enter name: ")
        cur.execute("SELECT * FROM phonebook WHERE name = %s", (value,))
    elif option == "2":
        value = input("Enter surname: ")
        cur.execute("SELECT * FROM phonebook WHERE surname = %s", (value,))
    elif option == "3":
        value = input("Enter phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (value,))
    elif option == "4":
        value = input("Enter part of name: ")
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{value}%",))
    else:
        print("❌ Invalid option")
        conn.close()
        return

    results = cur.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No records found")

    conn.close()

def delete_user():
    value = input("Enter name or phone to delete: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (value, value))
    conn.commit()
    conn.close()
    print("🗑️ Deleted")

def menu():
    create_table()
    while True:
        print("\n📘 PhoneBook Menu")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update user")
        print("4. Query data")
        print("5. Delete user")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            insert_from_csv()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_user()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_user()
        elif choice == "0":
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid choice")

menu()
