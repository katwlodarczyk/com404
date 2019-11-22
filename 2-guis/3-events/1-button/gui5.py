from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
    def __add_heading_label(self):
        #create
        self.heading_label= Label()
        self.heading_label.grid(row=0, column=0)
        #style
        self.heading_label.configure( font="Roboto 24",
                                      text="Entrance Ticket",
                                      padx=50)
        #handle events
                                      
    def __add_instruction_label(self):
        #create
        self.instruction_label= Label()
        self.instruction_label.grid(row=1, column=0,sticky=W)
        #style
        self.instruction_label.configure(text="How many tickets are needed?",
                                         font="Roboto 20")
        #handle events
        
    def __add_tickets_entry(self):
        #create
        self.tickets_entry=Entry()
        self.tickets_entry.grid(row=2,column=0,sticky=N+E+S+W,pady=10)
        #style
        self.tickets_entry.configure(text="",
                                     font="Roboto 20")
        #handle event
        
    def __add_buy_button(self):
        #create
        self.buy_button=Button()
        self.buy_button.grid(row=3,column=0,pady=10)
        #style
        self.buy_button.configure(text="Buy",
                                      font="Roboto 20",
                                      padx=50,
                                      borderwidth=2,
                                      relief="solid")
        #handle events
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)

    def __buy_button_clicked(self,event):
        no_of_tickets = int(self.tickets_entry.get())
        if (no_of_tickets == 1):
            messagebox.showinfo("Purchased!", "You have purchased 1 ticket!")
        elif (no_of_tickets > 1):
            messagebox.showinfo("Purchased!", "You have purchased " + str(no_of_tickets) + " tickets!")
        else:
            messagebox.showinfo("Error", "You have entered an invalid number of tickets!")


