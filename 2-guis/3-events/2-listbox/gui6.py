from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Song maker")

        #add components
        self.__add_heading_label()
        self.__add_lyrics_to_add_label()
        self.__add_lyrics_frame()
        self.__add_lyrics_to_add_entry()
        self.__add_add_button()
        self.__add_lyrics_label()
        self.__add_lyrics_listbox()

    def __add_heading_label(self):
        #create
        self.heading_label= Label()
        self.heading_label.grid(row=0, columnspan=2)
        #style
        self.heading_label.configure( font="Roboto 24",
                                     text="Song Lyrics",
                                     padx=50)
        #handle events

    def __add_lyrics_to_add_label(self):
        #create
        self.lyrics_to_add_label= Label()
        self.lyrics_to_add_label.grid(row=1, column=0, sticky=W, pady=10)
        #style
        self.lyrics_to_add_label.configure(font="Roboto 20",
                                           text="Lyric to add:")
                                           
        #handle events

    def __add_lyrics_frame(self):
        #create
        self.lyrics_frame= Frame()
        self.lyrics_frame.grid(row=2,column=0, columnspan=2)
        #style
        #handle events

    def __add_lyrics_to_add_entry(self):
        #create
        self.lyrics_to_add_entry= Entry()
        self.lyrics_to_add_entry.grid(row=2, column=0, sticky=W,pady=12, padx=10 )
        #style
        self.lyrics_to_add_entry.configure(text="",
                                           font="Roboto 20",)
        #handle events

    def __add_add_button(self):
        #create
        self.add_button= Button()
        self.add_button.grid(row=2, column=1, sticky=E,pady=10)
        #style
        self.add_button.configure(font="Roboto 14",
                                  text="Add",
                                  borderwidth=2,
                                  relief="solid")
        #handle events
        self.add_button.bind("<ButtonRelease-1>", self.__add_button_clicked)

    def __add_button_clicked(self, event):
        added_lyrics= self.lyrics_to_add_entry.get()
        self.lyrics_listbox.insert(END, added_lyrics)
        

    def __add_lyrics_label(self):
        #create
        self.lyrics_label= Label()
        self.lyrics_label.grid(row=3, column=0,sticky=W)
        #style
        self.lyrics_label.configure( text="Lyrics",
                                     font="Roboto 20")
        #handle events

    def __add_lyrics_listbox(self):
        #create
        self.lyrics_listbox= Listbox()
        self.lyrics_listbox.grid(row=4, column=0)
        #style
        self.lyrics_listbox.configure(height= 10,
                                      font="Roboto 20")
                                      
        #handle events
