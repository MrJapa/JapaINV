import tkinter as tk
from tkinter import messagebox
import tkinter.font as font 
import os
import time
import pyodbc
import webbrowser
import winshell
import win32com.client
import keyboard
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from tkinter import Button, Tk, HORIZONTAL
from tkinter.ttk import Progressbar
from datetime import datetime, date
from string import Template
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from tooltip import CreateToolTip
from tkPDFViewer import tkPDFViewer as pdf
from tkcalendar import Calendar,DateEntry
from passwords import serverkey,databasekey,uidkey,passwordkey

cdir = os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
##############################
bg_inv = "images/background.png"
bgpng = "images/bgpng.png"
icon = "images/icon.ico"
url2 = "https://github.com/MrJapa"
new = 1
#BUNGEE LAYER FONT
##############################
server = serverkey
database = databasekey
UID = uidkey
passw = passwordkey
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+UID+';PWD='+ passw)
cursor = cnxn.cursor()

##############################
main_login = Tk()
login = tk.StringVar()
password = tk.StringVar()
###!Inventory*###
###*Computers*###
user = StringVar()
model = StringVar()
manu = StringVar()
name = StringVar()
###*Phones*###
userp = StringVar()
phonep = StringVar()
subscriptionp = StringVar()
phonenumberp = StringVar()
###*Hardware*###
userh = StringVar()
typeh = StringVar()
modelh = StringVar()
manuh = StringVar()
desch = StringVar()
###*Network*###
typen = StringVar()
modeln = StringVar()
manun = StringVar()
ipadr = StringVar()
descn = StringVar()
##############################
exitinv_startcom = lambda: [exit_inv(), computers_screen()]
exitinv_startpho = lambda: [exit_inv(), phones_screen()]
exitinv_starthar = lambda: [exit_inv(), hardware_screen()]
exitinv_startnet = lambda: [exit_inv(), network_screen()]
###!!####

###!!###
exitcom_startmain = lambda: [exit_com(), inventory_screen()]
exitpho_startmain = lambda: [exit_pho(), inventory_screen()]
exithwd_startmain = lambda: [exit_hdw(), inventory_screen()]
exitnet_startmain = lambda: [exit_net(), inventory_screen()]
##############################
def login_screen():
    global signin
    signin = tk.Toplevel()
    signin.geometry("375x175")
    signin.title("JapaINV")
    signin.iconbitmap(icon)
    signin.resizable(False,False)
    #signin.overrideredirect(1) #removes border

    bg_login = PhotoImage(file="images/create.png")
    label1 = Label(signin, image=bg_login)
    label1.place(x=0,y=0)

    email_label = Label(signin, text="Username:")
    email_label.pack(expand=False)

    email_entry = Entry(signin, textvariable=login)
    email_entry.pack(expand=False)
    email_entry.focus()

    # password
    password_label = Label(signin, text="Password:")
    password_label.pack(expand=False)

    password_entry = Entry(signin, textvariable=password, show="*")
    password_entry.pack(expand=False)

    login_button = Button(signin, text="Sign In", command=sign_in)
    login_button.pack(expand=False, pady=10)

    signin.mainloop()
##########!Inventory!##########!
def inventory_screen():
    global inventory
    inventory = Tk()
    inventory.geometry("1366x768")
    inventory.title("JapaINV")
    inventory.iconbitmap(icon)
    inventory.resizable(False,False)
    inventorybg = PhotoImage(file = bg_inv)
    
    canvas_inv = Canvas(inventory,width=1366, height=768)
    canvas_inv.pack(fill = "both", expand=True)
    canvas_inv.create_image(0,0, image = inventorybg, anchor = "nw")

    computers = PhotoImage(file = "images/computers.png")
    computer_button = Button(text="", image=computers,highlightthickness=0,bd=0, command=exitinv_startcom)
    computer_canvas = canvas_inv.create_window(400,58,anchor="center",window=computer_button)

    phones = PhotoImage(file= "images/phones.png")
    phones_button = Button(text="", image = phones,highlightthickness=0,bd=0,command=exitinv_startpho)
    phones_canvas = canvas_inv.create_window(600,58,anchor="center",window=phones_button)

    hardware = PhotoImage(file= "images/hardware.png")
    hardware_button = Button(text="", image = hardware,highlightthickness=0,bd=0,command=exitinv_starthar)
    hardware_canvas = canvas_inv.create_window(800,58,anchor="center",window=hardware_button)

    network = PhotoImage(file= "images/network.png")
    network_button = Button(text="", image = network,highlightthickness=0,bd=0,command=exitinv_startnet)
    network_canvas = canvas_inv.create_window(1000,58,anchor="center",window=network_button)

    user_button = Button(inventory,text=login.get(),fg="white",bg="#00b5ff", font="Calibri 20 bold",highlightthickness=0,bd=0,command=sign_out)
    user_canvas = canvas_inv.create_window(1300,35,anchor="center",window=user_button)

    charts = PhotoImage(file= "images/charts.png")
    charts_button = Button(text="",image=charts,highlightthickness=0,bd=0,command=None)
    charts_canvas = canvas_inv.create_window(350,500,anchor="center",window=charts_button)

    databases = PhotoImage(file= "images/database.png")
    databases_button = Button(text="",image=databases,highlightthickness=0,bd=0,command=None)
    databases_canvas = canvas_inv.create_window(950,500,anchor="center",window=databases_button)

    inventory.mainloop()
