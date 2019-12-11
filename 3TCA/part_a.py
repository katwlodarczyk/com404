from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        # load resources
        self.tick_image = PhotoImage(file="green.gif")
        self.cross_image = PhotoImage(file="red.gif")

        
        #set window attributes
        self.title("Currency Converter")
        self.configure( bg= "#ffe8e8",
                        padx= 10,
                        pady= 10)

        #add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_amount_label()
        self.__add_amount_frame()
        self.__add_amount_entry()
        self.__add_amount_image()
        self.__add_buttons_frame()
        self.__add_clear_button()
        self.__add_convert_button()
        self.__add_message_frame()
        self.__add_system_messages()
        

    def __add_outer_frame(self):
        self.outer_frame=Frame()
        self.outer_frame.grid(row=0, columnspan=4)
        self.outer_frame.configure(bg="#ffe8e8")
        
    def __add_heading_label(self):
        self.heading_label=Label(self.outer_frame)
        self.heading_label.grid(row=0, columnspan=4)
        self.heading_label.configure(text="Currency Converter", font="Roboto 20", bg="#ffe8e8")

    def __add_amount_label(self):
        self.amount_label= Label(self.outer_frame)
        self.amount_label.grid(row=1, column=0,sticky=W)
        self.amount_label.configure(text="Amount", font="Roboto 14", bg="#ffe8e8")

    def __add_amount_frame(self):
        self.amount_frame= Frame(self.outer_frame)
        self.amount_frame.grid(row=2,columnspan=4,sticky=W+E+S+N)
        self.amount_frame.configure(bg="#ffe8e8")

    def __add_amount_entry(self):
        self.amount_entry=Entry(self.amount_frame)
        self.amount_entry.grid(row=2,columnspan=3,sticky=W+E+S+N)
        self.amount_entry.configure()
        self.amount_entry.bind("<KeyRelease>", self.amount_entry_typed)

    def amount_entry_typed(self, event):
        if len(self.amount_entry.get()) >=1:
            self.amount_image.configure(image=self.tick_image)
        else:
            self.amount_image.configure(image=self.cross_image)

    def __add_amount_image(self):
        self.amount_image= Label(self.amount_frame)
        self.amount_image.grid(row=2, column=4, padx=10)
        self.amount_image.configure(image=self.cross_image, width=20, height=20)

    def __add_buttons_frame(self):
        self.buttons_frame=Frame(self.outer_frame)
        self.buttons_frame.grid(row=3, columnspan=2 , pady=10, padx=40, sticky= W+E+S+N)
        self.buttons_frame.configure(bg="#ffe8e8")

    def __add_clear_button(self):
        self.clear_button=Button(self.buttons_frame)
        self.clear_button.grid(row=3,column=1, padx=20,sticky=W)
        self.clear_button.configure(text="Clear", font="Roboto 14", padx=5)
        self.clear_button.bind("<ButtonRelease-1>", self.clear_button_clicked)

    def clear_button_clicked(self,event):
        self.system_messages.configure(text="System Message Displayed Here", padx=1)

    def __add_convert_button(self):
        self.convert_button=Button(self.buttons_frame)
        self.convert_button.grid(row=3,column=2, sticky=E)
        self.convert_button.configure(text="Convert", font="Roboto 14", padx=5)
        self.convert_button.bind("<ButtonRelease-1>", self.convert_button_clicked)

    def convert_button_clicked(self,event):
        self.system_messages.configure(text="Converting...", bg="#fffbce", padx=55)
        euro_conversion = int(self.amount_entry.get()) * 1.15
        messagebox.showinfo("Currency Converter", "£"+str(self.amount_entry.get())+ " is " +str(euro_conversion) + " euros with a conversion rate of 1.15.")
        

    def __add_message_frame(self):
        self.message_frame=Frame(self.outer_frame)
        self.message_frame.grid(row=4, columnspan=4, sticky=W+E+S+N)
        self.message_frame.configure(
                                     bg="#fffbce",
                                     highlightthickness = 1,
                                     highlightbackground = "black",
                                     highlightcolor = "black")

    def __add_system_messages(self):
        self.system_messages= Label(self.message_frame)
        self.system_messages.grid(row=4,columnspan=4, sticky=W+E+S+N, padx=30)
        self.system_messages.configure(text="System Message Displayed Here",
                                       bg="#fffbce",
                                       font="Roboto 14")
    
    

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
