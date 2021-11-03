import tkinter as tk
import sqlite3
from functools import partial

conn = sqlite3.connect("db.sqlite3")


win = tk.Tk()

win.geometry('750x550')
win.title("Adding Students' details")

frame = tk.Frame(win).grid(pady=80,padx=100)

f_name = tk.StringVar()
l_name = tk.StringVar()
ss = tk.StringVar()
ae = tk.StringVar()

label__f_name = tk.Label(frame,text='First Name: ').grid(row=4,column=3)
label__l_name = tk.Label(frame,text='Last Name: ').grid(row=5,column=3)
label__status = tk.Label(frame,text='Status: ').grid(row=6,column=3)
label__age = tk.Label(frame,text='Age: ').grid(row=7,column=3)

first_name = tk.Entry(frame, textvariable=f_name,width=30).grid(row=4,column=6,pady=10,ipady=3)
last_name = tk.Entry(frame,textvariable=l_name,width=30).grid(row=5,column=6,pady=10,ipady=3)
status = tk.Entry(frame,textvariable=ss,width=30).grid(row=6,column=6,pady=10,ipady=3)
age = tk.Entry(frame,textvariable=ae,width=30).grid(row=7,column=6,pady=10,ipady=3)


def executer(f,l,s,a):
	print('hello')

	first_name = (f.get())
	last_name = (l.get())
	status = (s.get())
	age = (a.get())

	print('%s' % last_name)
	
	params = (first_name,last_name,status,age)

	conn.execute("INSERT INTO StudentsList(first_name,last_name,status,age) VALUES (?,?,?,?)",params)

	conn.commit()

executer = partial(executer,f_name, l_name,ss,ae)

btn = tk.Button(win,text='Submit',command=executer).grid(column=6)


win.mainloop()
