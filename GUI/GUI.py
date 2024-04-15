from tkinter import *
from customtkinter import *

#Setup
GUI = CTk()
GUI.geometry("1000x500")
set_appearance_mode("dark")

#Label for GUI
label = CTkLabel(master=GUI, text="ChopMatic Pro", font = ("Lalezar",90))
label.grid()

#Frame1
frame = CTkFrame(master=GUI,width=150,height=150,corner_radius=10,fg_color="#28A9DF")
frame.pack(side=LEFT)
#Frame1 Contents
frame1_label = CTkLabel(master=frame,text="Size",font=("Arial", 20),text_color="Black")
frame1_label.place(relx=.5,rely=.1,anchor="center")
dropdown = CTkComboBox(master=frame, values=["Small","Medium","Large"])
dropdown.place(relx=.5,rely=.5,anchor="center")

#Frame2
frame2 = CTkFrame(master=GUI,width=150,height=150,corner_radius=10,fg_color="#28A9DF")
frame2.pack(side=LEFT)
#Frame2 Contents
frame2_label = CTkLabel(master=frame2,text="Thickness",font=("Arial", 20),text_color="Black")
frame2_label.place(relx=.5,rely=.1,anchor="center")
entry = CTkEntry(master=frame2)
entry.place(relx=.5,rely=.5,anchor="center")

#Frame2
frame3 = CTkFrame(master=GUI,width=150,height=150,corner_radius=10,fg_color="#28A9DF")
frame3.pack(side=LEFT)
#Frame2 Contents
dropdown = CTkComboBox(master=frame3, values=["1","2","3",'4'])
dropdown.place(relx=.5,rely=.5,anchor="center")
frame3_label = CTkLabel(master=frame3,text="Slices Amount",font=("Arial", 20),text_color="Black")
frame3_label.place(relx=.5,rely=.1,anchor="center")

GUI.mainloop()