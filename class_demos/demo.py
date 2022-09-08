import psycopg2

connection = psycopg2.connect('dbname=example')

cursor= connection.cursor()

# drop any existing todos table
cursor.execute("DROP TABLE IF EXISTS table2;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)

cursor.execute('''
    CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
    );
    ''')

cursor.execute('INSERT INTO table2 (id,completed) VALUES (1, true);')

cursor.execute('INSERT INTO table2 (id,completed) VALUES (%s,%s);' , (2,True))

SQL='INSERT INTO table2 (id,completed) VALUES (%(id)s,%(completed)s);'
data={
    'id':3,
    'completed':False
}
cursor.execute(SQL , data)

cursor.execute('SELECT * from table2;')
result = cursor.fetchall()
##fetchmany(3)
##fetchone()
print(result)

connection.commit()

connection.close()
cursor.close()