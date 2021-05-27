import random
from tkinter import *
from PIL import ImageTk,Image

fen= Tk()
fen.title("Flag_Game")
fen.geometry("1080x600")
fen.minsize(480, 360)
fen.iconbitmap("logo.ico")
lbl1=Label(fen, text= "Flag Game", font=("Monotype Corsiva", 20), bg= "orange",
           fg="red", bd=2, relief= SUNKEN)
lbl1.pack()

def start():
    flag1 = ImageTk.PhotoImage(Image.open("C:/Users/pc/Desktop/Python/Flag_project/Maroc.png"))
    flag2 = ImageTk.PhotoImage(Image.open("C:/Users/pc/Desktop/Python/Flag_project/Mali.png"))
    flag3 = ImageTk.PhotoImage(Image.open("C:/Users/pc/Desktop/Python/Flag_project/Egypte.png"))
    flag_list=[flag1, flag2, flag3]
    flag = random.choice(flag_list)
    lbl= Label(image=flag)
    lbl.place(x=400, y=200)

lbl2= Button(fen, text = "***Start***", font=("Sakkal Majalla", 15), bg= "yellow",
             fg="red", bd=5, relief= RAISED, command= start)
lbl2.place(x= 200, y= 80)

lbl3=Label(fen, text = " C'est le drapeau du :")
lbl3.place(x= 200, y= 380)
entrynbre3= Entry(fen)
entrynbre3.place(x= 350, y= 380)


button_quit= Button(fen, text= "Exit_Game", command= fen.quit)
button_quit.place(x=960, y= 500)
fen.mainloop()