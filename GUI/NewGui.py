from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
import os
# import serial
from time import sleep

# ser = serial.Serial('/dev/ttyACM0', 9600)

class App:
    def __init__(self) -> None:
        #Setup
        self.GUI = CTk()
        self.GUI.geometry("1055x600")
        set_appearance_mode("dark")

        #image names
        self.image1 = CTkImage(Image.open(os.path.join("GUI", "Images", "side-image.jpg")), size=(525, 600))
        self.image2 = CTkImage(Image.open(os.path.join("GUI", "Images", "text.png")),size = (530, 170))
        self.image3 = CTkImage(Image.open(os.path.join("GUI", "Images", "icon.png")),size = (256, 200))

        #frame1 setup & contents
        self.frame1 = CTkFrame(master=self.GUI, width=530,height=500,bg_color="transparent")
        self.frame1.grid(row=0,column=0,columnspan=2,rowspan=7)
        self.placed_image1 = CTkLabel(master=self.frame1, image=self.image1, text="")
        self.placed_image1.grid(row=0,column=0,columnspan=2,rowspan=7)

        #frame2 setup & contents
        self.frame2 = CTkFrame(master=self.GUI, width=530,height=250)
        self.frame2.grid(row=0,column=2,columnspan=3,rowspan=2)
        self.placed_image2 = CTkLabel(master=self.frame2, image=self.image2, text="")
        self.placed_image2.grid(row=2,column=0,columnspan=3,rowspan=2)

        #frame3 setup & contents
        self.frame3 = CTkFrame(master=self.GUI,width=265,height=200,fg_color="#81B0E0")
        self.frame3.grid(row=2,column=4,columnspan=2,rowspan=2)
        self.frame3.grid_propagate(False)
        # self.dropdown3 = CTkComboBox(master=self.frame3, values=["Small","Medium","Large"])
        # self.dropdown3.grid(column=1,row=2)
        self.frame3_label = CTkLabel(master=self.frame3,text="Size",font=("Arial", 20),text_color="Black")
        self.frame3_label.grid(column=1,row=0)
        self.frame3_label = CTkLabel(master=self.frame3,text="How big is the food? \n (Inches)",font=("Arial", 20),text_color="Black")
        self.frame3_label.grid(column=1,row=3)
        self.entry3 = CTkEntry(master=self.frame3)
        self.entry3.grid(column=1,row=2,sticky=S)

        #frame4 setup & contents
        self.frame4 = CTkFrame(master=self.GUI,width=265,height=200,fg_color="#81B0E0")
        self.frame4.grid(row=2,column=2,columnspan=2,rowspan=2)
        self.frame4.grid_propagate(False)
        self.frame4_label = CTkLabel(master=self.frame4,text="Thickness",font=("Lao UI", 20),text_color="Black")
        self.frame4_label.grid(column=0,row=0,sticky=N)
        self.frame4_label = CTkLabel(master=self.frame4,text="How thick are the cuts? \n (Inches)",font=("Lao UI", 20),text_color="Black")
        self.frame4_label.grid(column=0,row=2,sticky=N)
        self.entry4 = CTkEntry(master=self.frame4)
        self.entry4.grid(column=0,row=1,sticky=S)



        #frame5 setup & contents
        self.frame5 = CTkFrame(master=self.GUI,width=265,height=200,fg_color="#81B0E0")
        self.frame5.grid(row=4,column=2,columnspan=2,rowspan=2)
        self.frame5.grid_propagate(False)
        # self.dropdown5 = CTkComboBox(master=self.frame5, values=["1","2","3",'4'])
        # self.dropdown5.grid(column=0,row=1,sticky=S)
        self.entry5 = CTkEntry(master=self.frame5)
        self.entry5.grid(column=0,row=1,sticky=S)
        self.frame5_label = CTkLabel(master=self.frame5,text="Slices Amount",font=("Arial", 20),text_color="Black")
        self.frame5_label.grid(column=0,row=0,sticky=N)
        self.frame5_label = CTkLabel(master=self.frame5,text="How many slices?",font=("Arial", 20),text_color="Black")
        self.frame5_label.grid(column=0,row=2,sticky=N)
        self.entry5 = CTkEntry(master=self.frame5)
        self.entry5.grid(column=0,row=1,sticky=S)

        #frame6 setup & contents
        # frame6 = CTkFrame(master=GUI,width=265,height=200,fg_color="#81B0E0")
        # frame6.grid(row=4,column=4,columnspan=2,rowspan=2)
        # frame6.grid_propagate(False)
        # dropdown = CTkComboBox(master=frame6, values=["Pizza Cut","Sliced","Diced"])
        # dropdown.grid(column=0,row=1,sticky=S)
        # frame6_label = CTkLabel(master=frame6,text="Type Of Cut",font=("Arial", 20),text_color="Black")
        # frame6_label.grid(column=0,row=0,sticky=N)
        # frame6_label = CTkLabel(master=frame6,text="What type of cut?",font=("Arial", 20),text_color="Black")
        # frame6_label.grid(column=0,row=2,sticky=N)
        self.frame6 = CTkFrame(master=self.GUI, width=530,height=250)
        self.frame6.grid(row=4,column=4,columnspan=2,rowspan=2)
        self.button = CTkButton(master=self.frame6,text="Lets get Cutting!",fg_color="#81B0E0", text_color="#000000", command=self.beginCommand)
        self.button.grid(row=0,column=1,rowspan=3,columnspan=3)
        # self.placed_image3 = CTkLabel(master=self.frame6, image=self.image3, text="")
        # self.placed_image3.grid(row=2,column=0,columnspan=2,rowspan=2)

        self.GUI.mainloop()

    def beginCommand(self):
        responses = self.entry4.get() + " " + self.entry3.get() + " " + self.entry5.get()
        #dataToSend = " ".join(responses)
        print(responses)
        #ser.write(dataToSend.encode())
        # ser.write(responses.encode())
        #test = self.entry4.get()
        #ser.write(test.encode())
        print('poggers')

runGUI = App()