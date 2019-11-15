#import all classes from the tkinter library
from tkinter import *

#class definition for our GUI
class Gui(Tk):
    #constructor for making Gui objects
    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Newsletter")
        self.configure(bg="#000",
                       height=500,
                       width=500)
        
        #add components to the window
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_frame()
        self.__add_email_label()
        self.__add_user_entry()
        self.__add_submit_button()

    def __add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)

        #style
        self.heading_label.configure( text="Receive our newsletter",
                                      bg= "#000",
                                      font= "Roboto 32 underline",
                                      fg= "#fff",
                                      padx= 25)
        
    def __add_instruction_label(self):
        #create
        self.instruction_label= Label()
        self.instruction_label.grid(row=1, column=0, columnspan=2)
        #style
        self.instruction_label.configure(text= "Please enter your e-mail address to receive our newsletter",
                                          bg= "#000",
                                          font= "Roboto, 12",
                                          fg= "#fff",
                                          padx=40)
        #handle events


    def __add_email_frame(self):
        self.email_frame= Frame()
        self.email_frame.grid(row=2, column=0, columnspan=2)
        #style
        self.email_frame.configure(bg="#000")
    
    def __add_email_label(self):
        #create
        self.email_label= Label(self.email_frame)
        self.email_label.grid(row=3, column=1, columnspan=1)
        #style
        self.email_label.configure(text= "E-mail:",
                                    bg= "#000",
                                    font= "Roboto 12",
                                    fg= "#fff",
                                    padx= 30,
                                    pady= 10,
                                   )
        
        #handle events

    def __add_user_entry(self):
        #create
        self.user_entry= Entry(self.email_frame)
        self.user_entry.grid(row=3, column=2, columnspan=1)
        #style
        self.user_entry.configure(font="Roboto 12")
        
        #handle events

    def __add_submit_button(self):
        #create
        self.submit_button= Button()
        self.submit_button.grid(row=4, column=0, columnspan=2)
        #style
        self.submit_button.configure(font= "Roboto 12",
                                     text= "Submit", bd=1)
        
        #handle events
