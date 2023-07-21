import psycopg2
import os

DB_ENDPOINT = os.environ.get('DB_ENDPOINT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def delete_records():
    try:
        # Connect to the database
        connection = psycopg2.connect(
            host=DB_ENDPOINT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        # Create a cursor
        cursor = connection.cursor()

        # Your SQL query to delete records, modify as needed
        query = "DELETE FROM public.activities WHERE activities.expires_at < now();"

        # Execute the query
        cursor.execute(query)

        # Commit the changes
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        print("Records deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    delete_records()
