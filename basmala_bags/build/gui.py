
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,Label ,messagebox ,Frame
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
import sqlite3
import time
from PIL import Image, ImageTk
import customtkinter

#cunters
qty=0
qty1=0
qty2=0
qty3=0
qty4=0
qty5=0
qty6=0
qty7=0
qty8=0

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\basmala_bags\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#new_invice()
def new_invoice():
    tree.delete(*tree.get_children())
    
    invoice_list.clear()

def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = "basmala"
    phone = "666-666"
    subtotal = sum(item[3] for item in invoice_list) 
    salestax = 0.1
    total = subtotal*(1-salestax)
    
    doc.render({"name":name, 
            "phone":phone,
            "invoice_list": invoice_list,
            "subtotal":subtotal,
            "salestax":str(salestax*100)+"%",
            "total":total})
    
    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)
    
    messagebox.showinfo("Invoice Complete", "Invoice Complete")
    
   
    new_invoice()    


def enter_data(qt,descz,pricez,totalz):
    
    # Create Table
    conn = sqlite3.connect('data1.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS bags_data 
            (qt INT, descz TEXT, pricez FLOAT, totalz FLOAT )
    '''
    conn.execute(table_create_query)
    
    # Insert Data
    data_insert_query = '''INSERT INTO bags_data (qt, descz, pricez, 
    totalz) VALUES 
    (?, ?, ?,?)'''
    data_insert_tuple = (qt,
                          descz, pricez, totalz)
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()
   
window = Tk()

window.geometry("1512x982")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 982,
    width = 1512,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

#create  a tree 
columns = ('qty', 'desc', 'price', 'total')
tree = ttk.Treeview(window, columns=columns, show="headings")
tree.heading('qty', text='Qty')
tree.heading('desc', text='Description')
tree.heading('price', text='Unit Price')
tree.heading('total', text="Total")
tree.place(x=418,
    y=658,
    width=741,
    height=249)


# i1

invoice_list = []
#cinters defs
def itemplus():
    global qty
    qty+=1
    my_label.config(text = qty)

def itemmins():
    global qty
    if(qty>0):
         qty-=1
    my_label.config(text = qty)
#adding iteam in tree 
def add_item():
    global qty
    if(qty>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty*price
         invoice_item = [qty, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label= Label(window,text = qty)
my_label.place(x=202,
    y=271,
    width=45,
    height=45)
#-------------------------------------------------
#2
def item1plus():
    global qty1
    qty1+=1
    my_label1.config(text = qty1)

def item1mins():
    global qty1
    if(qty1>0):
         qty1-=1
    my_label1.config(text = qty1)
#adding iteam in tree 
def add_item1():
    global qty1
    if(qty1>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty1*price
         invoice_item = [qty1, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty1,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label1= Label(window,text = qty1)
my_label1.place(x=536,
    y=268,
    width=45,
    height=45)
#-------------------------------------------------
#3

def item2plus():
    global qty2
    qty2+=1
    my_label2.config(text = qty2)

def item2mins():
    global qty2
    if(qty2>0):
         qty2-=1
    my_label2.config(text = qty2)
#adding iteam in tree 
def add_item2():
    global qty2
    if(qty2>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty2*price
         invoice_item = [qty2, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty2,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label2= Label(window,text = qty2)
my_label2.place(x=868,
    y=269,
    width=45,
    height=45)
#-------------------------------------------------
#4
def item3plus():
    global qty3
    qty3+=1
    my_label3.config(text = qty3)

def item3mins():
    global qty3
    if(qty3>0):
         qty3-=1
    my_label3.config(text = qty3)
#adding iteam in tree 
def add_item3():
    global qty3
    if(qty3>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty3*price
         invoice_item = [qty3, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty3,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label3= Label(window,text = qty3)
my_label3.place(x=1227,
    y=273,
    width=45,
    height=45)
#-------------------------------------------------
#5
def item4plus():
    global qty4
    qty4+=1
    my_label4.config(text = qty4)

def item4mins():
    global qty4
    if(qty4>0):
         qty4-=1
    my_label4.config(text = qty4)
#adding iteam in tree 
def add_item4():
    global qty4
    if(qty4>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty4*price
         invoice_item = [qty4, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty4,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label4= Label(window,text = qty4)
my_label4.place(x=374,
    y=578,
    width=45,
    height=45)
#-------------------------------------------------
#6
def item5plus():
    global qty5
    qty5+=1
    my_label5.config(text = qty5)

def item5mins():
    global qty5
    if(qty5>0):
         qty5-=1
    my_label5.config(text = qty5)
#adding iteam in tree 
def add_item5():
    global qty5
    if(qty5>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty5*price
         invoice_item = [qty5, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty5,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label5= Label(window,text = qty5)
my_label5.place(x=701,
    y=586,
    width=45,
    height=45)
#-------------------------------------------------
#7
def item6plus():
    global qty6
    qty6+=1
    my_label6.config(text = qty6)

def item6mins():
    global qty6
    if(qty6>0):
         qty6-=1
    my_label6.config(text = qty6)
#adding iteam in tree 
def add_item6():
    global qty6
    if(qty6>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty6*price
         invoice_item = [qty6, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty6,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label6= Label(window,text = qty6)
my_label6.place(x=1084,
    y=583,
    width=45,
    height=45)
#-------------------------------------------------
#8
def item7plus():
    global qty7
    qty7+=1
    my_label7.config(text = qty7)

def item7mins():
    global qty7
    if(qty7>0):
         qty7-=1
    my_label7.config(text = qty7)
#adding iteam in tree 
def add_item7():
    global qty7
    if(qty7>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty7*price
         invoice_item = [qty7, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty7,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label7 = Label(window,text = qty7)
my_label7.place(x=191,
    y=905,
    width=45,
    height=45)
#-------------------------------------------------
#9
def item8plus():
    global qty8
    qty8+=1
    my_label8.config(text = qty8)

def item8mins():
    global qty8
    if(qty8>0):
         qty8-=1
    my_label8.config(text = qty8)
#adding iteam in tree 
def add_item8():
    global qty8
    if(qty8>0):
         desc = "stitch  galaxy space backpack"
         price = 170.00
         line_total= qty8*price
         invoice_item = [qty8, desc, price, line_total]
         tree.insert('',0, values=invoice_item)
         enter_data(qty8,desc,price,line_total)
         invoice_list.append(invoice_item)

my_label8 = Label(window,text = qty8)
my_label8.place(x=1272,
    y=894,
    width=45,
    height=45)
#-------------------------------------------------



image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    756.0,
    493.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item(),
    relief="flat"
)
button_1.place(
    x=110.0,
    y=17.0,
    width=257.0,
    height=228.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item4(),
    relief="flat"
)
button_2.place(
    x=268.0,
    y=318.0,
    width=293.0,
    height=240.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item7(),
    relief="flat"
)
button_3.place(
    x=46.0,
    y=658.0,
    width=350.0,
    height=236.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item1(),
    relief="flat"
)
button_4.place(
    x=433.0,
    y=13.0,
    width=291.0,
    height=229.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item5(),
    relief="flat"
)
button_5.place(
    x=618.0,
    y=333.0,
    width=285.0,
    height=232.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item8(),
    relief="flat"
)
button_6.place(
    x=1187.0,
    y=644.0,
    width=294.0,
    height=234.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item2(),
    relief="flat"
)
button_7.place(
    x=791.0,
    y=20.0,
    width=255.0,
    height=225.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item3(),
    relief="flat"
)
button_8.place(
    x=1131.0,
    y=26.0,
    width=272.0,
    height=242.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_item6(),
    relief="flat"
)
button_9.place(
    x=997.0,
    y=333.0,
    width=263.0,
    height=232.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: itemmins(),
    relief="flat"
)
button_10.place(
    x=266.218017578125,
    y=271.0,
    width=43.108428955078125,
    height=43.60453796386719
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item1mins(),
    relief="flat"
)
button_11.place(
    x=604.3798217773438,
    y=270.0,
    width=43.10844421386719,
    height=43.47840881347656
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item2mins(),
    relief="flat"
)
button_12.place(
    x=925.2981567382812,
    y=271.0,
    width=43.10844421386719,
    height=43.60453796386719
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item3mins(),
    relief="flat"
)
button_13.place(
    x=1303.5416259765625,
    y=273.9999694824219,
    width=43.10845947265625,
    height=43.56495666503906
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item5mins(),
    relief="flat"
)
button_14.place(
    x=777.8001708984375,
    y=588.0,
    width=43.10844039916992,
    height=43.52296447753906
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item4mins(),
    relief="flat"
)
button_15.place(
    x=452.218017578125,
    y=576.0,
    width=43.108428955078125,
    height=43.52296447753906
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item7mins(),
    relief="flat"
)
button_16.place(
    x=266.218017578125,
    y=906.6270751953125,
    width=43.108428955078125,
    height=43.108428955078125
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item8mins(),
    relief="flat"
)
button_17.place(
    x=1338.8001708984375,
    y=896.6691284179688,
    width=43.10845947265625,
    height=43.108428955078125
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item6mins(),
    relief="flat"
)
button_18.place(
    x=1151.5416259765625,
    y=584.6270751953125,
    width=43.108428955078125,
    height=43.10844421386719
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    157.0,
    292.5,
    image=image_image_2
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: itemplus(),
    relief="flat"
)
button_19.place(
    x=135.9346923828125,
    y=271.49609375,
    width=43.10845947265625,
    height=43.10844421386719
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item1plus(),
    relief="flat"
)
button_20.place(
    x=474.0,
    y=269.0,
    width=43.10844421386719,
    height=43.10844421386719
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item2plus(),
    relief="flat"
)
button_21.place(
    x=812.0,
    y=270.0,
    width=43.10844421386719,
    height=43.10844421386719
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item3plus(),
    relief="flat"
)
button_22.place(
    x=1149.0,
    y=273.0,
    width=43.108428955078125,
    height=43.10844421386719
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item6plus(),
    relief="flat"
)
button_23.place(
    x=1022.0,
    y=585.0,
    width=43.108428955078125,
    height=43.10844421386719
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item5plus(),
    relief="flat"
)
button_24.place(
    x=634.0,
    y=588.0,
    width=43.10844421386719,
    height=43.10844421386719
)

button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item4plus(),
    relief="flat"
)
button_25.place(
    x=307.0,
    y=577.0,
    width=43.108428955078125,
    height=43.10844421386719
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item7plus(),
    relief="flat"
)
button_26.place(
    x=134.0,
    y=907.0,
    width=43.10845947265625,
    height=43.108428955078125
)

button_image_27 = PhotoImage(
    file=relative_to_assets("button_27.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: item8plus(),
    relief="flat"
)
button_27.place(
    x=1208.5169677734375,
    y=894.0,
    width=43.108428955078125,
    height=45.777618408203125
)

button_image_28 = PhotoImage(
    file=relative_to_assets("button_28.png"))
button_28 = Button(
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: new_invoice(),
    relief="flat"
)
button_28.place(
    x=418.0,
    y=918.0,
    width=332.0,
    height=57.0
)

button_image_29 = PhotoImage(
    file=relative_to_assets("button_29.png"))
button_29 = Button(
    image=button_image_29,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: generate_invoice(),
    relief="flat"
)
button_29.place(
    x=827.0,
    y=916.0,
    width=332.0,
    height=57.0
)
def check():
    if entry_user.get()=="basmala" and entry_pass.get()=="123":
        LOGIN.destroy()
        
LOGIN = Frame( window)

# Create a photoimage object of the image in the path
# 1440x950
LOGIN.place(x=0,y=0,width=1512,height=982)
LOGIN.configure(background="white")
LOGIN_IM = Image.open(r"D:\basmala_bags\build\assets\frame0\Desktop - 1.png")
test_LOGIN = ImageTk.PhotoImage(LOGIN_IM)
LOGOIN = Label(LOGIN,background="white",image=test_LOGIN).place(
    x=0,
    y=0,
    
)






entry_user = customtkinter.CTkEntry(master=LOGIN,
                               placeholder_text="USERNAME",
                               placeholder_text_color="#1E1E1E",
                               text_color="#1E1E1E",
                               fg_color=("white","white"),
                               
                               width=582,
                               height=61,
                               border_width=2,
                               border_color=("#1E1E1E","#1E1E1E"),
                               corner_radius=20)
entry_user.place(x=790,y=473)

entry_pass = customtkinter.CTkEntry(master=LOGIN,
                               placeholder_text="Password",
                               placeholder_text_color="#1E1E1E",
                               text_color="#1E1E1E",
                               fg_color=("white","white"),
                               width=582,
                               height=61,
                               show="*",
                               border_width=2,
                               border_color=("#1E1E1E","#1E1E1E"),
                               corner_radius=20)
entry_pass.place(x=790,y=618)

button_login = customtkinter.CTkButton(master=LOGIN,
                                 #text="LOGIN",
                                 width=308,
                                 height=66,
                                 fg_color=("#1E1E1E","#1E1E1E"),
                                 border_width=0,
                                 corner_radius=20,
                                 text="LOGIN",
                                 command=check)
button_login.place(x=925,y=751)



#LOGO.image = test

w = Frame( window)
# Create a photoimage object of the image in the path
w.place(x=0,y=0,width=1512,height=982)
image1 = Image.open(r"D:\basmala_bags\build\assets\frame0\MacBook Air - 1.png")
test = ImageTk.PhotoImage(image1)
LOGO = Label(w,image=test).pack()
#LOGO.image = test

window.after(2000,lambda:w.destroy())

window.resizable(False, False)
window.mainloop()
