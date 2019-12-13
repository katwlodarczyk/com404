from tkinter import *
import time
from tkinter import messagebox
import sys

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.pikachu_image = PhotoImage(file="/Users/seanypollard/Documents/Uni/Programming/com404/02-guis/05-animation/04-with-events/img/pikachu.gif")
        self.poke_ball_image = PhotoImage(file="/Users/seanypollard/Documents/Uni/Programming/com404/02-guis/05-animation/04-with-events/img/PokeBall.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.pikachu_x_pos = 400
        self.pikachu_y_pos = 200

        self.poke_ball_x_pos = 0
        self.poke_ball_y_pos = 170
        self.poke_ball_x_change = 1
        self.poke_ball_y_change = 1

        self.num_ticks = 0

        # add components
        self.add_pikachu_image_label()
        self.add_poke_ball_image_label()
        self.add_change_button()
 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        self.poke_ball_x_pos += self.poke_ball_x_change
        self.poke_ball_y_pos += self.poke_ball_y_change
        self.poke_ball_image_label.place(x=self.poke_ball_x_pos, 
                                        y=self.poke_ball_y_pos)

        self.num_ticks += 1

        if self.poke_ball_x_pos >= 400:
            if self.poke_ball_y_pos >=150 and self.poke_ball_y_pos <= 300:
                messagebox.showinfo("Congrats!", "You caught Pikachu!")
                sys.exit()
        if self.num_ticks == 500:
            messagebox.showwarning("Oh no!","You did not catch Pickachu!")
            sys.exit()
        
        self.after(10, self.tick)

    # the components
    def add_poke_ball_image_label(self):
        self.poke_ball_image_label = Label()
        self.poke_ball_image_label.place(x=self.poke_ball_x_pos,
                                            y=self.poke_ball_y_pos)
        self.poke_ball_image_label.configure(image=self.poke_ball_image)

    def add_pikachu_image_label(self):
        self.pikachu_image_label = Label()
        self.pikachu_image_label.place(x=self.pikachu_x_pos,
                                            y=self.pikachu_y_pos)
        self.pikachu_image_label.configure(image=self.pikachu_image)

    def add_change_button(self):
        self.change_button = Button()
        self.change_button.place(x=225,
                                    y=450)
        self.change_button.configure(text="Up / Down")
        self.change_button.bind("<ButtonRelease-1>", self.__change_button_clicked)

    def __change_button_clicked(self, event):
        self.poke_ball_y_change *= -1

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 
