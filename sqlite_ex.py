import sqlite3

connection = sqlite3.connect('tutorial.db')

c = connection.cursor()

#SQL

def create_table():
    c.excute('CREATE TABLE IF NOT EXISTS dados (id integer, unix real, keyword text, \
                    datestamp text, value real)')
    create_table()

def dataentry():
    
    c.execute("INSERT INTO dados VALUES(1, 1365952181.288, 'Python Sentiment',\
                       '2016-06-01 19:54:55', 5) ")
     c.execute("INSERT INTO dados VALUES(2, 1365952257.905, 'Python Sentiment',\
                       '2016-06-01 19:54:55',6) ")
      c.execute("INSERT INTO dados VALUES(3, 1365952264.123, 'Python Sentiment',\
                       '2016-06-01 19:54:55', 4) ")

      connection.commit()

      dataentry()
