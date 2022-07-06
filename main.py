# GANESH SHINGRE ----------- PROJECT 2  INVENTORY MANAGEMENT

from tkinter import *
from tkinter import messagebox
from tkinter import font

root = Tk()
root.title("INVENTORY MANAGEMENT")
root.geometry("1050x400")
root.configure(bg="powder blue")
frame_1=Frame(root,width=1050,height=400,bg="powder blue")

def insert_but():
    txt1=text_1.get()
    txt2=text_2.get()
    txt3=text_3.get()
    txt4=text_4.get()

    txt3_check=txt3.isnumeric()
    txt4_check=txt4.isnumeric()
    check = open('IInventory_Record.txt','a')
    check1 = open('Inventory_Record.txt','r')
    test = check1.read()

    if len(txt1)==0:
        messagebox.showwarning("title","Please Enter Product ID!!")

    elif len(txt2)==0:
        messagebox.showwarning("title","Please Enter Product Name!!")

    elif txt3_check==False or (int(txt3))==0:
       messagebox.showerror("Error","Enter valid Selling Price!!")
        
    elif txt4_check==False or (int(txt4))==0:
        messagebox.showerror("Error","Enter valid Quantity!!")
   
    elif txt1 in test:
        messagebox.showwarning("title","Product ID already exist!!")       

    else:
        file=open("Inventory_Record.txt","a")
        file.write("\n")
        file=open("Inventory_Record.txt","r")
        
        counter=1
        content= file.read()
        coList=content.split("\n")
        for i in coList:
            if i:
                counter+=1
        file = open("Inventory_Record.txt","a")
        index_no=str(counter)

        file.write("  ")
        file.write(index_no)
        file.write(".")
        file.write("\t      ")
        file.write(txt1)
        for i in range (0,16-len(txt1)):
            file.write(" ")
        file.write(txt2)
        for i in range (0,18-len(txt2)):
            file.write(" ")
        file.write(txt3)
        for i in range (0,19-len(txt3)):
            file.write(" ")
        file.write(txt4)
        file.close()
        text_1.delete(0,END)
        text_2.delete(0,END)
        text_3.delete(0,END)
        text_4.delete(0,END)
        messagebox.showinfo("info","Entry Successful !!")
        
def clear_but():
    text_1.delete(0,END)
    text_2.delete(0,END)
    text_3.delete(0,END)
    text_4.delete(0,END)
    textA_1.delete(1.0,END)
   
def show_but():
    textA_1.delete(1.0,END)
    with open("Inventory_Record.txt","r") as f:
        textA_1.insert(INSERT,f.read())

lab_1=Label(root,text=" INVENTORY MANAGEMENT ",font=("times 12 bold"),width=25,height=3,bg="cyan2")
lab_1.place(x=8,y=6)
lab_2=Label(root,text=" Product ID ",font=("Albertus 10 bold"),width=16,bg="CadetBlue1")
lab_2.place(x=8,y=86)
lab_3=Label(root,text=" Product Name ",font=("Albertus 10 bold"),width=16,bg="CadetBlue1")
lab_3.place(x=8,y=151)
lab_4=Label(root,text=" Selling Price ",font=("Albertus 10 bold"),width=16,bg="CadetBlue1")
lab_4.place(x=8,y=213)
lab_5=Label(root,text=" Quantity ",font=("Albertus 10 bold"),width=16,bg="CadetBlue1")
lab_5.place(x=8,y=277)
lab_6=Label(root,text=" PRODUCT LIST ",font=("times 12 bold"),width=88,height=1,bg="turquoise1")
lab_6.place(x=244,y=6)
lab_7=Label(root,text="  ",font=("times 19 bold"),width=53,height=1,bg="turquoise1")
lab_7.place(x=244,y=35)
lab_8=Label(root,text=" Item No ",font=("Albertus 10 bold"),width=8,bg="CadetBlue1")
lab_8.place(x=257,y=42)
lab_9=Label(root,text=" Product ID ",font=("Albertus 10 bold"),width=20,bg="CadetBlue1")
lab_9.place(x=335,y=42)
lab_10=Label(root,text=" Product Name ",font=("Albertus 10 bold"),width=20,bg="CadetBlue1")
lab_10.place(x=510,y=42)
lab_11=Label(root,text=" Selling Price ",font=("Albertus 10 bold"),width=20,bg="CadetBlue1")
lab_11.place(x=684,y=42)
lab_12=Label(root,text=" Quantity ",font=("Albertus 10 bold"),width=20,bg="CadetBlue1")
lab_12.place(x=858,y=42)

text_1=Entry(root,width=28,font="Courier 10 bold italic")
text_1.place(x=8,y=116)
text_2=Entry(root,width=28,font="Courier 10 bold italic")
text_2.place(x=8,y=179)
text_3=Entry(root,width=28,font="Courier 10 bold italic")
text_3.place(x=8,y=240)
text_4=Entry(root,width=28,font="Courier 10 bold italic")
text_4.place(x=8,y=304)

scroll_y=Scrollbar(root)
textA_1=Text(root,width=78,height=17,bg="light cyan",font="Courier 12 bold ",yscrollcommand=scroll_y.set)
textA_1.place(x=244,y=80)

scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textA_1.yview)
frame_1.pack(side=LEFT)

but_1=Button(root,text="Insert",width=6,height=1,bg="cyan",font=("Albertus 10 bold"),command=insert_but)
but_1.place(x=19,y=355)
but_2=Button(root,text="Show",width=6,height=1,bg="cyan",font=("Albertus 10 bold"),command=show_but)
but_2.place(x=90,y=355)
but_3=Button(root,text="Clear",width=6,height=1,bg="cyan",font=("Albertus 10 bold"),command=clear_but)
but_3.place(x=162,y=355)

root.mainloop()