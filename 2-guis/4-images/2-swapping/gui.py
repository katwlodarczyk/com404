from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.cactus_image = PhotoImage(file="cactus.gif")
        self.cactus2_image = PhotoImage(file="cactus2.gif")
             # set window attributes
        self.title("Cactus")
        
        # add components
        self.__add_title_label()
        self.__add_cactus_image_label()
        self.__add_flip_button()

    def __add_title_label(self):
        self.title_label=Label()
        self.title_label.grid(row=0, columnspan=2, sticky= W+S+E+N)
        self.title_label.configure( text="CACTUS", font="Roboto 20",)

    def __add_cactus_image_label(self):
        self.cactus_image_label = Label()
        self.cactus_image_label.grid(row=1, column=0)
        self.cactus_image_label.configure(image=self.cactus_image)

    def __add_flip_button(self):
        self.flip_button= Button()
        self.flip_button.grid(row=2, column=0)
        self.flip_button.configure(text="Flip", relief="solid", font="Roboto 24")
        self.flip_button.bind("<ButtonRelease-1>", self.flip_button_clicked)
        self.flip_button.bind("<ButtonRelease-2>", self.flip_button3_clicked)

    def flip_button_clicked(self,event):
        self.cactus_image_label.configure(image = self.cactus2_image)

    def flip_button3_clicked(self,event):
        self.cactus_image_label.configure(image = self.cactus_image)

    
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
