from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_image = PhotoImage(file="ball.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500,
                       bg="#73b504")

        # set animation attributes
        self.ball_x_pos = 240
        self.ball_y_pos = 0
        self.ball_x_change = 1
        self.ball_y_change = 1
        
        # add components
        self.add_ball_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        if (self.ball_x_pos >= (500 - 10)):
            self.ball_x_change *= -1

        if (self.ball_y_pos >= (500 - 10)):
            self.ball_y_change *= -1

        if (self.ball_x_pos <= 0):
            self.ball_x_change *= -1

        if (self.ball_y_pos <= 0):
            self.ball_y_change = 1


        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        self.after(1, self.tick)
        

    # the ball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop()