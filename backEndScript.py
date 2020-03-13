import sqlite3
# why shoude i tell you evry sthing muther fucker know it by your self bitch 

def coonect():
    coon = sqlite3.connect('booke.db')
    cur = coon.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, auther text, year INTEGER, isbn INTEGER)")
    coon.commit()
    coon.close()


def insert(title, auther, year, isbn):
    conn = sqlite3.connect('booke.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (null, ?, ?, ?, ?)", (title, auther, year, isbn))
    conn.commit()
    conn.close()



def view():
    conn = sqlite3.connect('booke.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book;")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title='', auther='', year='', isbn=''):
    conn = sqlite3.connect('booke.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR auther=? OR year=? OR isbn=?",(title, auther, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('booke.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,title,auther,year,isbn):
    conn = sqlite3.connect('booke.db')
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, auther=?, year=?, isbn=? WHERE id=?", (title, auther, year, isbn ,id))
    conn.commit()
    conn.close()

coonect()
