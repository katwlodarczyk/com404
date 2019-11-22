from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Passport Checker")

        #add components
        self.__add_heading_label()
        self.__add_first_q_label()
        self.__add_first_q_yes_Checkbutton()
        self.__add_first_q_no_Checkbutton()
        self.__add_second_q_label()
        self.__add_second_q_yes_Checkbutton()
        self.__add_second_q_no_Checkbutton()
        self.__add_third_q_label()
        self.__add_third_q_yes_Checkbutton()
        self.__add_third_q_no_Checkbutton()
        self.__add_check_button()

    def __add_heading_label(self):
        #create
        self.heading_label= Label()
        self.heading_label.grid(row=0, columnspan=3)
        #style
        self.heading_label.configure( font="Roboto 24",
                                     text="Passport Checker",
                                     padx=50)
    def __add_first_q_label(self):
        #create
        self.first_q_label= Label()
        self.first_q_label.grid(row=1, column=0, sticky=W)
        #style
        self.first_q_label.configure( text=" 1.Photo matches face?",
                                  font="Roboto 16")
        #handle events

    def __add_first_q_yes_Checkbutton(self):
        #create
        self.first_q_yes_Checkbutton= Checkbutton()
        self.first_q_yes_Checkbutton.grid(row=2, column=1, sticky=W)
        #style
        self.first_q_yes_Checkbutton.configure( text="yes",
                                                font="Roboto 16")
        #handle events
    
    def __add_first_q_no_Checkbutton(self):
        #create
        self.first_q_no_Checkbutton= Checkbutton()
        self.first_q_no_Checkbutton.grid(row=2, column=2,sticky=E)
        #style
        self.first_q_no_Checkbutton.configure(text="no",
                                              font="Roboto 16")
        #handle events


    def __add_second_q_label(self):
        #create
        self.second_q_label= Label()
        self.second_q_label.grid(row=3, column=0, sticky=W)
        #style
        self.second_q_label.configure( text=" 2.Passport has at least 6 motnths validity?",
                                  font="Roboto 16")
        #handle events

    def __add_second_q_yes_Checkbutton(self):
        #create
        self.second_q_yes_Checkbutton= Checkbutton()
        self.second_q_yes_Checkbutton.grid(row=4, column=1, sticky=W)
        #style
        self.second_q_yes_Checkbutton.configure( text="yes",
                                                font="Roboto 16")
        #handle events

    def __add_second_q_no_Checkbutton(self):
         #create
        self.second_q_no_Checkbutton= Checkbutton()
        self.second_q_no_Checkbutton.grid(row=4, column=2,sticky=E)
        #style
        self.second_q_no_Checkbutton.configure(text="no",
                                              font="Roboto 16")
                         
        #handle events

    def __add_third_q_label(self):
        #create
        self.third_q_label= Label()
        self.third_q_label.grid(row=5, column=0, sticky=W)
        #style
        self.third_q_label.configure( text=" 3.Visa, if required, is valid?",
                                  font="Roboto 16")
        #handle events

    def __add_third_q_yes_Checkbutton(self):
        #create
        self.third_q_yes_Checkbutton= Checkbutton()
        self.third_q_yes_Checkbutton.grid(row=6, column=1, sticky=W)
        #style
        self.third_q_yes_Checkbutton.configure( text="yes",
                                                font="Roboto 16")
        #handle events

    def __add_third_q_no_Checkbutton(self):
        #create
        self.third_q_no_Checkbutton= Checkbutton()
        self.third_q_no_Checkbutton.grid(row=6, column=2, sticky=E)
        #style
        self.third_q_no_Checkbutton.configure( text="no",
                                                font="Roboto 16")
        #handle events

    def __add_check_button(self):
        #create
        self.check_button= Button()
        self.check_button.grid(row=7, columnspan=3)
        #style
        self.check_button.configure( font= "Roboto 20",
                                     bd= 2,
                                     relief= "solid",
                                     text="Check")
        #handle events