##########*Computer*##########
def computers_screen():
    global computersscreen
    computersscreen = Tk()
    computersscreen.geometry("1366x768")
    computersscreen.title("JapaINV")
    computersscreen.iconbitmap(icon)
    computersscreen.resizable(False,False)
    computersscreenbg = PhotoImage(file = bg_inv)
    
    global canvas_cs
    canvas_cs = Canvas(computersscreen,width=1366, height=768,border=0)
    canvas_cs.pack(fill = "both", expand=True)
    canvas_cs.create_image(0,0, image = computersscreenbg, anchor = "nw")

    computers = PhotoImage(file = "images/computers.png")
    computer_button = Button(text="", image=computers,highlightthickness=0,bd=0, command=None)
    computer_canvas = canvas_cs.create_window(400,58,anchor="center",window=computer_button)

    selected_window = PhotoImage(file= "images/computers.png")
    selected_window_button = Button(text="", image=selected_window,highlightthickness=0,bd=0,command=None)
    selected_window_canvas = canvas_cs.create_window(163,235,anchor="center",window=selected_window_button)

    user_button = Button(computersscreen,text=login.get(),fg="white",bg="#00b5ff", font="Calibri 20 bold",highlightthickness=0,bd=0,command=sign_out)
    user_canvas = canvas_cs.create_window(1300,35,anchor="center",window=user_button)

    back = PhotoImage(file= "images/back.png")
    back_button = Button(text="",image=back,highlightthickness=0,bd=0,command=exitcom_startmain)
    back_canvas = canvas_cs.create_window(1305,92,anchor="center",window=back_button)

    #TREEVIEW FRAME
    computerframe = LabelFrame(canvas_cs, text="")
    computerframe.place(x=75, y=245,height=500, width=545)
    global trv
    trv = ttk.Treeview(computerframe, columns=(1,2,3,4), show="headings", height="20")
    trv.pack()
    trv.heading(1, text="User")
    trv.heading(2, text="Device Name")
    trv.heading(3, text="Model")
    trv.heading(4, text="Manufacturer")

    trv.column(1, minwidth=100, width=100)
    trv.column(2, minwidth=100, width=100)
    trv.column(3, minwidth=100, width=100)
    trv.column(4, minwidth=100, width=100)
    trv.bind('<Double 1>', getrow)

    computerquery = "SELECT * FROM Computers"
    cursor.execute(computerquery)
    rows = cursor.fetchall()
    rows = [tuple(item.strip() for item in row) for row in rows]
    update(rows)
    
    cursor.execute("SELECT COUNT (*) FROM Computers")
    rowcount = cursor.fetchone()[0]

    #SEARCH FRAME
    searchimage = PhotoImage(file = "images/search.png")
    searchimage_button = Button(text="", image=searchimage,highlightthickness=0,bd=0, command=None)
    searchimage_canvas = canvas_cs.create_window(719,235,anchor="center",window=searchimage_button)
    global searchframe
    searchframe = LabelFrame(canvas_cs, text="")
    searchframe.place(x=650, y=245, height=150, width=350)
    lbl = Label(searchframe, text="")
    lbl.pack(side=tk.TOP, padx=10)
    global labelcount2
    labelcount2 = Label(searchframe, text="Total records: %s" % rowcount)
    labelcount2.pack(side=tk.TOP, padx=6)
    labelcount = Label(canvas_cs, text="Total records: %s" % rowcount)
    labelcount.place(x=260,y=230)
    global ent
    ent = Entry(searchframe)
    ent.pack(side=tk.LEFT, padx=6)
    ent.focus()
    searchbtnimage = PhotoImage(file="images/searchbtn.png")
    btn = Button(searchframe, text="Search",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command=search)
    btn.pack(side=tk.LEFT, padx=6)
    clearbtnimage = PhotoImage(file="images/clearbtn.png")
    btn2 = Button(searchframe, text="Clear",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command=allquery)
    btn2.pack(side=tk.LEFT,padx=6)
    refreshbtnimage = PhotoImage(file="images/refreshbtn.png")
    btn3 = Button(searchframe, text="Refresh",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command=allquery)
    btn3.pack(side=tk.LEFT, padx=6)

    queryimage = PhotoImage(file="images/query.png")
    queryimage_button = Button(text="",image=queryimage,highlightthickness=0,bd=0,command=None)
    queryimage_canvas = canvas_cs.create_window(719,435,anchor="center",window=queryimage_button)
    #USER DATA SECTION
    userdataframe = LabelFrame(canvas_cs, text="")
    userdataframe.place(x=650, y=445, height=250, width=350)
    filler1 = Label(userdataframe, text="")
    filler1.grid(row=0,column=0,padx=5,pady=3)
    filler2 = Label(userdataframe, text="Create a new entry")
    filler2.grid(row=1,column=1,padx=5,pady=3)
    global userent
    userlbl = Label(userdataframe, text="User")
    userlbl.grid(row=2,column=0,padx=5,pady=3)
    userent = Entry(userdataframe, textvariable=user)
    userent.grid(row=2,column=1,padx=5,pady=3)
    global nameent
    namelbl = Label(userdataframe,text="PC Name")
    namelbl.grid(row=3,column=0,padx=5,pady=3)
    nameent = Entry(userdataframe,textvariable=name)
    nameent.grid(row=3,column=1,padx=5,pady=3)
    global modelent
    modellbl = Label(userdataframe, text="Model")
    modellbl.grid(row=4,column=0,padx=5,pady=3)
    modelent = Entry(userdataframe, textvariable=model)
    modelent.grid(row=4,column=1,padx=5,pady=3)
    global manuent
    manulbl = Label(userdataframe, text="Manufacturer")
    manulbl.grid(row=5,column=0,padx=5,pady=3)
    manuent = Entry(userdataframe,textvariable=manu)
    manuent.grid(row=5,column=1,padx=5,pady=3)

    add_btn = Button(userdataframe, text="Add New",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command = add_new)
    add_btn_ttp = CreateToolTip(add_btn, "Add a new entry")
    delete_btn = Button(userdataframe, text="Delete",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command = delete_entry)
    delete_btn_ttp = CreateToolTip(delete_btn, "Delete the selected entry (Double click entry)")
    filler3 = Label(userdataframe, text="")
    filler3.grid(row=6,column=0,padx=5,pady=3)

    add_btn.grid(row=7,column=0,padx=5,pady=3)
    delete_btn.grid(row=7,column=1,padx=5,pady=3)


    computersscreen.mainloop()
#get rows computer
def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    user.set(item['values'][0])
    name.set(item['values'][1])
    model.set(item['values'][2])
    manu.set(item['values'][3])
#add new computer
def add_new():
    newmodel = model.get()
    newuser = user.get()
    newmanu = manu.get()
    cursor.execute("INSERT INTO Computers ([User],DeviceName,Model,Manufacturer) VALUES (?,?,?,?)",userent.get(),nameent.get(),modelent.get(),manuent.get())
    cursor.commit()
    allquery()
