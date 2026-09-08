import sqlite3  

conn = None

try:
    conn = sqlite3.connect("../db/lesson.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Task 1:
    query = """
            SELECT o.order_id, SUM(p.price * l.quantity ) AS total_price
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
    query_2 = """
           SELECT c.customer_name, AVG(subquery.total_price) AS average_total_price
           FROM customers AS c
           LEFT JOIN
            ( SELECT o.customer_id AS customer_id_b, SUM(p.price * l.quantity ) AS total_price
             FROM orders AS o
                INNER JOIN line_items AS l ON o.order_id = l.order_id
                INNER JOIN products AS p ON l.product_id = p.product_id
                GROUP BY o.order_id, o.customer_id) AS subquery  ON subquery.customer_id_b = c.customer_id
            GROUP BY c.customer_id, c.customer_name
    """
    cursor.execute(query_2)
    rows_2 = cursor.fetchall()

    for customer_name, average_total_price in rows_2:
        if average_total_price is None:
            print(f"{customer_name}: no orders")
        else:
            print(f"{customer_name}: ${average_total_price:,.2f}")

    # Task 3:

    # Task 4:

except sqlite3.Error as e:
    print("database error:", e)
    
finally:
    if conn is not None:
        conn.close()