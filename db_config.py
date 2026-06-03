import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Omsai9405',
        database='student_task_manager'
    )
    
    return connection