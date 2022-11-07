import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = 'a'
port_id = 5432
conn = None


def create_table():

    # Establishing the connection
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Doping EMPLOYEE table if already exists.
    cursor.execute('DROP TABLE IF EXISTS botdb1')
    create_script = ''' CREATE TABLE IF NOT EXISTS botdb1 (
                                            id      int PRIMARY KEY,
                                            alert    varchar(100) NOT NULL,
                                            alert_response  varchar(540) NOT NULL) '''
    cursor.execute(create_script)
    conn.commit()
    print("Table created successfully........")
    cursor.close()


def insert_into_table(database_content):
    # Establishing the connection
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    insert_script = 'INSERT INTO botdb1 (id, alert,alert_response ) VALUES (%s, %s, %s)'
    for record in database_content:
        print("\n\n\n", record)
        cursor.execute(insert_script, record)
    print("*****************")
    cursor.execute('SELECT * FROM botdb1')
    for record in cursor.fetchall():
        print(record[0], record[1])
    conn.commit()
    cursor.close()
    conn.close()
