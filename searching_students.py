import tkinter as tk
import sqlite3
from functools import partial

conn = sqlite3.connect('db.sqlite3')

cursor = conn.cursor()

root = tk.Tk()

root.geometry('750x550')

root.title("Looking Students' details")

frame = tk.Frame(root).grid(pady=80,padx=100)

text = tk.StringVar()


search = tk.Entry(root,textvariable=text).grid(row=1,column=1,pady=10,ipady=3,ipadx=20,padx=10)


def executer(txt):

    data = (txt.get())

    info = cursor.execute("SELECT * FROM StudentsList where first_name=(?) or last_name=(?) order by id",(data.capitalize(),data.capitalize(),))

    obj = []

    j = 7


    for i in info:
        for n in range(len(i)):
            e = tk.Label(frame,text=i[n]).grid(row=j,column=n,padx=4)
        j = j + 1


    conn.commit()


executer = partial(executer,text)

btn = tk.Button(root,text="Search",command=executer).grid(column=2,row=1,padx=10)

root.mainloop()
