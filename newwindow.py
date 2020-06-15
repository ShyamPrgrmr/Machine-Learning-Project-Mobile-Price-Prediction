import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
import subprocess as sub

from prettytable import PrettyTable
import mysql.connector


x = PrettyTable()
x.field_names = ["Mobile name", "Battery Power", "Clock Speed","Front Camera","Internal Mem.","Processor Core","Primary Camera","screen_h","screen_w","Ram","Pixel_h","price"]

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="Shyam123@@"
)

sql_select_Query = "select * from mobile.mob"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()

for row in records:
    x.add_row([row[0],row[1],row[2],row[3],row[5],row[6],row[7],row[11],row[12],row[10],row[8],row[14]])

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1303x575+47+70")
        top.title("Mobiles")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.008, rely=0.017, relheight=0.939, relwidth=0.987)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(wrap="word")
        self.Text1.insert(tk.END, x)

if __name__ == '__main__':
    vp_start_gui()




