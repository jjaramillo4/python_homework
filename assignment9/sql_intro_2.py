import sqlite3
import pandas as pd 

conn = None
try: 
    conn = sqlite3.connect("../db/lesson.db")
    db_df = pd.read_sql_query(sql="SELECT l.line_item_id, l.quantity, l.product_id, p.product_name, p.price " \
    "                               FROM line_items l  JOIN products p ON l.product_id = p.product_id", con=conn)
    print(db_df.head())

    db_df['total'] = db_df['quantity'] * db_df['price']
    print(db_df.head())

    db_df = db_df.groupby('product_id').agg({
        'line_item_id':'count',
        'total': 'sum',
        'product_name':'first'
    })
    print(db_df.head())

    db_df = db_df.sort_values('product_name')

    db_df.to_csv('order_summary.csv')
except Exception as e:
    print(f"Error connecting to database: {e}")
finally:
    if conn is not None:
        conn.close()