#Delete computer
def delete_entry():
    user_id = user.get()
    if messagebox.askyesno("Confirm deletion", "Are you sure you want to delete this item?"):
        cursor.execute("DELETE FROM Computers WHERE [User] = (?)",user.get())
        cursor.commit()
        allquery()
    else:
        return True
#Allquery Computer
def allquery():
    computerquery = "SELECT * FROM Computers"
    cursor.execute(computerquery)
    rows = cursor.fetchall()
    rows = [tuple(item.strip() for item in row) for row in rows]
    update(rows)
    cursor.execute("SELECT COUNT (*) FROM Computers")
    rowcount = cursor.fetchone()[0]
    labelcount2.config(text="Total records: %s" % rowcount)
    labelcount2.pack(side=tk.TOP,padx=6)
#Search Computer
def search():
    global search
    tup1 = "SELECT * FROM Computers WHERE [User] LIKE '%"
    tup2 = ent.get()
    tup3 = "%' OR Model LIKE '%"
    tup4 = ent.get()
    tup5 = "%' OR Manufacturer LIKE '%"
    tup6 = ent.get()
    tup7 = "%'"
    tuples = tup1 + tup2 + tup3 + tup4 + tup5 + tup6 + tup7
    cursor.execute(tuples)
    rows = cursor.fetchall()
    rows = [tuple(item.strip() for item in row) for row in rows]
    update(rows)
    if len(rows) == 0:
        cursor.execute("SELECT COUNT (*) FROM Computers")
        rowcount = cursor.fetchone()[0]
        labelcount2.config(text="Total records: %s" % rowcount)
        labelcount2.pack(side=tk.TOP,padx=6)
    else:
        tup1 = "SELECT COUNT (*) FROM Computers WHERE [User] LIKE '%"
        tup2 = ent.get()
        tup3 = "%' OR Model LIKE '%"
        tup4 = ent.get()
        tup5 = "%' OR Manufacturer LIKE '%"
        tup6 = ent.get()
        tup7 = "%'"
        tuples2 = tup1 + tup2 + tup3 + tup4 + tup5 + tup6 + tup7
        cursor.execute(tuples2)
        rowcount = cursor.fetchone()[0]
        labelcount2.config(text="Total records: %s" % rowcount)
        labelcount2.pack(side=tk.TOP,padx=6)
#update computer rows
def update(rows):
    global update
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)
##########*Phones*##########
def phones_screen():
    global phonesscreen
    phonesscreen = Tk()
    phonesscreen.geometry("1366x768")
    phonesscreen.title("JapaINV")
    phonesscreen.iconbitmap(icon)
    phonesscreen.resizable(False,False)
    phonesscreenbg = PhotoImage(file = bg_inv)
    
    global canvas_ps
    canvas_ps = Canvas(phonesscreen,width=1366, height=768,border=0)
    canvas_ps.pack(fill = "both", expand=True)
    canvas_ps.create_image(0,0, image = phonesscreenbg, anchor = "nw")

    phones = PhotoImage(file = "images/phones.png")
    phones_button = Button(text="", image=phones,highlightthickness=0,bd=0, command=None)
    phones_canvas = canvas_ps.create_window(600,58,anchor="center",window=phones_button)

    selected_window = PhotoImage(file= "images/phones.png")
    selected_window_button = Button(text="", image=selected_window,highlightthickness=0,bd=0,command=None)
    selected_window_canvas = canvas_ps.create_window(163,235,anchor="center",window=selected_window_button)

    user_button = Button(phonesscreen,text=login.get(),fg="white",bg="#00b5ff", font="Calibri 20 bold",highlightthickness=0,bd=0,command=sign_out)
    user_canvas = canvas_ps.create_window(1300,35,anchor="center",window=user_button)

    back = PhotoImage(file= "images/back.png")
    back_button = Button(text="",image=back,highlightthickness=0,bd=0,command=exitpho_startmain)
    back_canvas = canvas_ps.create_window(1305,92,anchor="center",window=back_button)

    #TREEVIEW FRAME
    phonesframe = LabelFrame(canvas_ps, text="")
    phonesframe.place(x=75, y=245,height=500, width=545)
    global trvp
    trvp = ttk.Treeview(phonesframe, columns=(1,2,3,4), show="headings", height="20")
    trvp.pack()
    trvp.heading(1, text="User")
    trvp.heading(2, text="Phone")
    trvp.heading(3, text="Subscription")
    trvp.heading(4, text="Phone Number")

    trvp.column(1, minwidth=100, width=120)
    trvp.column(2, minwidth=100, width=120)
    trvp.column(3, minwidth=100, width=120)
    trvp.column(4, minwidth=100, width=120)
    trvp.bind('<Double 1>', getrow_phone)

    phonequery = "SELECT * FROM Phones"
    cursor.execute(phonequery)
    rows = cursor.fetchall()
    rows = [tuple(item.strip() for item in row) for row in rows]
    update_phones(rows)
    
    cursor.execute("SELECT COUNT (*) FROM Phones")
    rowcount = cursor.fetchone()[0]

    #SEARCH FRAME
    searchimagep = PhotoImage(file = "images/search.png")
    searchimagep_button = Button(text="", image=searchimagep,highlightthickness=0,bd=0, command=None)
    searchimagep_canvas = canvas_ps.create_window(719,235,anchor="center",window=searchimagep_button)
    global searchframep
    searchframep = LabelFrame(canvas_ps, text="")
    searchframep.place(x=650, y=245, height=150, width=350)
    lblp = Label(searchframep, text="")
    lblp.pack(side=tk.TOP, padx=10)
    global labelcount2p
    labelcount2p = Label(searchframep, text="Total records: %s" % rowcount)
    labelcount2p.pack(side=tk.TOP,padx=6)

    labelcountp = Label(canvas_ps, text="Total records: %s" % rowcount)
    labelcountp.place(x=260,y=230)
    global entp
    entp = Entry(searchframep)
    entp.pack(side=tk.LEFT, padx=6)
    entp.focus()
    searchbtnimagep = PhotoImage(file="images/searchbtn.png")
    btnp = Button(searchframep, text="Search",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command=search_phone)
    btnp.pack(side=tk.LEFT, padx=6)
    clearbtnimagep = PhotoImage(file="images/clearbtn.png")
    btn2p = Button(searchframep, text="Clear",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command=allquery_phone)
    btn2p.pack(side=tk.LEFT,padx=6)
    refreshbtnimagep = PhotoImage(file="images/refreshbtn.png")
    btn3p = Button(searchframep, text="Refresh",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command=allquery_phone)
    btn3p.pack(side=tk.LEFT, padx=6)

    queryimagep = PhotoImage(file="images/query.png")
    queryimage_buttonp = Button(text="",image=queryimagep,highlightthickness=0,bd=0,command=None)
    queryimage_canvasp = canvas_ps.create_window(719,435,anchor="center",window=queryimage_buttonp)
    #USER DATA SECTION
    userdataframep = LabelFrame(canvas_ps, text="")
    userdataframep.place(x=650, y=445, height=250, width=350)
    filler1p = Label(userdataframep, text="")
    filler1p.grid(row=0,column=0,padx=5,pady=3)
    filler2p = Label(userdataframep, text="Create a new entry")
    filler2p.grid(row=1,column=1,padx=5,pady=3)
    global userentp
    userlblp = Label(userdataframep, text="User")
    userlblp.grid(row=2,column=0,padx=5,pady=3)
    userentp = Entry(userdataframep, textvariable=userp)
    userentp.grid(row=2,column=1,padx=5,pady=3)
    global nameentp
    namelblp = Label(userdataframep,text="Phone")
    namelblp.grid(row=3,column=0,padx=5,pady=3)
    nameentp = Entry(userdataframep,textvariable=phonep)
    nameentp.grid(row=3,column=1,padx=5,pady=3)
    global modelentp
    modellblp = Label(userdataframep, text="Subscription")
    modellblp.grid(row=4,column=0,padx=5,pady=3)
    modelentp = Entry(userdataframep, textvariable=subscriptionp)
    modelentp.grid(row=4,column=1,padx=5,pady=3)
    global manuentp
    manulblp = Label(userdataframep, text="Phone Number")
    manulblp.grid(row=5,column=0,padx=5,pady=3)
    manuentp = Entry(userdataframep,textvariable=phonenumberp)
    manuentp.grid(row=5,column=1,padx=5,pady=3)

    add_btnp = Button(userdataframep, text="Add New",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command = add_new_phone)
    add_btn_ttpp = CreateToolTip(add_btnp, "Add a new entry")
    delete_btnp = Button(userdataframep, text="Delete",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command = delete_entry_phone)
    delete_btn_ttpp = CreateToolTip(delete_btnp, "Delete the selected entry (Double click entry)")
    filler3p = Label(userdataframep, text="")
    filler3p.grid(row=6,column=0,padx=5,pady=3)

    add_btnp.grid(row=7,column=0,padx=5,pady=3)
    delete_btnp.grid(row=7,column=1,padx=5,pady=3)


    phonesscreen.mainloop()
