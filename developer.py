from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="blueviolet",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=60)

        img_top=Image.open (r"images\b11.jpg")
        img_top=img_top. resize( (1530, 720) , Image.ANTIALIAS)
        self . photoimg_top=ImageTk . PhotoImage (img_top)

        f_lbl=Label(self.root, image =self. photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        main_frame=Frame(f_lbl, bd=2,bg="white")
        main_frame.place (x=1052, y=0, width=500, height=230)

        img_top1=Image.open (r"images\apoorva.jpeg")
        img_top1=img_top1. resize( (250, 260) , Image.ANTIALIAS)
        self . photoimg_top1=ImageTk . PhotoImage (img_top1)

        f_lbl=Label(main_frame, image =self. photoimg_top1)
        f_lbl.place(x=300, y=-1.2, width=210, height=250)

        #developer info
        developer_label=Label(main_frame, text= " Hello, Myself Apoorva", font=("times new roman", 18, "bold"),bg="white")
        developer_label.place(x=0,y=5)
        developer_label=Label(main_frame, text= " I am full stack developer", font=("times new roman", 18, "bold"),bg="white")
        developer_label.place(x=0,y=40)
        developer_label=Label(main_frame, text= " Nice to meet you all!!", font=("times new roman", 18, "bold"),bg="white")
        developer_label.place(x=0,y=75)
        developer_label=Label(main_frame, text= " contact info:", font=("times new roman", 18, "bold"),bg="white")
        developer_label.place(x=0,y=105)
        developer_label=Label(main_frame, text= " apoorva.keshu@gmail.com", font=("times new roman", 18, "bold"),bg="white")
        developer_label.place(x=0,y=135)

        # img2=Image.open (r"images\image3.jpg")
        # img2=img2.resize ( (500, 390), Image .ANTIALIAS)
        # self. photoimg2=ImageTk.PhotoImage(img2)
        # f_lbl=Label (main_frame, image=self. photoimg2)
        # f_lbl.place (x=0,y=210, width=500, height=390)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()