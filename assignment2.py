import psycopg2
from credentials import dbname, user, password, host

def connect_to_db(db_name, user, password, host):
    return psycopg2.connect(dbname=dbname,user=user, password=password, host=host)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

# QUERIES

create_table_statement = """
    CREATE TABLE test_table(
    id SERIAL PRIMARY KEY,
    name varchar(40) NOT NULL
    data JSONB
    );
"""

insert_statement= """
    INSERT INTO test_table(name, data) VALUES
    (
        'a row name',
        null
    ),
    (
        'I really hope this works!',
        '{"a":1 , "b":{"dog", "cat",42}, "c":true}' :: JSONB
    );
"""

table_check = "SELECT * FROM test_table"

if __name__ == "__main__":
    conn = connect_to_db(dbname,user,password,host)
    curs = conn.cursor()
    execute_query(curs, create_table_statement)
    execute_query(curs,insert_statement)
    conn.commit()
    print (execute_query(table_check))
