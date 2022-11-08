import psycopg2
import logging

from utils import db_connection_config

log_format = "%(asctime)s::%(levelname)s::%(name)s::" "%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(filename='logs\webscrapper.log',
                    level='DEBUG', format=log_format)


def create_table():
    # Establishing the connection
    config = db_connection_config()
    conn = psycopg2.connect(
        host=config["hostname"],
        dbname=config["database"],
        user=config["username"],
        password=config["pwd"],
        port=config["port_id"])
    cursor = conn.cursor()

    # Doping EMPLOYEE table if already exists.
    cursor.execute('DROP TABLE IF EXISTS botdb1')
    create_script = ''' CREATE TABLE IF NOT EXISTS botdb1 (
                                            id      int PRIMARY KEY,
                                            alert    varchar(100) NOT NULL,
                                            alert_response  varchar(540) NOT NULL) '''
    logging.debug("Executing the script ", create_script)
    cursor.execute(create_script)
    conn.commit()
    logging.info("------------- Successfully created the table ---------")
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

    insert_script = 'INSERT INTO botdb1 (id, alert,alert_response ) VALUES (%s, %s, %s)'

    for record in database_content:
        logging.debug("Inserting ", record, " into the table")
        cursor.execute(insert_script, record)
    conn.commit()
    cursor.close()
    conn.close()
