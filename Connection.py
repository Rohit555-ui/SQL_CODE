import pymysql

import logging

logging.basicConfig(filename='outage_data.log', level=logging.CRITICAL, format='%(asctime)s:%(levelname)s:%(message)s')

def get_data_base_connection():
    connection = None
    try:
        connection = pymysql.connect(host='brpl-test-db.cea15vlld93o.us-east-1.rds.amazonaws.com', user='probusdev', passwd='probusdev', db='management')
    except Exception as e:
        log.error("Database connection refushed!!!")

    return connection
