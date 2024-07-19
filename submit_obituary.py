from flask import Flask, render_template, request
import mysql.connector
import re  # For input validation (optional)

app = Flask(__name__)

# Database configuration
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""  # Not recommended for production; use a strong password
MYSQL_DB = "obituary_platform"

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        return connection
    except mysql.connector.Error as err:
        print(err)
        return None

@app.route("/submit_obituary", methods=["POST"])
def submit_obituary():
    # Capture form data
    name = request.form["name"]
    date_of_birth = request.form["date_of_birth"]  # Consider validation using re
    date_of_death = request.form["date_of_death"]  # Consider validation using re
    content = request.form["content"]
    author = request.form["author"]

    # Connect to database
    connection = connect_to_database()

    if connection:
        try:
            cursor = connection.cursor()
            # Prepared statement with parameter placeholders
            sql = """INSERT INTO obituaries (name, date_of_birth, date_of_death, content, author) VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (name, date_of_birth, date_of_death, content, author))
            connection.commit()
            connection.close()
            return "Obituary submitted successfully!"
        except mysql.connector.Error as err:
            print(err)
            return "Error submitting obituary."
    else:
        return "Error connecting to database."

if __name__ == "__main__":
    app.run(debug=True)
