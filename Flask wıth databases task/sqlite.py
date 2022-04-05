import sqlite3


def conn_sqlite():
    global db, cursor
    try:
        db = sqlite3.connect('dataflask.db')
        cursor = db.cursor()

    except Exception as e:
        print(e)


def table_new():
    try:
        cursor.execute('create table sample(name text, batchid int, marks real)')
    except Exception as e:
        print(e)


def table_sampledata():
    try:
        cursor.execute("insert into sample values('nesibe', 234, 345)")
        cursor.execute("insert into sample values('ali', 254, 235)")
        cursor.execute("insert into sample values('kerem', 35, 5325)")
        cursor.execute("insert into sample values('nil', 234, 353)")
        cursor.execute("insert into sample values('muhammed', 232, 654)")
    except Exception as e:
        print(e)
        db.rollback()
    else:
        db.commit()


def fetching_data():
    try:
        data = cursor.execute('select * from sample').fetchall()
        for c in data:
            print(c)
        return data
    except Exception as e:
        print(e)

if __name__ == '__main__':
    conn_sqlite()
    table_new()
   # table_sampledata()
    fetching_data()