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

    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';")
    customer_id = cursor.fetchone()[0]

    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris';")
    employee_id = cursor.fetchone()[0]

    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5;")
    product_ids = cursor.fetchall()

    cursor.execute(
        "INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, '2026-09-08') RETURNING order_id;",
        (customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    cursor.executemany("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)", [(order_id, p[0], 10) for p in product_ids])

    conn.commit()

    cursor.execute(
        "SELECT l.line_item_id, p.product_name, l.quantity "
        "FROM line_items AS l "
        "JOIN products AS p ON l.product_id = p.product_id "
        "WHERE l.order_id = ?;",
        (order_id,))
    rows_3 = cursor.fetchall()

    print(f"Created order {order_id} with {len(rows_3)} line items:")
    for line_item_id, product_name, quantity in rows_3:
        print(f"  line item {line_item_id}: {quantity} x {product_name}")

    # Task 4:
    query_3 = """
         SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS count_of_orders
         FROM employees AS e
         INNER JOIN orders AS o ON e.employee_id = o.employee_id
         GROUP BY e.employee_id, e.first_name, e.last_name
         HAVING COUNT(o.order_id) > 5
    """
    cursor.execute(query_3)
    rows_4 = cursor.fetchall()

    for employee_id, first_name, last_name, count_of_orders in rows_4:
        print(f"{first_name} {last_name} (ID: {employee_id}): {count_of_orders} orders")


except sqlite3.Error as e:
    print("database error:", e)
    if conn is not None:
        conn.rollback()
    
finally:
    if conn is not None:
        conn.close()
