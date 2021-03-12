import tkinter as tk
from datetime import  datetime
import sqlite3 as db


win_stock = tk.Tk()
db_connect = db.connect('Stock_DB')

Frame_1 = tk.Frame(win_stock)
Frame_1.pack()
L_frame = tk.LabelFrame(Frame_1)
L_frame.pack(padx=10,pady=10,fill='both',expand='yes')

L_frame_2 = tk.Frame(win_stock)
L_frame_2.pack(padx=10,pady=10,fill='both')





win_stock.geometry('500x500')
win_stock.mainloop()