#get rows phone
def getrow_phone(events):
    rowid = trvp.identify_row(events.y)
    item = trvp.item(trvp.focus())
    userp.set(item['values'][0])
    phonep.set(item['values'][1])
    subscriptionp.set(item['values'][2])
    phonenumberp.set(item['values'][3])
#add new phones
def add_new_phone():
    cursor.execute("INSERT INTO Phones ([User],Phone,Subscription,PhoneNumber) VALUES (?,?,?,?)",userentp.get(),nameentp.get(),modelentp.get(),manuentp.get())
    cursor.commit()
    allquery_phone()
#Delete phones
def delete_entry_phone():
    user_id = userp.get()
    if messagebox.askyesno("Confirm deletion", "Are you sure you want to delete this item?"):
        cursor.execute("DELETE FROM Phones WHERE [User] = (?)",userp.get())
        cursor.commit()
        allquery_phone()
    else:
        return True
#Allquery phones
def allquery_phone():
    computerquery = "SELECT * FROM Phones"
    cursor.execute(computerquery)
    rows = cursor.fetchall()
    rows = [tuple(item.strip() for item in row) for row in rows]
    update_phones(rows)
    cursor.execute("SELECT COUNT (*) FROM Phones")
    rowcount = cursor.fetchone()[0]
    labelcount2p.config(text="Total records: %s" % rowcount)
    labelcount2p.pack(side=tk.TOP,padx=6)
#Search phones
def search_phone():
    global search
    tup1 = "SELECT * FROM Phones WHERE [User] LIKE '%"
    tup2 = entp.get()
    tup3 = "%' OR Phone LIKE '%"
    tup4 = entp.get()
    tup5 = "%' OR PhoneNumber LIKE '%"
    tup6 = entp.get()
    tup7 = "%'"
    tuples = tup1 + tup2 + tup3 + tup4 + tup5 + tup6 + tup7
    cursor.execute(tuples)
    rows = cursor.fetchall()
    rows = [tuple(item.strip() for item in row) for row in rows]
    update_phones(rows)
    if len(rows) == 0:
        cursor.execute("SELECT COUNT (*) FROM Phones")
        rowcount = cursor.fetchone()[0]
        labelcount2p.config(text="Total records: %s" % rowcount)
        labelcount2p.pack(side=tk.TOP,padx=6)
    else:#COPY THIS TO OTHER SEARCHES
        tup_1 = "SELECT COUNT (*) FROM Phones WHERE [User] LIKE '%"
        tup_2 = entp.get()
        tup_3 = "%' OR Phone LIKE '%"
        tup_4 = entp.get()
        tup_5 = "%' OR PhoneNumber LIKE '%"
        tup_6 = entp.get()
        tup_7 = "%'"
        tuples2 = tup_1 + tup_2 + tup_3 + tup_4 + tup_5 + tup_6 + tup_7
        cursor.execute(tuples2)
        rowcount = cursor.fetchone()[0]
        labelcount2p.config(text="Total records: %s" % rowcount)
        labelcount2p.pack(side=tk.TOP,padx=6)
