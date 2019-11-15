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
        self.__add_email_label()
        self.__add_user_entry()
        self.__add_submit_button()

    def __add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.place(x=0, y=0)
        #style
        self.heading_label.configure( text="Receive our newsletter",
                                      bg= "#000",
                                      font= "Roboto 32 underline",
                                      fg= "#fff",
                                      padx= 25
                                     )
        #handle events
    def __add_instruction_label(self):
        #create
        self.instruction_label= Label()
        self.instruction_label.place(x=0, y=100)
        #style
        self.instruction_label.configure( text= "Please enter your e-mail address to receive our newsletter",
                                          bg= "#000",
                                          font= "Roboto, 12",
                                          fg= "#fff",
                                          padx=40)
        #handle events

    def __add_email_label (self):
        #create
        self.email_label= Label()
        self.email_label.place(x=70, y= 150)
        #style
        self.email_label.configure( text= "E-mail:",
                                    bg= "#000",
                                    font= "Roboto 12",
                                    fg= "#fff",
                                    padx= 30)
        #handle events
        
    def __add_user_entry(self):
        #create
        self.user_entry= Entry()
        self.user_entry.place (x=170, y=150)
        #style
        self.user_entry.configure(font="Roboto 12",
                                 
                                  )
        #handle events

    def __add_submit_button(self):
        #create
        self.submit_button= Button()
        self.submit_button.place(x=190, y=200)
        #style
        self.submit_button.configure(font= "Roboto 12",
                                        text= "Submit")
                                       
        #handle events




        
