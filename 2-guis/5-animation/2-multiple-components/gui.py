from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.red_ball_image = PhotoImage(file="red_ball.gif")
        self.blue_ball_image = PhotoImage(file="blue_ball.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.red_ball_x_pos = 225
        self.red_ball_y_pos = 1
        self.red_ball_x_change = 1
        self.red_ball_y_change = 1

        self.blue_ball_x_pos = 120
        self.blue_ball_y_pos = 1
        self.blue_ball_x_change = 1
        self.blue_ball_y_change = 1

        #add components
        self.add_red_ball_image_label()
        self.add_blue_ball_image_label()

        #start the timer
        self.tick()

    #the timer tick function
    def tick(self):

        #if conditions for red ball
        if (self.red_ball_x_pos <= 0):
            self.red_ball_x_change *= -1

        if (self.red_ball_y_pos >= (500 - 50)):
            self.red_ball_y_change *= -1

        if (self.red_ball_x_pos >= (500 - 50)):
            self.red_ball_x_change *= -1

        if (self.red_ball_y_pos <= 0):
            self.red_ball_y_change *= -1

        #if conditions for blue ball
        if (self.blue_ball_x_pos >= (500 - 50)):
            self.blue_ball_x_change *= -1

        if (self.blue_ball_y_pos >= (500 - 50)):
            self.blue_ball_y_change *= -1

        if (self.blue_ball_x_pos <= 0):
            self.blue_ball_x_change *= -1

        if (self.blue_ball_y_pos <= 0):
            self.blue_ball_y_change = 1

        #for red ball
        self.red_ball_x_pos = self.red_ball_x_pos - self.red_ball_x_change
        self.red_ball_y_pos = self.red_ball_y_pos + self.red_ball_y_change
        self.red_ball_image_label.place(x=self.red_ball_x_pos,
                                        y=self.red_ball_y_pos)

        #for blue ball
        self.blue_ball_x_pos = self.blue_ball_x_pos + self.blue_ball_x_change
        self.blue_ball_y_pos = self.blue_ball_y_pos + self.blue_ball_y_change
        self.blue_ball_image_label.place(x=self.blue_ball_x_pos,
                                         y=self.blue_ball_y_pos)
        
        self.after(2, self.tick)

    #the red ball
    def add_red_ball_image_label(self):
        self.red_ball_image_label = Label()
        self.red_ball_image_label.place(x=self.red_ball_x_pos,
                                        y=self.red_ball_y_pos)
        self.red_ball_image_label.configure(image=self.red_ball_image)

    #the blue ball
    def add_blue_ball_image_label(self):
        self.blue_ball_image_label = Label()
        self.blue_ball_image_label.place(x=self.blue_ball_x_pos,
                                        y=self.blue_ball_y_pos)
        self.blue_ball_image_label.configure(image=self.blue_ball_image)

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop()