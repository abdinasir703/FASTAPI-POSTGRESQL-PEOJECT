from fastapi import FastAPI
import psycopg2

app = FastAPI()
@app.get("/")
def home():
    return {"message": "FastAPI is working"}

@app.get("/create_table")
def create_table():
    try:
        connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="Backend_database",
        user="postgres",
        password="YOUR PASSWD"
        )

        connection.close()

        return{"message": "PostgreSQL connected successfully"}
    except Exception as error:
        return {"error": str(error)}
    @app.get("/create-table")
    def create_table():
        connection = psycopg2.connect(
         host="localhost",
         port="5432",
         database="Backend_database",
         user="postgres",
         password="YOUR PASSWD"
        )
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE if not exists users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255,
        age INTEGER,""")

        connection.commit()
        cursor.close()
        connection.close()
        return {"message": "Users table created successfully"}

