import pymysql

# Database connection details
host = "localhost"
user = "root"
password = "1234"
database = "py_db_test"
table = "customer"

try:
    # Establish a connection
    connection = pymysql.connect(host=host, user=user, password=password, database=database)

    # Create a cursor
    with connection.cursor() as cursor:
        # Execute the SELECT query
        query = f"SELECT * FROM {table}"
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Print the data (example: in a simple format)
        for row in rows:
            print(row)

except pymysql.Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection (if it was established)
    if 'connection' in locals() and connection:  # Check if connection was established
        connection.close()




########################################################################################
'''
output:
('Jane Smith', '456 Oak Avenue')
'''