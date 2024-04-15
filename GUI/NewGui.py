from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image

#Setup
GUI = CTk()
GUI.geometry("1000x500")
set_appearance_mode("dark")

#image names
image1 = ImageTk.PhotoImage(Image.open('side-image.jpg'))

#frame for custom image
frame1 = CTkFrame(master=GUI, width=500,height=500,image=image1)
frame1.grid(row=0,column=0,columnspan=2,rowspan=7)

GUI.mainloop()