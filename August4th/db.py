import sqlite3
import time

def connect(target):
    return sqlite3.connect(target)

'''
New Paste
'''
def add_paste(pid, content, pType):
    db = connect('august4th.db')
    db.execute('INSERT INTO pastes(pid, content, pType) VALUES(?,?,?)', (pid, content, pType))
    db.commit()
    db.close()