#update phones rows
def update_phones(rows):
    global update
    trvp.delete(*trvp.get_children())
    for i in rows:
        trvp.insert('','end',values=i)
##########*Hardware*##########
def hardware_screen():
    global hardwarescreen
    hardwarescreen = Tk()
    hardwarescreen.geometry("1366x768")
    hardwarescreen.title("JapaINV")
    hardwarescreen.iconbitmap(icon)
    hardwarescreen.resizable(False,False)
    hardwarescreenbg = PhotoImage(file = bg_inv)
    
    global canvas_hs
    canvas_hs = Canvas(hardwarescreen,width=1366, height=768)
    canvas_hs.pack(fill = "both", expand=True)
    canvas_hs.create_image(0,0, image = hardwarescreenbg, anchor = "nw")

    hardware = PhotoImage(file = "images/hardware.png")
    hardware_button = Button(text="", image=hardware,highlightthickness=0,bd=0, command=None)
    hardware_canvas = canvas_hs.create_window(800,58,anchor="center",window=hardware_button)

    selected_window = PhotoImage(file= "images/hardware.png")
    selected_window_button = Button(text="", image=selected_window,highlightthickness=0,bd=0,command=None)
    selected_window_canvas = canvas_hs.create_window(163,235,anchor="center",window=selected_window_button)

    user_button = Button(hardwarescreen,text=login.get(),fg="white",bg="#00b5ff", font="Calibri 20 bold",highlightthickness=0,bd=0,command=sign_out)
    user_canvas = canvas_hs.create_window(1300,35,anchor="center",window=user_button)

    back = PhotoImage(file= "images/back.png")
    back_button = Button(text="",image=back,highlightthickness=0,bd=0,command=exithwd_startmain)
    back_canvas = canvas_hs.create_window(1305,92,anchor="center",window=back_button)

    #TREEVIEW FRAME
    hardwareframe = LabelFrame(canvas_hs, text="")
    hardwareframe.place(x=75, y=245,height=500, width=545)
    global trvh
    trvh = ttk.Treeview(hardwareframe, columns=(1,2,3,4,5), show="headings", height="20")
    trvh.pack()
    trvh.heading(1, text="User")
    trvh.heading(2, text="Type")
    trvh.heading(3, text="Model")
    trvh.heading(4, text="Manufacturer")
    trvh.heading(5, text="Description")

    trvh.column(1, minwidth=100, width=100)
    trvh.column(2, minwidth=100, width=100)
    trvh.column(3, minwidth=100, width=100)
    trvh.column(4, minwidth=100, width=100)
    trvh.column(5, minwidth=100, width=100)
    trvh.bind('<Double 1>', getrow_hardware)

    phonequery = "SELECT * FROM Hardware"
    cursor.execute(phonequery)
    rows = cursor.fetchall()
    rows = [tuple(item.strip() for item in row) for row in rows]
    update_hardware(rows)
    
    cursor.execute("SELECT COUNT (*) FROM Hardware")
    rowcount = cursor.fetchone()[0]

    #SEARCH FRAME
    searchimageh = PhotoImage(file = "images/search.png")
    searchimageh_button = Button(text="", image=searchimageh,highlightthickness=0,bd=0, command=None)
    searchimageh_canvas = canvas_hs.create_window(719,235,anchor="center",window=searchimageh_button)
    global searchframeh
    searchframeh = LabelFrame(canvas_hs, text="")
    searchframeh.place(x=650, y=245, height=150, width=350)
    lblh = Label(searchframeh, text="")
    lblh.pack(side=tk.TOP, padx=10)
    global labelcount2h
    labelcount2h = Label(searchframeh, text="Total records: %s" % rowcount)
    labelcount2h.pack(side=tk.TOP, padx=6)

    labelcounth = Label(canvas_hs, text="Total records: %s" % rowcount)
    labelcounth.place(x=260,y=230)
    global enth
    enth = Entry(searchframeh)
    enth.pack(side=tk.LEFT, padx=6)
    enth.focus()
    searchbtnimageh = PhotoImage(file="images/searchbtn.png")
    btnh = Button(searchframeh, text="Search",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command=search_hardware)
    btnh.pack(side=tk.LEFT, padx=6)
    clearbtnimageh = PhotoImage(file="images/clearbtn.png")
    btn2h = Button(searchframeh, text="Clear",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command=allquery_hardware)
    btn2h.pack(side=tk.LEFT,padx=6)
    refreshbtnimageh = PhotoImage(file="images/refreshbtn.png")
    btn3h = Button(searchframeh, text="Refresh",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command=allquery_hardware)
    btn3h.pack(side=tk.LEFT, padx=6)

    queryimageh = PhotoImage(file="images/query.png")
    queryimage_buttonh = Button(text="",image=queryimageh,highlightthickness=0,bd=0,command=None)
    queryimage_canvash = canvas_hs.create_window(719,435,anchor="center",window=queryimage_buttonh)
    #USER DATA SECTION
    userdataframeh = LabelFrame(canvas_hs, text="")
    userdataframeh.place(x=650, y=445, height=300, width=350)
    filler1h = Label(userdataframeh, text="Create a new entry")
    filler1h.grid(row=0,column=0,padx=5,pady=3)
    filler2h = Label(userdataframeh, text="")
    filler2h.grid(row=1,column=1,padx=5,pady=3)
    global userenth
    userlblh = Label(userdataframeh, text="User")
    userlblh.grid(row=2,column=0,padx=5,pady=3)
    userenth = Entry(userdataframeh, textvariable=userh)
    userenth.grid(row=2,column=1,padx=5,pady=3)
    global typeenth
    typelblh = Label(userdataframeh,text="Type")
    typelblh.grid(row=3,column=0,padx=5,pady=3)
    typeenth = Entry(userdataframeh,textvariable=typeh)
    typeenth.grid(row=3,column=1,padx=5,pady=3)
    global modelenth
    modellblh = Label(userdataframeh, text="Model")
    modellblh.grid(row=4,column=0,padx=5,pady=3)
    modelenth = Entry(userdataframeh, textvariable=modelh)
    modelenth.grid(row=4,column=1,padx=5,pady=3)
    global manuenth
    manulblh = Label(userdataframeh, text="Manufacturer")
    manulblh.grid(row=5,column=0,padx=5,pady=3)
    manuenth = Entry(userdataframeh,textvariable=manuh)
    manuenth.grid(row=5,column=1,padx=5,pady=3)
    global descenth
    desclblh = Label(userdataframeh, text="Description")
    desclblh.grid(row=6,column=0,padx=5,pady=3)
    descenth = Entry(userdataframeh,textvariable=desch)
    descenth.grid(row=6,column=1,padx=5,pady=3)

    add_btnh = Button(userdataframeh, text="Add New",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command = add_new_hardware)
    add_btn_ttph = CreateToolTip(add_btnh, "Add a new entry")
    delete_btnh = Button(userdataframeh, text="Delete",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command = delete_entry_hardware)
    delete_btn_ttph = CreateToolTip(delete_btnh, "Delete the selected entry (Double click entry)")
    filler3h = Label(userdataframeh, text="")
    filler3h.grid(row=7,column=0,padx=5,pady=3)

    add_btnh.grid(row=8,column=0,padx=5,pady=3)
    delete_btnh.grid(row=8,column=1,padx=5,pady=3)


    hardwarescreen.mainloop()
