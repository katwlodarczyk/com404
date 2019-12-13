from tkinter import *
from tkinter import messagebox
import time

class Gui(Tk):

    # initialise window
    def __init__(self):
        super().__init__()
        
        # load resources
        self.plane_image = PhotoImage(file="C:/Users/dcarter/Documents/code/com404/com404/2-guis/5-animation/3-varying-ticks/plane.gif")
        # set window attributes
        self.title("Gui")
        self.configure(height=500,width=500)
        
        #set animation components
        self.plane_x_pos = 100
        self.plane_y_pos = 250
        self.plane_x_change = 1
        self.plane_y_change = 0
        self.num_tick = 0

        # add components
        self.__add_plane_image_label()
        self.__add_up_button()
        self.__add_down_button()

        #start the timer
        self.tick()

    def tick(self):
        self.num_tick +=1

        if self.num_tick % 1 == 0:
            if self.plane_x_pos >= 450 or self.plane_x_pos <=0:
                self.plane_x_change *= -1

            self.plane_x_pos = self.plane_x_pos+self.plane_x_change

            if not (self.plane_y_pos >=450 and self.plane_y_change == 1) and not (self.plane_y_pos <=0 and self.plane_y_change == -1):
                self.plane_y_pos = self.plane_y_pos+self.plane_y_change

            self.plane_image_label.place(x=self.plane_x_pos,y=self.plane_y_pos)

        self.after(5, self.tick)

    #the image
    def __add_plane_image_label(self):
        self.plane_image_label = Label()
        self.plane_image_label.place(x=self.plane_x_pos,y=self.plane_y_pos)
        self.plane_image_label.configure(image=self.plane_image)

    def __add_up_button(self):
        #create
        self.up_button = Button()
        self.up_button.place(x=125,y=425)

        #style
        self.up_button.configure(
            width=10,
            bg="#fed",
            text="UP"
            )

        #events
        self.up_button.bind("<Button-1>",self.__up_button_clicked)  
        self.up_button.bind("<ButtonRelease-1>",self.__up_button_released)

    def __add_down_button(self):
        #create
        self.down_button = Button()
        self.down_button.place(x=275,y=425)

        #style
        self.down_button.configure(
            width=10,
            bg="#fed",
            text="down"
            )
        
        #events
        self.down_button.bind("<Button-1>",self.__down_button_clicked)  
        self.down_button.bind("<ButtonRelease-1>",self.__down_button_released)

    def __up_button_clicked(self,event):
        self.plane_y_change = -1

    def __up_button_released(self,event):
        self.plane_y_change = 0

    def __down_button_clicked(self,event):
        self.plane_y_change = 1

    def __down_button_released(self,event):
        self.plane_y_change = 0
