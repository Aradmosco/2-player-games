from tkinter import *
from PIL import Image, ImageTk
from tugofwarGUI import TugOfWarGUI
from pongGui import PongGame
from tictactoe import TicTacToeGame 

class GUI:
    def __init__(self):
        # Initialize the main window
        self.fenster = Tk()
        self.fenster.attributes("-fullscreen", True)  
        self.fenster.configure(bg="khaki")  

        # Get screen dimensions
        self.screen_width = self.fenster.winfo_screenwidth()
        self.screen_height = self.fenster.winfo_screenheight()
        self.font_title = int(self.screen_width // 9.72)  

        # Load and resize images
        self.photo_tictactoe = Image.open("tic-tac-toe.png").resize((int(self.screen_width / 4.5), int(self.screen_width / 4.5)))
        self.photo_pong = Image.open("pong.png").resize((int(self.screen_width / 4.5), int(self.screen_width / 4.5)))
        self.photo_tugofwar = Image.open("tug-of-war.png").resize((int(self.screen_width / 4.5), int(self.screen_width / 4.5)))

        self.photo_tictactoe2 = ImageTk.PhotoImage(self.photo_tictactoe)
        self.photo_pong2 = ImageTk.PhotoImage(self.photo_pong)
        self.photo_tugofwar2 = ImageTk.PhotoImage(self.photo_tugofwar)

        # Title Label
        self.Label_title_main = Label(text="2-Player Games", font=("Comic Sans MS", self.font_title), fg="green4", bg="khaki")
        self.Label_title_main.place(x=0, y=0)

        # Tic-Tac-Toe Button
        self.Label_tictactoe = Label(self.fenster, image=self.photo_tictactoe2)
        self.Label_tictactoe.place(x=(self.screen_width / 4.5) * (1 / 4), y=self.screen_height / 2.7)
        self.Label_tictactoe.bind("<Button-1>", self.start_tictactoe)  

        # Pong Button
        self.Label_pong = Label(self.fenster, image=self.photo_pong2)
        self.Label_pong.place(x=(self.screen_width / 4.5) * (1.75), y=self.screen_height / 2.7)
        self.Label_pong.bind("<Button-1>", self.start_pong)  

        # Tug-of-War Button
        self.Label_tugofwar = Label(self.fenster, image=self.photo_tugofwar2)
        self.Label_tugofwar.place(x=(self.screen_width / 4.5) * (3.25), y=self.screen_height / 2.7)
        self.Label_tugofwar.bind("<Button-1>", self.start_tugofwar)  

        self.fenster.mainloop()  

    # Functions to start games
    def start_tictactoe(self, event=None):
        TicTacToeGame(self.fenster)  # Run Tic-Tac-Toe

    def start_pong(self, event=None):
        PongGame(self.fenster)  # Run Pong

    def start_tugofwar(self, event=None):
        TugOfWarGUI(self.fenster)  # Run Tug-of-War

if __name__ == "__main__":
    GUI()


    
