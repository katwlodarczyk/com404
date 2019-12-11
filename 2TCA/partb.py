from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        # load resources
        self.red_image = PhotoImage(file="red.gif")
        self.green_image = PhotoImage(file="green.gif")
        self.grey_image = PhotoImage(file="grey.gif")

        #options menu
        self.options= StringVar()
        self.options.set("Weekly")

        #set window attributes
        self.title("Newsletter")
        self.configure( bg= "#eee",
                        padx= 10,
                        pady= 10)

        #add components
        self.__add_heading_label()
        self.__add_instructional_label()
        self.__add_email_frame()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_image_label()
        self.__add_type_frame()
        self.__add_type_label()
        self.__add_type_optionmenu()
        self.__add_subscribe_button()
        

    def __add_heading_label(self):
        #create
        self.heading_label= Label()
        self.heading_label.grid(row=0, columnspan=3, sticky=N+E+S+W)
        #style
        self.heading_label.configure( font="Arial 14",
                                     text="RECEIVE OUR NEWSLETTER",
                                     pady=10)
    def __add_instructional_label(self):
        #create
        self.instructional_label= Label()
        self.instructional_label.grid(row=1, columnspan=3, sticky=N+E+S+W)
        #style
        self.instructional_label.configure(text="Please enter you email below to receive our newsletter.",
                                           padx=10,
                                           pady=10,
                                           justify= "left")
        
        #handle events

    def __add_email_frame(self):
        self.email_frame= Frame()
        self.email_frame.grid(row=2,columnspan=3, sticky= N+W+S+E)

    def __add_email_label(self):
        #create
        self.email_label= Label(self.email_frame)
        self.email_label.grid(row=2, column=0, padx=10, sticky=W)
        #style
        self.email_label.configure(text="Email:", padx=10)
        #handle events

    def __add_email_entry(self):
        #create
        self.email_entry= Entry(self.email_frame)
        self.email_entry.grid(row=2, column=1, sticky=E, pady=10)
        #style
        self.email_entry.configure(bd=2, fg="#f00", width= 30)
        #handle events
        self.email_entry.bind("<KeyRelease>", self.image_change)

    def image_change(self,event):
        email= self.email_entry.get()
        if len(email) == 0:
            self.image_label.configure(image=self.red_image)
        else:
            self.image_label.configure(image=self.green_image)

    def __add_image_label(self):
        #create
        self.image_label= Label(self.email_frame)
        self.image_label.grid(row=2, column=2, padx=10)
        #style
        self.image_label.configure(image=self.grey_image, height=20, width=20, )
        #handle events
        
    def __add_type_frame(self):
        self.type_frame= Frame()
        self.type_frame.grid(row=3, columnspan=3,sticky=W+E+S+N)

    def __add_type_label(self):
        self.type_label= Label(self.type_frame)
        self.type_label.grid(row=3, column=1)
        self.type_label.configure(text="Type", padx=10, pady=10)
    
    def __add_type_optionmenu(self):
        self.type_optionmenu= OptionMenu(self.type_frame, self.options, "Weekly", "Monthly", "Yearly")
        self.type_optionmenu.grid(row=3, column=2, padx=10)
        
    def __add_subscribe_button(self):
        #create
        self.subscribe_button=Button()
        self.subscribe_button.grid(row=4, columnspan=3, sticky=W+E+S+N)
        #style
        self.subscribe_button.configure(text="Subscribe", bg="#fee")
        #handle events
        self.subscribe_button.bind("<ButtonRelease-1>", self.subscribe_button_clicked)

    def subscribe_button_clicked(self, event):
        if len(self.email_entry.get()) >= 1:
            if (self.options.get() == "Weekly"):
                messagebox.showinfo("Newsletter", "You have subscribed to the weekly newsletter!")
            elif(self.options.get() == "Monthly"):
                messagebox.showinfo("Newletter", "You have subscribed to the monthly newsletter! You will receive this on the first day of each month.")
            elif(self.options.get() == "Yearly"):
                messagebox.showinfo("Newletter", "You have subscribed to the yearly newsletter! You will receive this at the start of each year.")
            else:
                messagebox.showinfo("Newletter", "Error, please try again.")
        else:
            messagebox.showinfo("Newletter", "Please enter your email!")   
            
    

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
