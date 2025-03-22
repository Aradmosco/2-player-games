from tkinter import *
from PIL import Image, ImageTk
from tugofwarGUI import TugOfWarGUI
from pongGui import PongGame
from tictactoe import TicTacToeGame 

class GUI:
    def __init__(self):
        # Initialize the main window
        self.fenstermain = Tk()
        self.fenstermain.attributes("-fullscreen", True)  
        self.fenstermain.configure(bg="khaki")  

        self.score_blue = 0  # Track blue player wins
        self.score_red = 0   # Track red player wins

        # Get screen dimensions
        self.screen_width = self.fenstermain.winfo_screenwidth()
        self.screen_height = self.fenstermain.winfo_screenheight()
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

        self.score_label = Label(self.fenstermain, text=f"Blau: {self.score_blue} | Rot: {self.score_red}", font=("Comic Sans MS", 30), fg="green", bg="khaki")
        self.score_label.place(x=self.screen_width // 2 - 100, y=self.screen_height - 100)  # Centered at the bottom

        
        # Tic-Tac-Toe Button
        self.Label_tictactoe = Label(self.fenstermain, image=self.photo_tictactoe2)
        self.Label_tictactoe.place(x=(self.screen_width / 4.5) * (1 / 4), y=self.screen_height / 2.7)
        self.Label_tictactoe.bind("<Button-1>", self.start_tictactoe)  

        # Pong Button
        self.Label_pong = Label(self.fenstermain, image=self.photo_pong2)
        self.Label_pong.place(x=(self.screen_width / 4.5) * (1.75), y=self.screen_height / 2.7)
        self.Label_pong.bind("<Button-1>", self.start_pong)  

        # Tug-of-War Button
        self.Label_tugofwar = Label(self.fenstermain, image=self.photo_tugofwar2)
        self.Label_tugofwar.place(x=(self.screen_width / 4.5) * (3.25), y=self.screen_height / 2.7)
        self.Label_tugofwar.bind("<Button-1>", self.start_tugofwar)  

        self.fenstermain.mainloop()  

    # Functions to start games
    def start_tictactoe(self, event=None):
        self.tictactoe_game = TicTacToeGame(self)  # Run Tic-Tac-Toe

    def start_pong(self, event=None):
        self.pong_game = PongGame(self)  # Run Pong

    def start_tugofwar(self, event=None):
        self.tugofwar_game = TugOfWarGUI(self)  # Run Tug-of-War

if __name__ == "__main__":
    GUI()

    