#Get rows hardware
def getrow_hardware(events):
    rowid = trvh.identify_row(events.y)
    item = trvh.item(trvp.focus())
    userh.set(item['values'][0])
    typeh.set(item['values'][1])
    modelh.set(item['values'][2])
    manuh.set(item['values'][3])
    desch.set(item['values'][4])
#add new hardware
def add_new_hardware():
    cursor.execute("INSERT INTO hardware ([User],Type,Model,Manufacturer,Description) VALUES (?,?,?,?,?)",userenth.get(),typeenth.get(),modelenth.get(),manuenth.get(),descenth.get())
    cursor.commit()
    allquery_hardware()
#Delete hardware
def delete_entry_hardware():
    user_id = userh.get()
    if messagebox.askyesno("Confirm deletion", "Are you sure you want to delete this item?"):
        cursor.execute("DELETE FROM Hardware WHERE [User] = (?)",userh.get())
        cursor.commit()
        allquery_hardware()
    else:
        return True
#Allquery hardware
def allquery_hardware():
    computerquery = "SELECT * FROM Hardware"
    cursor.execute(computerquery)
    rows = cursor.fetchall()
    rows = [tuple(item.strip() for item in row) for row in rows]
    update_hardware(rows)
    cursor.execute("SELECT COUNT (*) FROM Hardware")
    rowcount = cursor.fetchone()[0]
    labelcount2h.config(text="Total records: %s" % rowcount)
    labelcount2h.pack(side=tk.TOP,padx=6)
#Search hardware
def search_hardware():
    global search
    tup1 = "SELECT * FROM Hardware WHERE [User] LIKE '%"
    tup2 = enth.get()
    tup3 = "%' OR Type LIKE '%"
    tup4 = enth.get()
    tup5 = "%' OR Model LIKE '%"
    tup6 = enth.get()
    tup7 = "%' OR Manufacturer LIKE '%"
    tup8 = enth.get()
    tup9 = "%'"
    tuples = tup1 + tup2 + tup3 + tup4 + tup5 + tup6 + tup7 + tup8 + tup9
    cursor.execute(tuples)
    rows = cursor.fetchall()
    rows = [tuple(item.strip() for item in row) for row in rows]
    update_hardware(rows)
    if len(rows) == 0:
        cursor.execute("SELECT COUNT (*) FROM Hardware")
        rowcount = cursor.fetchone()[0]
        labelcount2h.config(searchframeh,text="Total records: %s" % rowcount)
    else:
        tup_1 = "SELECT COUNT (*) FROM Hardware WHERE [User] LIKE '%"
        tup_2 = ent.get()
        tup_3 = "%' OR Type LIKE '%"
        tup_4 = ent.get()
        tup_5 = "%' OR Model LIKE '%"
        tup_6 = ent.get()
        tup_7 = "%' OR Manufacturer LIKE '%"
        tup_8 = ent.get()
        tup_9 = "%'"
        tuples2 = tup_1 + tup_2 + tup_3 + tup_4 + tup_5 + tup_6 + tup_7 + tup_8 + tup_9
        cursor.execute(tuples2)
        rowcount = cursor.fetchone()[0]
        labelcount2h.config(text="Total records: %s" % rowcount)
        labelcount2h.pack(side=tk.TOP,padx=6)
#update hardware rows
def update_hardware(rows):
    global update
    trvh.delete(*trvh.get_children())
    for i in rows:
        trvh.insert('','end',values=i)
