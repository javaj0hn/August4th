import sqlite3
import time

def connect(target):
    return sqlite3.connect(target)

'''
Get Paste
'''
def getPaste(pid):
    db = connect('august4th.db')
    paste = db.execute('SELECT * FROM pastes WHERE pid = ?', (pid,)).fetchall()
    db.commit()
    db.close()
    return paste

'''
New Paste
'''
def add_paste(pid, content, pType):
    db = connect('august4th.db')
    db.execute('INSERT INTO pastes(pid, content, pType) VALUES(?,?,?)', (pid, content, pType))
    db.commit()
    db.close()

'''
Paste Gallery
'''
def getPasteGallery():
    db = connect('august4th.db')
    pastes = db.execute('SELECT * FROM pastes')
    db.commit()
    #db.close()
    return pastes
