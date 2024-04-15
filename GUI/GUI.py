from tkinter import *
import sv_ttk

class MainGUI(Frame):
    #constructor
    def __init__(self,parent):
        Frame.__init__(self, parent, bg="gray")
    
    #setting up the layout of the Food Cutter GUI    
    def setupGUI(self):
        #setup the label
        self.display = Label(self,text="FoodNinja",anchor=E,bg="gray",height=1,width=5, font=("Arial",40))
        self.display.grid(row=0,column=0,columnspan=5,sticky=E+W+N+S)
            

window = Tk()
window.title("FoodNinja")
p = MainGUI(window)
sv_ttk.set_theme("dark")

window.mainloop()
