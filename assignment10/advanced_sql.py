import sqlite3  

conn = None

try:
    conn = sqlite3.connect("../db/lesson.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Task 1:
    query = """
            SELECT o.order_id, SUM(p.price * l.quantity ) AS Total
            FROM orders AS o
            INNER JOIN line_items AS l ON o.order_id = l.order_id
            INNER JOIN products AS p ON l.product_id = p.product_id
            GROUP BY o.order_id
            ORDER BY o.order_id LIMIT 5        
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    for order_id, total in rows:
     print(f"Order {order_id}: ${total:,.2f}")

    # Task 2:

    # Task 3:

    # Task 4:

except sqlite3.Error as e:
    print("database error:", e)
    
finally:
    if conn is not None:
        conn.close()