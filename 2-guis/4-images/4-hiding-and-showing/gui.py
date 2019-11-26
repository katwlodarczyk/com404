from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        #load resources
        self.tick_image = PhotoImage(file="tick.gif")
        self.cross_image = PhotoImage(file="cross.gif")
        
        # set window attributes
        self.title("Hotel Check In")
        self.configure( height= 500, width=500)
        
        # add components
        self.__add_heading_label()
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_passport_label()
        self.__add_passport_entry()
        self.__add_nights_label()
        self.__add_nights_entry()
        self.__add_name_image_label()
        self.__add_passport_image_label()
        self.__add_nights_image_label()
        self.__add_checkin_button()

    def __add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.grid(row=0, columnspan=3)
        #style
        self.heading_label.configure(text="Hotel Check In", font="Roboto 18", padx= 20)
        #handle events
        
    def __add_name_label(self):
        #create
        self.name_label= Label()
        self.name_label.grid(row=1,column=0, sticky=W)
        #style
        self.name_label.configure(text="Name", font="Roboto,18", pady=10)
        #handle events

    def __add_name_entry(self):
        #create
        self.name_entry = Entry()
        self.name_entry.grid(row=1, column=1)
        #style
        self.name_entry.configure(font="Roboto 18", relief="solid", bd=2)
        #handle events
        self.name_entry.bind("<KeyRelease>", self.name_image_change)
        self.name_entry.bind("<FocusOut>", self.name_image_change)
        

    def __add_name_image_label(self):
        #create
        self.name_image_label = Label()
        self.name_image_label.grid(row=1, column=2)
        #style
        self.name_image_label.configure(image= self.cross_image,
                                   width=30,
                                   height=30,
                                   padx=10,
                                   relief= "solid")
        #handle events

    def name_image_change(self, event):
        name = self.name_entry.get()
        if len(name) == 0:
            self.name_image_label.configure(image=self.cross_image)
        else:
            self.name_image_label.configure(image=self.tick_image)
        


    def __add_passport_label(self):
        #create
        self.passport_label= Label()
        self.passport_label.grid(row=2,column=0, sticky=W)
        #style
        self.passport_label.configure(text="Passport Number", font="Roboto,18", pady=10)
        #handle events

    def __add_passport_entry(self):
        #create
        self.passport_entry = Entry()
        self.passport_entry.grid(row=2, column=1)
        #style
        self.passport_entry.configure(font="Roboto 18", relief="solid", bd=2)
        #handle events
        self.passport_entry.bind("<KeyRelease>", self.passport_image_change)
        self.passport_entry.bind("<FocusOut>", self.passport_image_change)
        

    def __add_passport_image_label(self):
        #create
        self.passport_image_label = Label()
        self.passport_image_label.grid(row=2, column=2)
        #style
        self.passport_image_label.configure(image= self.cross_image,
                                   width=30,
                                   height=30,
                                   padx=10,
                                   relief= "solid")
        #handle events

    def passport_image_change(self, event):
        passport = self.passport_entry.get()
        if len(passport) == 0:
            self.passport_image_label.configure(image=self.cross_image)
        else:
            self.passport_image_label.configure(image=self.tick_image)
            

    def __add_nights_label(self):
        #create
        self.nights_label= Label()
        self.nights_label.grid(row=3,column=0, sticky=W)
        #style
        self.nights_label.configure(text="No. of nights", font="Roboto,18", pady=10)
        #handle events

    def __add_nights_entry(self):
        #create
        self.nights_entry = Entry()
        self.nights_entry.grid(row=3, column=1)
        #style
        self.nights_entry.configure(font="Roboto 18", relief="solid", bd=2)
        #handle events
        self.nights_entry.bind("<KeyRelease>", self.nights_image_change)
        self.nights_entry.bind("<FocusOut>", self.nights_image_change)
        

    def __add_nights_image_label(self):
        #create
        self.nights_image_label = Label()
        self.nights_image_label.grid(row=3, column=2)
        #style
        self.nights_image_label.configure(image= self.cross_image,
                                   width=30,
                                   height=30,
                                   padx=10,
                                   relief= "solid")
        #handle events

    def nights_image_change(self, event):
        name = self.nights_entry.get()
        if len(name) == 0:
            self.nights_image_label.configure(image=self.cross_image)
        else:
            self.nights_image_label.configure(image=self.tick_image)

    def __add_checkin_button(self):
        #create
        self.checkin_button= Button()
        self.checkin_button.grid(row=4, column=1)
        #style
        self.checkin_button.configure(text="Check In",
                                      font="Roboto 16",
                                      relief= "solid")
        #handle events
        self.checkin_button.bind("<ButtonRelease-1>", self.checkin_button_clicked)

    def checkin_button_clicked(self,event):
        
        messagebox.showinfo("Check In", "You succesfully checked in!")
 


# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()

