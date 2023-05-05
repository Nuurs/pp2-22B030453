import psycopg2
#from config import host,database,password,user
host = "127.0.0.1"
database = "postgres"
password = "0510"
user = "postgres"


try:
    
    #connect to exist database///
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

    
    connection.autocommit = True
    
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")


    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE Phone(
                id serial PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                nick_name varchar(50) NOT NULL);"""
        )
        
        print("[INFO] Table created succesfully")

    
    with connection.cursor() as cursor:
         cursor.execute(
            """INSERT INTO Phone (first_name, nick_name) VALUES
            ('Nursultan', '87768792999'), ('Iliyas', '87777777777'),
            ('Era', '87471234567')"""
         )
         print("[INFO] DATA was succesfully inserted")
    
    

except Exception as _ex:
    print("[INFO] Error while working with PostreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostreSQL connection closed")