from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

     
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="blueviolet",fg="white")
        title_lbl.place(x=0,y=3,width=1530,height=55)

        img_top=Image.open (r"images\b8.png")
        img_top=img_top.resize( (1530, 720) , Image.ANTIALIAS)
        self.photoimg_top=ImageTk . PhotoImage (img_top)

        f_lbl=Label(self.root, image =self. photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=750)

        dep_label=Label(f_lbl, text= "Email:apoorva.keshu@gmail.com", font=("times new roman", 20, "bold"),bg="yellow")
        dep_label.place(x=550,y=220)


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()