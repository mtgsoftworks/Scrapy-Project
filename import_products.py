import mysql.connector
import json

# Connect to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="petlebi"
)

# Create a cursor object
cursor = connection.cursor()

# Read the JSON file containing the product data
with open('petlebi_products.json', 'r') as f:
    data = json.load(f)

# Iterate over the product data and insert each product into the database
for product in data:
    # Prepare the SQL INSERT statement
    sql = "INSERT INTO petlebi (url, name, price, short_description, rating, number_of_reviews, product_description, sales_rank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (product['url'], product['name'], product['price'], product['short_description'], product['rating'], product['number_of_reviews'], product['product_description'], product['sales_rank'])

    # Execute the SQL statement
    cursor.execute(sql, values)

# Commit the changes to the database
connection.commit()

# Close the cursor and connection objects
cursor.close()
connection.close()