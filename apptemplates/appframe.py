from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random



root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()



img = (Image.open("buttons_PNG3.png"))
resized = img.resize((50,50), Image.Resampling.LANCZOS)
myimg = ImageTk.PhotoImage(resized)

#PhotoImage(file="buttons_PNG3.png")



def update_entries():
    
    
    openfile = open("entrytext.txt", "r")
    openfile.seek(0)

    entrylist = openfile.readlines(50)
    labelstring = ""
    for entry in entrylist:
        labelstring = labelstring + entry
        

    entrydisplay = ttk.Label(frm, text=labelstring, width=100, justify=LEFT, anchor=CENTER)
    entrydisplay.grid(column=2, row=1)
    
    

    

def get_entry():
    stuff = ent.get()
    txtfile = open("entrytext.txt","a")
    txtfile.write(stuff + '\n')
    txtfile.close()
    update_entries()   

def change_label():
    num = str(random.randint(1, 100))

    label0.config(text=num)




label0 = ttk.Label(frm, text="Hello World!", foreground="red", background="yellow", cursor="spider", font='32')
label0.grid(column=0, row=0)

label1 = ttk.Label(frm, text="Entry Box", anchor=CENTER)
label1.grid(column=0, row=2)

ent = ttk.Entry(frm, text="Testing", font="Luminari")
ent.grid(column=0, row=3)

butt = ttk.Button(frm, text="Quit", width=24, cursor="heart", image=myimg, command=lambda:change_label())
butt.grid(column=1, row=0)

butt2 = ttk.Button(frm, text='Add entry', command=lambda:get_entry())
butt2.grid(column=1, row=3)

header = ttk.Label(frm, text="List of entries ", anchor=CENTER, font=('Arial', '24', 'bold'))
header.grid(column=2, row=0)




#command=root.destroy





root.mainloop()


