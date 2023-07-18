import psycopg2


def storeData(name, email, phone_number):

    conn = psycopg2.connect(
        host="18.224.227.40",
        port="5432",
        dbname="postgres",
        user="postgres",
        password="admin"
    )

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # Execute an SQL INSERT statement to store the data
    insert_query = "INSERT INTO public.chat_bot_lead(name, email, phone) VALUES (%s, %s, %s)"
    # Provide the actual data for insertion
    data = (name, email, phone_number)
    cur.execute(insert_query, data)

    # Commit the transaction and close the connection
    conn.commit()
    cur.close()
    conn.close()
    pass
