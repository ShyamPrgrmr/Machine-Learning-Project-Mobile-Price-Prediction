import sys
import numpy as np
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score 
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, LogisticRegression
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler
import mysql.connector
import os
from PIL import Image, ImageTk

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
def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
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
        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec' 
        font11 = "-family gothic -size 15 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("1240x599+110+63")
        top.title("Mobile Pice Predictor")
        top.configure(background="#6cd873")
        
        self.data = pd.read_csv("data.csv")
        self.test_data = pd.read_csv("test.csv")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.36, rely=0.017, relheight=0.977
                , relwidth=0.258)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#6cd873")
        self.Frame1.configure(highlightbackground="#5dd8c8")

        self.M1 = tk.Button(self.Frame1,command = self.c1)
        self.M1.place(relx=0.110, rely=0.034, height=35, width=260)
        self.M1.configure(text='''Redmi note 7 pro''')

        self.M2 = tk.Button(self.Frame1,command = self.c2)
        self.M2.place(relx=0.110, rely=0.103, height=35, width=260)
        self.M2.configure(activebackground="#f9f9f9")
        self.M2.configure(text='''Realme xt''')

        self.M3 = tk.Button(self.Frame1,command = self.c3)
        self.M3.place(relx=0.110, rely=0.171, height=35, width=260)
        self.M3.configure(activebackground="#f9f9f9")
        self.M3.configure(text='''Samsung galaxy x''')

        self.M4 = tk.Button(self.Frame1,command = self.c4)
        self.M4.place(relx=0.110, rely=0.239, height=35, width=260)
        self.M4.configure(activebackground="#f9f9f9")
        self.M4.configure(text='''Samsung A1''')

        self.M5 = tk.Button(self.Frame1,command = self.c5)
        self.M5.place(relx=0.110, rely=0.308, height=35, width=260)
        self.M5.configure(activebackground="#f9f9f9")
        self.M5.configure(text='''Lenovo k1''')

        self.M6 = tk.Button(self.Frame1,command = self.c6)
        self.M6.place(relx=0.110, rely=0.376, height=35, width=260)
        self.M6.configure(activebackground="#f9f9f9")
        self.M6.configure(text='''One plus 6T''')

        self.M7 = tk.Button(self.Frame1,command = self.c7)
        self.M7.place(relx=0.110, rely=0.444, height=35, width=260)
        self.M7.configure(activebackground="#f9f9f9")
        self.M7.configure(text='''Coolpad cool 1''')

        self.M9 = tk.Button(self.Frame1,command = self.c9)
        self.M9.place(relx=0.110, rely=0.581, height=35, width=260)
        self.M9.configure(activebackground="#f9f9f9")
        self.M9.configure(text='''Samsung Galax A2''')

        self.M8 = tk.Button(self.Frame1,command = self.c8)
        self.M8.place(relx=0.110, rely=0.513, height=35, width=260)
        self.M8.configure(activebackground="#f9f9f9")
        self.M8.configure(text='''Vivo x pro''')

        self.M10 = tk.Button(self.Frame1,command = self.c10)
        self.M10.place(relx=0.110, rely=0.65, height=35, width=260)
        self.M10.configure(activebackground="#f9f9f9")
        self.M10.configure(text='''Nokia asha''')

        self.M11 = tk.Button(self.Frame1,command = self.c11)
        self.M11.place(relx=0.110, rely=0.718, height=35, width=260)
        self.M11.configure(activebackground="#f9f9f9")
        self.M11.configure(text='''Micromax zono''')

        self.M12 = tk.Button(self.Frame1,command = self.c12)
        self.M12.place(relx=0.110, rely=0.786, height=35, width=260)
        self.M12.configure(activebackground="#f9f9f9")
        self.M12.configure(text='''Huawei d1''')

        self.M13 = tk.Button(self.Frame1,command = self.c13)
        self.M13.place(relx=0.110, rely=0.855, height=35, width=260)
        self.M13.configure(activebackground="#f9f9f9")
        self.M13.configure(text='''Honor 6x''')

        self.M14 = tk.Button(self.Frame1,command = self.c14)
        self.M14.place(relx=0.110, rely=0.923, height=35, width=260)
        self.M14.configure(activebackground="#f9f9f9")
        self.M14.configure(text='''One plus 7T''')

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.013, rely=0.017, relheight=0.977, relwidth=0.35)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#6cd873")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.024, rely=0.017, height=15, width=139)
        self.Label1.configure(text='''Name of Mobile''')

        self.name = tk.Entry(self.Frame2)
        self.name.place(relx=0.386, rely=0.017,height=17, relwidth=0.569)
        self.name.configure(background="white")
        self.name.configure(font="TkFixedFont")

        self.Label2 = tk.Label(self.Frame2)
        self.Label2.place(relx=0.024, rely=0.12, height=25, width=389)
        self.Label2.configure(font=font11)
        self.Label2.configure(text='''Fill Information''')

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.024, rely=0.205, height=15, width=95)
        self.Label3.configure(text='''Battery Power''')

        self.Label3_18 = tk.Label(self.Frame2)
        self.Label3_18.place(relx=0.024, rely=0.239, height=15, width=95)
        self.Label3_18.configure(activebackground="#f9f9f9")
        self.Label3_18.configure(text='''Clock Speed''')

        self.Label3_19 = tk.Label(self.Frame2)
        self.Label3_19.place(relx=0.024, rely=0.274, height=15, width=95)
        self.Label3_19.configure(activebackground="#f9f9f9")
        self.Label3_19.configure(text='''Front Camera''')

        self.Label3_20 = tk.Label(self.Frame2)
        self.Label3_20.place(relx=0.024, rely=0.308, height=15, width=95)
        self.Label3_20.configure(activebackground="#f9f9f9")
        self.Label3_20.configure(text='''Internal mem.''')

        self.Label3_21 = tk.Label(self.Frame2)
        self.Label3_21.place(relx=0.024, rely=0.342, height=15, width=95)
        self.Label3_21.configure(activebackground="#f9f9f9")
        self.Label3_21.configure(text='''Mobile Depth''')

        self.Label3_22 = tk.Label(self.Frame2)
        self.Label3_22.place(relx=0.024, rely=0.376, height=15, width=105)
        self.Label3_22.configure(activebackground="#f9f9f9")
        self.Label3_22.configure(text='''Processor core''')

        self.Label3_23 = tk.Label(self.Frame2)
        self.Label3_23.place(relx=0.024, rely=0.41, height=15, width=105)
        self.Label3_23.configure(activebackground="#f9f9f9")
        self.Label3_23.configure(text='''Primary Camera''')

        self.Label3_24 = tk.Label(self.Frame2)
        self.Label3_24.place(relx=0.024, rely=0.444, height=15, width=95)
        self.Label3_24.configure(activebackground="#f9f9f9")
        self.Label3_24.configure(text='''Pixel height''')

        self.Label3_25 = tk.Label(self.Frame2)
        self.Label3_25.place(relx=0.024, rely=0.479, height=15, width=95)
        self.Label3_25.configure(activebackground="#f9f9f9")
        self.Label3_25.configure(text='''Pixel width''')

        self.Label3_26 = tk.Label(self.Frame2)
        self.Label3_26.place(relx=0.024, rely=0.513, height=15, width=95)
        self.Label3_26.configure(activebackground="#f9f9f9")
        self.Label3_26.configure(text='''Ram''')

        self.Label3_27 = tk.Label(self.Frame2)
        self.Label3_27.place(relx=0.024, rely=0.547, height=15, width=95)
        self.Label3_27.configure(activebackground="#f9f9f9")
        self.Label3_27.configure(text='''Screen height''')

        self.Label3_28 = tk.Label(self.Frame2)
        self.Label3_28.place(relx=0.024, rely=0.581, height=15, width=95)
        self.Label3_28.configure(activebackground="#f9f9f9")
        self.Label3_28.configure(text='''Screen width''')

        self.Label3_29 = tk.Label(self.Frame2)
        self.Label3_29.place(relx=0.024, rely=0.615, height=15, width=95)
        self.Label3_29.configure(activebackground="#f9f9f9")
        self.Label3_29.configure(text='''Talktime''')

        self.output = tk.Text(self.Frame2)
        self.output.place(relx=0.024, rely=0.735, relheight=0.220
                , relwidth=0.954)
        self.output.configure(background="white")
        self.output.configure(font="TkTextFont")
        self.output.configure(selectbackground="#c4c4c4")
        self.output.configure(wrap="word")

        self.f1 = tk.Entry(self.Frame2)
        self.f1.place(relx=0.265, rely=0.205,height=17, relwidth=0.617)
        self.f1.configure(background="white")
        self.f1.configure(font="TkFixedFont")
        self.f1.configure(selectbackground="#c4c4c4")

        self.f2 = tk.Entry(self.Frame2)
        self.f2.place(relx=0.265, rely=0.239,height=17, relwidth=0.617)
        self.f2.configure(background="white")
        self.f2.configure(font="TkFixedFont")
        self.f2.configure(selectbackground="#c4c4c4")

        self.f3 = tk.Entry(self.Frame2)
        self.f3.place(relx=0.265, rely=0.274,height=17, relwidth=0.617)
        self.f3.configure(background="white")
        self.f3.configure(font="TkFixedFont")
        self.f3.configure(selectbackground="#c4c4c4")

        self.f4 = tk.Entry(self.Frame2)
        self.f4.place(relx=0.265, rely=0.308,height=17, relwidth=0.617)
        self.f4.configure(background="white")
        self.f4.configure(font="TkFixedFont")
        self.f4.configure(selectbackground="#c4c4c4")

        self.f5 = tk.Entry(self.Frame2)
        self.f5.place(relx=0.265, rely=0.342,height=17, relwidth=0.617)
        self.f5.configure(background="white")
        self.f5.configure(font="TkFixedFont")
        self.f5.configure(selectbackground="#c4c4c4")

        self.f6 = tk.Entry(self.Frame2)
        self.f6.place(relx=0.265, rely=0.376,height=17, relwidth=0.617)
        self.f6.configure(background="white")
        self.f6.configure(font="TkFixedFont")
        self.f6.configure(selectbackground="#c4c4c4")

        self.f7 = tk.Entry(self.Frame2)
        self.f7.place(relx=0.265, rely=0.41,height=17, relwidth=0.617)
        self.f7.configure(background="white")
        self.f7.configure(font="TkFixedFont")
        self.f7.configure(selectbackground="#c4c4c4")

        self.f8 = tk.Entry(self.Frame2)
        self.f8.place(relx=0.265, rely=0.444,height=17, relwidth=0.617)
        self.f8.configure(background="white")
        self.f8.configure(font="TkFixedFont")
        self.f8.configure(selectbackground="#c4c4c4")

        self.f9 = tk.Entry(self.Frame2)
        self.f9.place(relx=0.265, rely=0.479,height=17, relwidth=0.617)
        self.f9.configure(background="white")
        self.f9.configure(font="TkFixedFont")
        self.f9.configure(selectbackground="#c4c4c4")

        self.f10 = tk.Entry(self.Frame2)
        self.f10.place(relx=0.265, rely=0.513,height=17, relwidth=0.617)
        self.f10.configure(background="white")
        self.f10.configure(font="TkFixedFont")
        self.f10.configure(selectbackground="#c4c4c4")

        self.f11 = tk.Entry(self.Frame2)
        self.f11.place(relx=0.265, rely=0.547,height=17, relwidth=0.617)
        self.f11.configure(background="white")
        self.f11.configure(font="TkFixedFont")
        self.f11.configure(selectbackground="#c4c4c4")

        self.f12 = tk.Entry(self.Frame2)
        self.f12.place(relx=0.265, rely=0.581,height=17, relwidth=0.617)
        self.f12.configure(background="white")
        self.f12.configure(font="TkFixedFont")
        self.f12.configure(selectbackground="#c4c4c4")

        self.f13 = tk.Entry(self.Frame2)
        self.f13.place(relx=0.265, rely=0.615,height=17, relwidth=0.617)
        self.f13.configure(background="white")
        self.f13.configure(font="TkFixedFont")
        self.f13.configure(selectbackground="#c4c4c4")

        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.892, rely=0.205, height=15, width=25)
        self.Label4.configure(text='''Mah''')

        self.Label4_40 = tk.Label(self.Frame2)
        self.Label4_40.place(relx=0.892, rely=0.239, height=15, width=25)
        self.Label4_40.configure(activebackground="#f9f9f9")
        self.Label4_40.configure(text='''ghz''')

        self.Label4_41 = tk.Label(self.Frame2)
        self.Label4_41.place(relx=0.892, rely=0.274, height=15, width=25)
        self.Label4_41.configure(activebackground="#f9f9f9")
        self.Label4_41.configure(text='''MP''')

        self.Label4_42 = tk.Label(self.Frame2)
        self.Label4_42.place(relx=0.892, rely=0.308, height=15, width=25)
        self.Label4_42.configure(activebackground="#f9f9f9")
        self.Label4_42.configure(text='''MB''')

        self.Label4_43 = tk.Label(self.Frame2)
        self.Label4_43.place(relx=0.892, rely=0.342, height=15, width=25)
        self.Label4_43.configure(activebackground="#f9f9f9")
        self.Label4_43.configure(text='''inch''')

        self.Label4_44 = tk.Label(self.Frame2)
        self.Label4_44.place(relx=0.892, rely=0.376, height=15, width=25)
        self.Label4_44.configure(activebackground="#f9f9f9")
        self.Label4_44.configure(text='''num''')

        self.Label4_45 = tk.Label(self.Frame2)
        self.Label4_45.place(relx=0.892, rely=0.41, height=15, width=25)
        self.Label4_45.configure(activebackground="#f9f9f9")
        self.Label4_45.configure(text='''Px''')

        self.Label4_46 = tk.Label(self.Frame2)
        self.Label4_46.place(relx=0.892, rely=0.444, height=15, width=25)
        self.Label4_46.configure(activebackground="#f9f9f9")
        self.Label4_46.configure(text='''Px''')

        self.Label4_47 = tk.Label(self.Frame2)
        self.Label4_47.place(relx=0.892, rely=0.479, height=15, width=25)
        self.Label4_47.configure(activebackground="#f9f9f9")
        self.Label4_47.configure(text='''Px''')

        self.Label4_48 = tk.Label(self.Frame2)
        self.Label4_48.place(relx=0.892, rely=0.513, height=15, width=25)
        self.Label4_48.configure(activebackground="#f9f9f9")
        self.Label4_48.configure(text='''Mb''')

        self.Label4_49 = tk.Label(self.Frame2)
        self.Label4_49.place(relx=0.892, rely=0.547, height=15, width=25)
        self.Label4_49.configure(activebackground="#f9f9f9")
        self.Label4_49.configure(text='''inch''')

        self.Label4_50 = tk.Label(self.Frame2)
        self.Label4_50.place(relx=0.892, rely=0.581, height=15, width=25)
        self.Label4_50.configure(activebackground="#f9f9f9")
        self.Label4_50.configure(text='''inch''')

        self.Label4_50 = tk.Label(self.Frame2)
        self.Label4_50.place(relx=0.892, rely=0.615, height=15, width=25)
        self.Label4_50.configure(activebackground="#f9f9f9")
        self.Label4_50.configure(text='''Hr''')

        self.calculate = tk.Button(self.Frame2,command = self.cal)
        self.calculate.place(relx=0.024, rely=0.667, height=35, width=400)
        self.calculate.configure(font=font11)
        self.calculate.configure(text='''Calculate''')
        
        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.62, rely=0.017, relheight=0.977
                , relwidth=0.380)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#6cd873")

        self.Label5 = tk.Label(self.Frame3)
        self.Label5.place(relx=0.170, rely=0.14, height=500, width=290)
        self.Label5.configure(activebackground="#f9f9f9")
        
        self.M15 = tk.Button(self.Frame3,command=self.openanother)
        self.M15.place(relx=0.170, rely=0.034, height=35, width=290)
        self.M15.configure(activebackground="#f9f9f9")
        self.M15.configure(text='''Show Saved Data''')
        self.knnclassifier()    
    def openanother(self):
        os.system('python newwindow.py')

    def create_connection(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Shyam123@@"
        )

    def insert_data_db(self):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO mobile.mob VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (str(self.na_mobile),
        str(self.ff1),str(self.ff2),str(self.ff3),
        str(self.ff4),str(self.ff5),str(self.ff6),
        str(self.ff7),str(self.ff8),str(self.ff9),
        str(self.ff10),str(self.ff11),str(self.ff12),
        str(self.ff13),str(self.predicted_price[0]))
        mycursor.execute(sql, val) 
        self.mydb.commit()

        print(mycursor.rowcount, "record inserted.")

    def deletefromoutput(self):
        self.output.delete(1.0, 'end')
    
    def mulReg(self):
        pass

    def feature_selection(self):        
        data = pd.read_csv("data.csv")

        numerics = ['int16','int32','int64','float16','float32','float64']
        numerical_vars = list(data.select_dtypes(include=numerics).columns)
        data = data[numerical_vars]
        X_train, X_test, y_train, y_test = train_test_split(
            data.drop(labels=['price_range'], axis=1),
            data['price_range'],
            test_size=0.3,
            random_state=0)

        regressor = LinearRegression()  
        regressor.fit(self.x, self.y)
        pre = regressor.predict(self.test_data)
        self.predicted_price = pre
        self.output.insert(tk.END, "\nBy multiple linear regression\n Predicted price of mobile : "+str(pre)+" Rs.\n")
        regressor.fit(X_train,y_train)
        reg = LassoCV()
        reg.fit(self.x, self.y)
        pre = reg.predict(self.test_data)
        self.output.insert(tk.END, "\nBy embedded method,\n Predicted price of mobile : "+str(pre)+" Rs.\n")
        self.output.insert(tk.END, "\n\nAccuracy of Training Data : "+str(regressor.score(X_train,y_train)))
        self.output.insert(tk.END, "\n\nAccuracy of Testing Data : "+str(regressor.score(X_test,y_test)))

    def knnclassifier(self):
        self.y = self.data['price_range']
        self.x = self.data.drop('price_range', axis = 1)
        self.x_train, self.x_valid, self.y_train, self.y_valid = train_test_split(self.x, self.y, test_size = 0.2, random_state = 101, stratify = self.y)
        self.test_data=self.test_data.drop('id',axis=1)

    def cal(self):
        self.deletefromoutput()
        self.na_mobile = str(self.name.get())
        self.output.insert(tk.END, "\nMobile Name : "+str(self.na_mobile)+"\n")
        self.ff1 = int(self.f1.get())
        self.ff2 = float(self.f2.get())
        self.ff3 = int(self.f3.get())
        self.ff4 = int(self.f4.get())
        self.ff5 = float(self.f5.get())
        self.ff6 = int(self.f6.get())
        self.ff7 = int(self.f7.get())
        self.ff8 = int(self.f8.get())
        self.ff9 = int(self.f9.get())
        self.ff10 = int(self.f10.get())
        self.ff11 = int(self.f11.get())
        self.ff12 = int(self.f12.get())
        self.ff13 = int(self.f13.get())
        
        self.test_data["battery_power"]=self.ff1
        self.test_data["clock_speed"]=self.ff2
        self.test_data["fc"]=self.ff3
        self.test_data["int_memory"]=self.ff4
        self.test_data["m_dep"]=self.ff5
        self.test_data["n_cores"]=self.ff6
        self.test_data["pc"]=self.ff7
        self.test_data["px_height"]=self.ff8
        self.test_data["px_width"]=self.ff9
        self.test_data["ram"]=self.ff10
        self.test_data["sc_h"]=self.ff11
        self.test_data["sc_w"]=self.ff12
        self.test_data["talk_time"]=self.ff13
        self.feature_selection()
        self.mulReg()
        self.create_connection()
        self.insert_data_db()

    def deleteextra(self):
        self.name.delete(0,'end')
        self.f1.delete(0,'end')
        self.f2.delete(0,'end')
        self.f3.delete(0,'end')
        self.f4.delete(0,'end')
        self.f5.delete(0,'end')
        self.f6.delete(0,'end')
        self.f7.delete(0,'end')
        self.f8.delete(0,'end')
        self.f9.delete(0,'end')
        self.f10.delete(0,'end')
        self.f11.delete(0,'end')
        self.f12.delete(0,'end')
        self.f13.delete(0,'end')

    def c1(self):
        self.deleteextra()
        self.name.insert(0,"Redmi note 7")
        self.f1.insert(0,"842")
        self.f2.insert(0,"2.2")
        self.f3.insert(0,"1")
        self.f4.insert(0,"7")
        self.f5.insert(0,"0.6")
        self.f6.insert(0,"2")
        self.f7.insert(0,"2")
        self.f8.insert(0,"20")
        self.f9.insert(0,"756")
        self.f10.insert(0,"2549")
        self.f11.insert(0,"9")
        self.f12.insert(0,"7")
        self.f13.insert(0,"19")
        render = ImageTk.PhotoImage(file="mobile_img/2.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

    def c2(self):
        self.deleteextra()
        self.name.insert(0,"Realme XT")
        self.f1.insert(0,"1021")
        self.f2.insert(0,"0.5")
        self.f3.insert(0,"0")
        self.f4.insert(0,"53")
        self.f5.insert(0,"0.7")
        self.f6.insert(0,"3")
        self.f7.insert(0,"6")
        self.f8.insert(0,"905")
        self.f9.insert(0,"1988")
        self.f10.insert(0,"2631")
        self.f11.insert(0,"17")
        self.f12.insert(0,"3")
        self.f13.insert(0,"7")
        render = ImageTk.PhotoImage(file="mobile_img/3.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

    def c3(self):
        self.deleteextra()
        self.name.insert(0,"Samsung Galaxy X")
        self.f1.insert(0,"563")
        self.f2.insert(0,"0.5")
        self.f3.insert(0,"2")
        self.f4.insert(0,"41")
        self.f5.insert(0,"0.9")
        self.f6.insert(0,"5")
        self.f7.insert(0,"6")
        self.f8.insert(0,"1263")
        self.f9.insert(0,"1716")
        self.f10.insert(0,"2603")
        self.f11.insert(0,"11")
        self.f12.insert(0,"2")
        self.f13.insert(0,"9")
        render = ImageTk.PhotoImage(file="mobile_img/4.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

    def c4(self):
        self.deleteextra()
        self.name.insert(0,"Samsung A1")
        self.f1.insert(0,"615")
        self.f2.insert(0,"2.5")
        self.f3.insert(0,"0")
        self.f4.insert(0,"10")
        self.f5.insert(0,"0.8")
        self.f6.insert(0,"6")
        self.f7.insert(0,"9")
        self.f8.insert(0,"1216")
        self.f9.insert(0,"1786")
        self.f10.insert(0,"2769")
        self.f11.insert(0,"16")
        self.f12.insert(0,"8")
        self.f13.insert(0,"11")
        render = ImageTk.PhotoImage(file="mobile_img/5.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

    def c5(self):
        self.deleteextra()
        self.name.insert(0,"Lenovo K1")
        self.f1.insert(0,"1821")
        self.f2.insert(0,"1.2")
        self.f3.insert(0,"13")
        self.f4.insert(0,"44")
        self.f5.insert(0,"0.6")
        self.f6.insert(0,"2")
        self.f7.insert(0,"14")
        self.f8.insert(0,"1208")
        self.f9.insert(0,"1212")
        self.f10.insert(0,"1411")
        self.f11.insert(0,"8")
        self.f12.insert(0,"2")
        self.f13.insert(0,"15")
        render = ImageTk.PhotoImage(file="mobile_img/6.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

    def c6(self):
        self.deleteextra()
        self.name.insert(0,"One plus 6T")
        self.f1.insert(0,"1821")
        self.f2.insert(0,"1.7")
        self.f3.insert(0,"4")
        self.f4.insert(0,"10")
        self.f5.insert(0,"0.8")
        self.f6.insert(0,"8")
        self.f7.insert(0,"10")
        self.f8.insert(0,"381")
        self.f9.insert(0,"1018")
        self.f10.insert(0,"3220")
        self.f11.insert(0,"13")
        self.f12.insert(0,"8")
        self.f13.insert(0,"18")
        render = ImageTk.PhotoImage(file="mobile_img/7.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

    def c7(self):
        self.deleteextra()
        self.name.insert(0,"Coolpad cool 1")
        self.f1.insert(0,"1954")
        self.f2.insert(0,"0.5")
        self.f3.insert(0,"0")
        self.f4.insert(0,"24")
        self.f5.insert(0,"0.8")
        self.f6.insert(0,"4")
        self.f7.insert(0,"0")
        self.f8.insert(0,"512")
        self.f9.insert(0,"1149")
        self.f10.insert(0,"700")
        self.f11.insert(0,"16")
        self.f12.insert(0,"3")
        self.f13.insert(0,"5")
        render = ImageTk.PhotoImage(file="mobile_img/8.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

    def c8(self):
        self.deleteextra()
        self.name.insert(0,"Vivo x pro")
        self.f1.insert(0,"1445")
        self.f2.insert(0,"0.5")
        self.f3.insert(0,"0")
        self.f4.insert(0,"53")
        self.f5.insert(0,"0.7")
        self.f6.insert(0,"7")
        self.f7.insert(0,"14")
        self.f8.insert(0,"386")
        self.f9.insert(0,"836")
        self.f10.insert(0,"1099")
        self.f11.insert(0,"17")
        self.f12.insert(0,"1")
        self.f13.insert(0,"20")
        render = ImageTk.PhotoImage(file="mobile_img/9.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

    def c9(self):
        self.deleteextra()
        self.name.insert(0,"Samsung Galaxt A2")
        self.f1.insert(0,"509")
        self.f2.insert(0,"0.6")
        self.f3.insert(0,"2")
        self.f4.insert(0,"9")
        self.f5.insert(0,"0.1")
        self.f6.insert(0,"5")
        self.f7.insert(0,"15")
        self.f8.insert(0,"1137")
        self.f9.insert(0,"1224")
        self.f10.insert(0,"513")
        self.f11.insert(0,"19")
        self.f12.insert(0,"10")
        self.f13.insert(0,"12")
        render = ImageTk.PhotoImage(file="mobile_img/10.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

    def c10(self):
        self.deleteextra()
        self.name.insert(0,"Nokia Asha")
        self.f1.insert(0,"509")
        self.f2.insert(0,"0.6")
        self.f3.insert(0,"2")
        self.f4.insert(0,"9")
        self.f5.insert(0,"0.1")
        self.f6.insert(0,"5")
        self.f7.insert(0,"15")
        self.f8.insert(0,"1137")
        self.f9.insert(0,"1227")
        self.f10.insert(0,"513")
        self.f11.insert(0,"19")
        self.f12.insert(0,"10")
        self.f13.insert(0,"12")
        render = ImageTk.PhotoImage(file="mobile_img/11.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

    def c11(self):
        self.deleteextra()
        self.name.insert(0,"Micomax zono")
        self.f1.insert(0,"769")
        self.f2.insert(0,"2.9")
        self.f3.insert(0,"0")
        self.f4.insert(0,"9")
        self.f5.insert(0,"0.1")
        self.f6.insert(0,"5")
        self.f7.insert(0,"1")
        self.f8.insert(0,"248")
        self.f9.insert(0,"874")
        self.f10.insert(0,"3946")
        self.f11.insert(0,"5")
        self.f12.insert(0,"2")
        self.f13.insert(0,"7")
        render = ImageTk.PhotoImage(file="mobile_img/12.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

    def c12(self):
        self.deleteextra()
        self.name.insert(0,"Huawei d1")
        self.f1.insert(0,"1520")
        self.f2.insert(0,"2.2")
        self.f3.insert(0,"5")
        self.f4.insert(0,"33")
        self.f5.insert(0,"0.5")
        self.f6.insert(0,"8")
        self.f7.insert(0,"18")
        self.f8.insert(0,"151")
        self.f9.insert(0,"1005")
        self.f10.insert(0,"3826")
        self.f11.insert(0,"14")
        self.f12.insert(0,"9")
        self.f13.insert(0,"13")
        render = ImageTk.PhotoImage(file="mobile_img/13.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

    def c13(self):
        self.deleteextra()
        self.name.insert(0,"Honor 6x")
        self.f1.insert(0,"1815")
        self.f2.insert(0,"2.8")
        self.f3.insert(0,"2")
        self.f4.insert(0,"33")
        self.f5.insert(0,"0.6")
        self.f6.insert(0,"4")
        self.f7.insert(0,"17")
        self.f8.insert(0,"607")
        self.f9.insert(0,"748")
        self.f10.insert(0,"1482")
        self.f11.insert(0,"18")
        self.f12.insert(0,"0")
        self.f13.insert(0,"2")
        render = ImageTk.PhotoImage(file="mobile_img/1.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

    def c14(self):
        self.deleteextra()
        self.name.insert(0,"One plus 7T")
        self.f1.insert(0,"803")
        self.f2.insert(0,"2.1")
        self.f3.insert(0,"7")
        self.f4.insert(0,"17")
        self.f5.insert(0,"1")
        self.f6.insert(0,"4")
        self.f7.insert(0,"11")
        self.f8.insert(0,"344")
        self.f9.insert(0,"1440")
        self.f10.insert(0,"2680")
        self.f11.insert(0,"7")
        self.f12.insert(0,"1")
        self.f13.insert(0,"4")
        render = ImageTk.PhotoImage(file="mobile_img/14.jpeg")
        self.Label5.configure(image = render)
        self.Label5.image = render
        self.Label5.place(x=0, y=0)

if __name__ == '__main__':
    vp_start_gui()





