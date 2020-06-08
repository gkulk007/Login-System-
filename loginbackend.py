import sqlite3
from tkinter import messagebox

def connect():
    conn = sqlite3.connect("Database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS data(username,password,security_question,security_answer)")
    conn.commit()
    conn.close()

# connect()

def insert(username, password, security_question, security_answer):
    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES (?,?,?,?)",(username, password, security_question, security_answer))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    print(rows)



def update(username, security_answer,password):
    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()
    cur.execute("UPDATE data SET password=? WHERE username=? and security_answer=?",(password,username,security_answer))
    cur.execute("""SELECT security_answer
                          ,username
                   FROM data
                   WHERE security_answer=?
                    AND username=?""",
                (security_answer, username))
    if cur.fetchone():
        que = 'True'
    else:
        que = 'False'
    conn.commit()
    conn.close()
    return que


def login_verify(username, password):

    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()
    cur.execute("""SELECT password
                          ,username
                   FROM data
                   WHERE password=?
                    AND username=?""",
                (password, username))
    if cur.fetchone():
        que = 'True'
    else:
        que = 'False'
    conn.commit()
    conn.close()
    return que