##########*Network*##########
def network_screen():
    global networkscreen
    networkscreen = Tk()
    networkscreen.geometry("1366x768")
    networkscreen.title("JapaINV")
    networkscreen.iconbitmap(icon)
    networkscreen.resizable(False,False)
    networkscreenbg = PhotoImage(file = bg_inv)
    
    global canvas_ns
    canvas_ns = Canvas(networkscreen,width=1366, height=768)
    canvas_ns.pack(fill = "both", expand=True)
    canvas_ns.create_image(0,0, image = networkscreenbg, anchor = "nw")

    network = PhotoImage(file = "images/network.png")
    network_button = Button(text="", image=network,highlightthickness=0,bd=0, command=None)
    network_canvas = canvas_ns.create_window(1000,58,anchor="center",window=network_button)

    selected_window = PhotoImage(file= "images/network.png")
    selected_window_button = Button(text="", image=selected_window,highlightthickness=0,bd=0,command=None)
    selected_window_canvas = canvas_ns.create_window(163,235,anchor="center",window=selected_window_button)

    user_button = Button(networkscreen,text=login.get(),fg="white",bg="#00b5ff", font="Calibri 20 bold",highlightthickness=0,bd=0,command=sign_out)
    user_canvas = canvas_ns.create_window(1300,35,anchor="center",window=user_button)

    back = PhotoImage(file= "images/back.png")
    back_button = Button(text="",image=back,highlightthickness=0,bd=0,command=exitnet_startmain)
    back_canvas = canvas_ns.create_window(1305,92,anchor="center",window=back_button)

    #TREEVIEW FRAME
    networkframe = LabelFrame(canvas_ns, text="")
    networkframe.place(x=75, y=245,height=500, width=545)
    global trvn
    trvn = ttk.Treeview(networkframe, columns=(1,2,3,4,5), show="headings", height="20")
    trvn.pack()
    trvn.heading(1, text="Type")
    trvn.heading(2, text="Model")
    trvn.heading(3, text="Manufacturer")
    trvn.heading(4, text="IP Address")
    trvn.heading(5, text="Description")

    trvn.column(1, minwidth=100, width=100)
    trvn.column(2, minwidth=100, width=100)
    trvn.column(3, minwidth=100, width=100)
    trvn.column(4, minwidth=100, width=100)
    trvn.column(5, minwidth=100, width=100)
    trvn.bind('<Double 1>', getrow_network)

    networkquery = "SELECT * FROM Network"
    cursor.execute(networkquery)
    rows = cursor.fetchall()
    rows = [tuple(item.strip() for item in row) for row in rows]
    update_network(rows)
    
    cursor.execute("SELECT COUNT (*) FROM Network")
    rowcount = cursor.fetchone()[0]

    #SEARCH FRAME
    searchimagen = PhotoImage(file = "images/search.png")
    searchimagen_button = Button(text="", image=searchimagen,highlightthickness=0,bd=0, command=None)
    searchimagen_canvas = canvas_ns.create_window(719,235,anchor="center",window=searchimagen_button)
    global searchframen
    searchframen = LabelFrame(canvas_ns, text="")
    searchframen.place(x=650, y=245, height=150, width=350)
    lbln = Label(searchframen, text="")
    lbln.pack(side=tk.TOP, padx=10)
    global labelcount2n
    labelcount2n = Label(searchframen, text="Total records: %s" % rowcount)
    labelcount2n.pack(side=tk.TOP, padx=6)

    labelcountn = Label(canvas_ns, text="Total records: %s" % rowcount)
    labelcountn.place(x=260,y=230)
    global entn
    entn = Entry(searchframen)
    entn.pack(side=tk.LEFT, padx=6)
    entn.focus()
    searchbtnimagen = PhotoImage(file="images/searchbtn.png")
    btnn = Button(searchframen, text="Search",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command=search_network)
    btnn.pack(side=tk.LEFT, padx=6)
    clearbtnimagen = PhotoImage(file="images/clearbtn.png")
    btn2n = Button(searchframen, text="Clear",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command=allquery_network)
    btn2n.pack(side=tk.LEFT,padx=6)
    refreshbtnimagen = PhotoImage(file="images/refreshbtn.png")
    btn3n = Button(searchframen, text="Refresh",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command=allquery_network)
    btn3n.pack(side=tk.LEFT, padx=6)

    queryimagen = PhotoImage(file="images/query.png")
    queryimage_buttonn = Button(text="",image=queryimagen,highlightthickness=0,bd=0,command=None)
    queryimage_canvasn = canvas_ns.create_window(719,435,anchor="center",window=queryimage_buttonn)
    #USER DATA SECTION
    userdataframen = LabelFrame(canvas_ns, text="")
    userdataframen.place(x=650, y=445, height=300, width=350)
    filler1n = Label(userdataframen, text="Create a new entry")
    filler1n.grid(row=0,column=0,padx=5,pady=3)
    filler2n = Label(userdataframen, text="")
    filler2n.grid(row=1,column=1,padx=5,pady=3)
    global typeentn
    typelbln = Label(userdataframen, text="Type")
    typelbln.grid(row=2,column=0,padx=5,pady=3)
    typeentn = Entry(userdataframen, textvariable=typen)
    typeentn.grid(row=2,column=1,padx=5,pady=3)
    global modelentn
    modellbln = Label(userdataframen,text="Model")
    modellbln.grid(row=3,column=0,padx=5,pady=3)
    modelentn = Entry(userdataframen,textvariable=modeln)
    modelentn.grid(row=3,column=1,padx=5,pady=3)
    global manuentn
    manulbln = Label(userdataframen, text="Manufacturer")
    manulbln.grid(row=4,column=0,padx=5,pady=3)
    manuentn = Entry(userdataframen, textvariable=manun)
    manuentn.grid(row=4,column=1,padx=5,pady=3)
    global ipadrentn
    ipadrlbln = Label(userdataframen, text="IP Address")
    ipadrlbln.grid(row=5,column=0,padx=5,pady=3)
    ipadrentn = Entry(userdataframen,textvariable=ipadr)
    ipadrentn.grid(row=5,column=1,padx=5,pady=3)
    global descentn
    desclbln = Label(userdataframen, text="Description")
    desclbln.grid(row=6,column=0,padx=5,pady=3)
    descentn = Entry(userdataframen,textvariable=descn)
    descentn.grid(row=6,column=1,padx=5,pady=3)

    add_btnn = Button(userdataframen, text="Add New",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command = add_new_network)
    add_btn_ttpn = CreateToolTip(add_btnn, "Add a new entry")
    delete_btnn = Button(userdataframen, text="Delete",bg="#00b5ff",fg="#ffffff",font=('Helvetica', 10, 'bold'),highlightthickness=0,bd=0, command = delete_entry_network)
    delete_btn_ttpn = CreateToolTip(delete_btnn, "Delete the selected entry (Double click entry)")
    filler3n = Label(userdataframen, text="")
    filler3n.grid(row=7,column=0,padx=5,pady=3)

    add_btnn.grid(row=8,column=0,padx=5,pady=3)
    delete_btnn.grid(row=8,column=1,padx=5,pady=3)

    networkscreen.mainloop()
#Get rows network
def getrow_network(events):
    rowid = trvn.identify_row(events.y)
    item = trvn.item(trvn.focus())
    typen.set(item['values'][0])
    modeln.set(item['values'][1])
    manun.set(item['values'][2])
    ipadr.set(item['values'][3])
    descn.set(item['values'][4])
#add new network
def add_new_network():
    cursor.execute("INSERT INTO Network (Type,Model,Manufacturer,IpAddress,Description) VALUES (?,?,?,?,?)",typeentn.get(),modelentn.get(),manuentn.get(),ipadrentn.get(),descentn.get())
    cursor.commit()
    allquery_network()
