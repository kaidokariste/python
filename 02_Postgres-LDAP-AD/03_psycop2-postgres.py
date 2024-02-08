import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


def get_connection():
    """
    Get database connection handle
    """
    return psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" %
                            (os.getenv('DB_DATABASE'),
                             os.getenv('DB_USERNAME'),
                             os.getenv('DB_HOSTNAME'),
                             os.getenv('DB_PASSWORD')))


def db_query():
    query = "SELECT * FROM myschema.env"
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result
    except psycopg2.Error as err:
        print(err)


if __name__ == '__main__':
    print(db_query())
