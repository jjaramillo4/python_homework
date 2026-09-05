import sqlite3
import pandas as pd 

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))

    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_magazine(cursor, name, publisher_name):
    try:
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
        results = cursor.fetchall()
        if len(results) == 0:
            print(f"Publisher {publisher_name} does not exist in the database.")
            return
        publisher_id = results[0][0]

        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?,?)", (name, publisher_id))
    
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_subscriber(cursor, name, address):
        cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
        results = cursor.fetchall()
        if len(results) > 0:
            print(f"{name} with address {address} is already in the database.")
            return
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?,?)", (name, address))

def add_subscription(cursor, subscriber_name, magazine_name, expiration_date):
    try:
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", (subscriber_name,))
        subscriber_results = cursor.fetchall()
        if len(subscriber_results) == 0:
            print(f"Subscriber {subscriber_name} does not exist in the database.")
            return
        subscriber_id = subscriber_results[0][0]

        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
        magazine_results = cursor.fetchall()
        if len(magazine_results) == 0:
            print(f"Magazine {magazine_name} does not exist in the database.")
            return
        magazine_id = magazine_results[0][0]
        
        cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
        if len(cursor.fetchall()) > 0:
            print(f"Subscription for {subscriber_name} to {magazine_name} already exists.")
            return

        cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?,?,?)", (subscriber_id, magazine_id, expiration_date))
    
    except sqlite3.IntegrityError:
        print(f"Subscription is already in the database.")

# Task 1
conn = None
try: 
    with sqlite3.connect("../db/magazines.db") as conn:
        cursor = conn.cursor()
        print("Connected to the database successfully.") 
       
        # Task 2
        cursor.execute('''CREATE TABLE IF NOT EXISTS publishers (
                            publisher_id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL UNIQUE
                        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS magazines(
                            magazine_id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL UNIQUE,
                            publisher_id INTEGER NOT NULL,
                            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
                       )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS subscribers(
                            subscriber_id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            address TEXT NOT NULL
                       )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS subscriptions(
                            subscription_id INTEGER PRIMARY KEY,
                            subscriber_id INTEGER,
                            magazine_id INTEGER,
                            expiration_date TEXT NOT NULL,
                            UNIQUE(subscriber_id, magazine_id),
                            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
                            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)        
                       )''')
        # Task 3
        conn.execute("PRAGMA foreign_keys = 1;")

        add_publisher(cursor, "Conde Nast")
        add_publisher(cursor, "Hearst")
        add_publisher(cursor, "Meredith")

        add_magazine(cursor, "Vogue", "Conde Nast")
        add_magazine(cursor, "Wired", "Conde Nast")
        add_magazine(cursor, "Cosmopolitan", "Hearst")
        add_magazine(cursor, "Better Homes and Gardens", "Meredith")

        add_subscriber(cursor, "John Doe", "123 Main St, Detroit, MI")
        add_subscriber(cursor, "Jane Smith", "456 Oak St, Los Angeles, CA")
        add_subscriber(cursor, "Alice Johnson", "789 Pine St, New York, NY")

        add_subscription(cursor, "John Doe", "Vogue", "2024-12-31")
        add_subscription(cursor, "John Doe", "Wired", "2025-01-31")
        add_subscription(cursor, "Alice Johnson", "Cosmopolitan", "2024-12-31")
        add_subscription(cursor, "Jane Smith", "Better Homes and Gardens", "2025-06-30")    
        add_subscription(cursor, "Jane Smith", "Vogue", "2025-06-30")
        conn.commit()

        # Task 4  
        cursor.execute('''SELECT *
                          FROM subscribers''')
        rows = cursor.fetchall() 
        print("\n Subscribers:")
        for row in rows:
            print(row)
        

        cursor.execute('''SELECT *
                          FROM magazines
                          ORDER BY name''')  
        rows = cursor.fetchall()
        print("\nMagazines sorted by name:")
        for row in rows:
            print(row)

        cursor.execute('''SELECT m.name AS magazine_name, p.name AS publisher_name
                          FROM magazines m
                          INNER JOIN publishers p ON m.publisher_id = p.publisher_id
                          WHERE p.name = 'Conde Nast'
                       ''')
        rows = cursor.fetchall()
        print("\nMagazines published by Conde Nast:")
        for row in rows:
            print(row)


except Exception as e:
    print(f"Error occurred while creating the table: {e}")

finally:
    if conn is not None:
        conn.close()
