from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.char_one_image = PhotoImage(file="char_one.gif")
        self.char_two_image = PhotoImage(file="char_two.gif")
        self.char_three_image = PhotoImage(file="char_three.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.char_one_x_pos = 1
        self.char_one_y_pos = 1
        self.char_one_x_change = 1
    

        self.char_two_x_pos = 399
        self.char_two_y_pos = 150
        self.char_two_x_change = 1
        self.char_two_y_change = 1

        self.char_three_x_pos = 399
        self.char_three_y_pos = 300
        self.char_three_x_change = 1
        self.char_three_y_change = 1

        #add components
        self.add_char_one_image_label()
        self.add_char_two_image_label()
        self.add_char_three_image_label()

        #start the timer
        self.tick_one()
        self.tick_two()
        self.tick_three()

    #the timer tick_one function
    def tick_one(self):

        #if conditions for char_one
        if (self.char_one_x_pos >= (500 - 100)):
            self.char_one_x_change *= -1
        if (self.char_one_x_pos <= 0):
            self.char_one_x_change *= -1

        self.char_one_x_pos = self.char_one_x_pos + self.char_one_x_change
        self.char_one_image_label.place(x=self.char_one_x_pos,
                                        y=self.char_one_y_pos)
        self.after(1, self.tick_one)
            
        
    #the timer tick_two function
    def tick_two(self):
        #if conditions for char_one
        if (self.char_two_x_pos <= 0):
            self.char_two_x_change *= -1
        if (self.char_two_x_pos >= (500 - 100)):
            self.char_two_x_change *= -1
        
        self.char_two_x_pos = self.char_two_x_pos - self.char_two_x_change
        self.char_two_image_label.place(x=self.char_two_x_pos,
                                        y=self.char_two_y_pos)
        self.after(1, self.tick_two)

    #the timer tick_three function
    def tick_three(self):
        #if conditions for char_one
        if (self.char_three_x_pos <= 0):
            self.char_three_x_change *= -1
        if (self.char_three_x_pos >= (500 - 100)):
            self.char_three_x_change *= -1
        
        self.char_three_x_pos = self.char_three_x_pos - self.char_three_x_change
        self.char_three_image_label.place(x=self.char_three_x_pos,
                                        y=self.char_three_y_pos)
        self.after(1, self.tick_three)

    #char one
    def add_char_one_image_label(self):
        self.char_one_image_label = Label()
        self.char_one_image_label.place(x=self.char_one_x_pos,
                                        y=self.char_one_y_pos)
        self.char_one_image_label.configure(image=self.char_one_image)

    #char two
    def add_char_two_image_label(self):
        self.char_two_image_label = Label()
        self.char_two_image_label.place(x=self.char_two_x_pos,
                                        y=self.char_two_y_pos)
        self.char_two_image_label.configure(image=self.char_two_image)

    #char three
    def add_char_three_image_label(self):
        self.char_three_image_label = Label()
        self.char_three_image_label.place(x=self.char_three_x_pos,
                                        y=self.char_three_y_pos)
        self.char_three_image_label.configure(image=self.char_three_image)

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop()