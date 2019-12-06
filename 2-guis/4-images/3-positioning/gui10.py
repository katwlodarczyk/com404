from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.map_image = PhotoImage(file="map.gif")
        self.bus_image = PhotoImage(file="bus.gif")
        
        # set window attributes
        self.title("Bus Journey")
        
        # add components
        self.__add_heading_label()
        self.__add_map_frame()
        self.__add_map_image_label()
        self.__add_bus_image_label()

    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        #style
        self.heading_label.configure(text="Bus Journey",
                                     font="Roboto 25")

    def __add_map_frame(self):
        self.map_frame = Frame()
        self.map_frame.grid(row=1, column=0)
        self.map_frame.configure(width=400, height=400)

    def __add_map_image_label(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(y=30)
        self.map_image_label.configure(image=self.map_image,
                                       height=399,
                                       width=399)

    def __add_bus_image_label(self):
        self.bus_image_label = Label(self.map_frame)
        self.bus_image_label.place(x=0, y=30)
        self.bus_image_label.configure(image=self.bus_image,
                                       height=75,
                                       width=80)
        #event
        self.bus_image_label.bind("<B1-Motion>", self.__bus_move)

    def __bus_move(self, event):
        #messagebox.showinfo("Bus Journey Gui", "Mouse x is" + str(event.x))
        #messagebox.showinfo("Bus Journey Gui", "Mouse y is" + str(event.y))

        #event
        self.bus_image_label.bind("<B1-Motion>", self.__bus_new)

    def __bus_new(self, event):
        self.bus_image_label.place(x=event.x, y=event.y)
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()