#Delete network
def delete_entry_network():
    user_id = ipadr.get()
    if messagebox.askyesno("Confirm deletion", "Are you sure you want to delete this item?"):
        cursor.execute("DELETE FROM Network WHERE IPAddress = (?)",ipadr.get())
        cursor.commit()
        allquery_network()
    else:
        return True
#Allquery network
def allquery_network():
    computerquery = "SELECT * FROM Network"
    cursor.execute(computerquery)
    rows = cursor.fetchall()
    rows = [tuple(item.strip() for item in row) for row in rows]
    update_network(rows)
    cursor.execute("SELECT COUNT (*) FROM Computers")
    rowcount = cursor.fetchone()[0]
    labelcount2n.config(text="Total records: %s" % rowcount)
    labelcount2n.pack(side=tk.TOP,padx=6)
#Search network
def search_network():
    global search
    tup1 = "SELECT * FROM Network WHERE Type LIKE '%"
    tup2 = entn.get()
    tup3 = "%' OR Model LIKE '%"
    tup4 = entn.get()
    tup5 = "%' OR Manufacturer LIKE '%"
    tup6 = entn.get()
    tup7 = "%' OR IPAddress LIKE '%"
    tup8 = entn.get()
    tup9 = "%'"
    tuples = tup1 + tup2 + tup3 + tup4 + tup5 + tup6 + tup7 + tup8 + tup9
    cursor.execute(tuples)
    rows = cursor.fetchall()
    rows = [tuple(item.strip() for item in row) for row in rows]
    update_network(rows)
    if len(rows) == 0:
        cursor.execute("SELECT COUNT (*) FROM Network")
        rowcount = cursor.fetchone()[0]
        labelcount2n.config(canvas_ps,text="Total records: %s" % rowcount)
    else:
        tup_1 = "SELECT COUNT (*) FROM Network WHERE Type LIKE '%"
        tup_2 = ent.get()
        tup_3 = "%' OR Model LIKE '%"
        tup_4 = ent.get()
        tup_5 = "%' OR Manufacturer LIKE '%"
        tup_6 = ent.get()
        tup_7 = "%' OR IPAddress LIKE '%"
        tup_8 = ent.get()
        tup_9 = "%'"
        tuples2 = tup_1 + tup_2 + tup_3 + tup_4 + tup_5 + tup_6 + tup_7 + tup_8 + tup_9
        cursor.execute(tuples2)
        rowcount = cursor.fetchone()[0]
        labelcount2n.config(text="Total records: %s" % rowcount)
        labelcount2n.pack(side=tk.TOP,padx=6)
#update network rows
def update_network(rows):
    global update
    trvn.delete(*trvn.get_children())
    for i in rows:
        trvn.insert('','end',values=i)


def sign_in():
    cursor.execute("SELECT * FROM login WHERE login = (?)",login.get())
    myresult = cursor.fetchall()
    if myresult:
        cursor.execute("SELECT * FROM login WHERE Password = (?)",password.get())
        mypass = cursor.fetchall()
        if mypass:
            messagebox.showinfo("Success", "You have signed in")
            signin.destroy()
            main_login.destroy()
            inventory_screen()
        if not mypass:
            messagebox.showerror("Error", "Incorrect password")
            signin.focus()
    if not myresult:
        messagebox.showerror("Error", "User does not exist")
        signin.focus()

def sign_out():
    inventory.destroy()

def sign_up_screen():
    global signup
    signup = tk.Toplevel()
    signup.geometry("375x175")
    signup.title("JapaINV")
    signup.iconbitmap(icon)
    signup.resizable(False,False)

    bg_signup = PhotoImage(file="images/create2.png")
    label1 = Label(signup, image=bg_signup)
    label1.place(x=0,y=0)

    email_label = Label(signup, text="Username:")
    email_label.pack(expand=False)

    email_entry = Entry(signup, textvariable=login)
    email_entry.pack(expand=False)
    email_entry.focus()

    # password
    password_label = Label(signup, text="Password:")
    password_label.pack(expand=False)

    password_entry = Entry(signup, textvariable=password, show="*")
    password_entry.pack(expand=False)

    sign_up_button = ttk.Button(signup, text="Sign Up", command=create_user)
    sign_up_button.pack(expand=False, pady=10)
    signup.mainloop()

def create_user():
    cursor.execute("SELECT * FROM login WHERE login = (?)",login.get())
    myresult = cursor.fetchall()
    if myresult:
        messagebox_username_taken()
        signup.focus()
    if not myresult:
        cursor.execute("INSERT INTO login(Login,Password) VALUES (?,?)",login.get(),password.get())
        cursor.commit()
        messagebox_user_created()
        signup.destroy()

def messagebox_username_taken():
    messagebox.askretrycancel("Username taken", "Try again?")

def messagebox_user_created():
    messagebox.showinfo("User created", "User has been created")

def exit_inv():
    inventory.destroy()

def exit_com():
    computersscreen.destroy()

def exit_pho():
    phonesscreen.destroy()

def exit_hdw():
    hardwarescreen.destroy()

def exit_net():
    networkscreen.destroy()

def githublink():
    webbrowser.open(url2,new=new)

main_login.geometry('500x500')
main_login.title('JapaINV')
main_login.iconbitmap(icon)
main_login.resizable(False,False)
bg = PhotoImage(file = "images/create.png")
canvas_ml = Canvas(main_login, width=500, height=500,border=0)
canvas_ml.pack(fill = "both", expand=True)
canvas_ml.create_image(0,0, image = bg, anchor="nw")

bg_login = PhotoImage(file = r"images/login.png")
bg_sign_up = PhotoImage(file= r"images/sign_up.png")
login_button = Button(text="",image=bg_login,highlightthickness=0,bd=0, command=login_screen)
sign_up_button = Button(text="",image=bg_sign_up,highlightthickness=0,bd=0, command=sign_up_screen)
start_canvas = canvas_ml.create_window(250,200,anchor="center",window=login_button)
exit_canvas = canvas_ml.create_window(250,300,anchor="center",window=sign_up_button)

#main_login.mainloop()