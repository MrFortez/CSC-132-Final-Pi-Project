from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image

#Setup
GUI = CTk()
GUI.geometry("1055x600")
set_appearance_mode("dark")

#image names
image1 = CTkImage(Image.open("C:/Users/baili/Downloads/CSC-132-Final-Pi-Project/GUI/Images/side-image.jpg"), size=(525, 600))
image2 = CTkImage(Image.open("C:/Users/baili/Downloads/CSC-132-Final-Pi-Project/GUI/Images/text.png"),size = (530, 170))

#frame1 setup & contents
frame1 = CTkFrame(master=GUI, width=530,height=500,bg_color="transparent")
frame1.grid(row=0,column=0,columnspan=2,rowspan=7)
placed_image1 = CTkLabel(master=frame1, image=image1, text="")
placed_image1.grid(row=0,column=0,columnspan=2,rowspan=7)

#frame2 setup & contents
frame2 = CTkFrame(master=GUI, width=530,height=250)
frame2.grid(row=0,column=2,columnspan=3,rowspan=2)
placed_image2 = CTkLabel(master=frame2, image=image2, text="")
placed_image2.grid(row=2,column=0,columnspan=3,rowspan=2)

#frame3 setup & contents
frame3 = CTkFrame(master=GUI,width=265,height=200,fg_color="#81B0E0")
frame3.grid(row=2,column=4,columnspan=2,rowspan=2)
frame3.grid_propagate(False)
dropdown = CTkComboBox(master=frame3, values=["Small","Medium","Large"])
dropdown.grid(column=1,row=2)
frame3_label = CTkLabel(master=frame3,text="Size",font=("Arial", 20),text_color="Black")
frame3_label.grid(column=1,row=0)
frame3_label = CTkLabel(master=frame3,text="How big is the food?",font=("Arial", 20),text_color="Black")
frame3_label.grid(column=1,row=3)

#frame4 setup & contents
frame4 = CTkFrame(master=GUI,width=265,height=200,fg_color="#81B0E0")
frame4.grid(row=2,column=2,columnspan=2,rowspan=2)
frame4.grid_propagate(False)
frame4_label = CTkLabel(master=frame4,text="Thickness",font=("Lao UI", 20),text_color="Black")
frame4_label.grid(column=0,row=0,sticky=N)
frame4_label = CTkLabel(master=frame4,text="How thick are the cuts?",font=("Lao UI", 20),text_color="Black")
frame4_label.grid(column=0,row=2,sticky=N)
entry = CTkEntry(master=frame4)
entry.grid(column=0,row=1,sticky=S)

#frame5 setup & contents
frame5 = CTkFrame(master=GUI,width=265,height=200,fg_color="#81B0E0")
frame5.grid(row=4,column=2,columnspan=2,rowspan=2)
frame5.grid_propagate(False)
dropdown = CTkComboBox(master=frame5, values=["1","2","3",'4'])
dropdown.grid(column=0,row=1,sticky=S)
frame5_label = CTkLabel(master=frame5,text="Slices Amount",font=("Arial", 20),text_color="Black")
frame5_label.grid(column=0,row=0,sticky=N)
frame5_label = CTkLabel(master=frame5,text="How many slices?",font=("Arial", 20),text_color="Black")
frame5_label.grid(column=0,row=2,sticky=N)

#frame6 setup & contents
frame6 = CTkFrame(master=GUI,width=265,height=200,fg_color="#81B0E0")
frame6.grid(row=4,column=4,columnspan=2,rowspan=2)
frame6.grid_propagate(False)
dropdown = CTkComboBox(master=frame6, values=["Pizza Cut","Sliced","Diced"])
dropdown.grid(column=0,row=1,sticky=S)
frame6_label = CTkLabel(master=frame6,text="Type Of Cut",font=("Arial", 20),text_color="Black")
frame6_label.grid(column=0,row=0,sticky=N)
frame6_label = CTkLabel(master=frame6,text="What type of cut?",font=("Arial", 20),text_color="Black")
frame6_label.grid(column=0,row=2,sticky=N)


#Enter Button
button = CTkButton(master=GUI,text="ENTER",fg_color="#81B0E0")
button.grid(row=6,column=2,rowspan=3,columnspan=3)

GUI.mainloop()