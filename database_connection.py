import psycopg2
import psycopg2.extras

from utils import db_connection_config


def create_table():

    # Establishing the connection
    config = db_connection_config()
    conn = psycopg2.connect(
        host=config["hostname"],
        dbname=config["database"],
        user=config["username"],
        password=config["pwd"],
        port=config["port_id"])
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Doping EMPLOYEE table if already exists.
    cursor.execute('DROP TABLE IF EXISTS documentationdb')
    create_script = ''' CREATE TABLE IF NOT EXISTS documentationdb (
                                            id      int PRIMARY KEY,
                                            alert    varchar(100) NOT NULL,
                                            alert_response  varchar(540) NOT NULL) '''
    cursor.execute(create_script)
    conn.commit()
    print("Table created successfully........")
    cursor.close()


def insert_into_table(database_content):
    config = db_connection_config()
    # Establishing the connection
    conn = psycopg2.connect(
        host=config["hostname"],
        dbname=config["database"],
        user=config["username"],
        password=config["pwd"],
        port=config["port_id"])
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    insert_script = 'INSERT INTO documentationdb (id, alert,alert_response ) VALUES (%s, %s, %s)'
    for record in database_content:
        print("\n\n\n", record)
        cursor.execute(insert_script, record)

    # cursor.execute('SELECT * FROM documentationdb')
    # for record in cursor.fetchall():
    #     print(record[0], record[1], record[2])
    conn.commit()
    cursor.close()
    conn.close()
