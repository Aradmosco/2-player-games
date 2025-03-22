from tkinter import *
from PIL import Image, ImageTk

class TicTacToeGame:
    def __init__(self, main_app):
        self.main_app = main_app
        self.tictactoe = Toplevel(main_app.fenstermain)  
        self.tictactoe.attributes("-fullscreen", True)  
        self.tictactoe.configure(bg="khaki")  

        self.screen_width = self.tictactoe.winfo_screenwidth()
        self.screen_height = self.tictactoe.winfo_screenheight()
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        self.dranncounter = 0  
        self.dranncounter = 0  # Zählt, wer am Zug ist (0 für Spieler 1, 1 für Spieler 2)
        self.schongewesen1 = 0  # Überprüft, ob ein Feld bereits besetzt wurde
        self.schongewesen2 = 0
        self.schongewesen3 = 0
        self.schongewesen4 = 0
        self.schongewesen5 = 0 
        self.schongewesen6 = 0
        self.schongewesen7 = 0
        self.schongewesen8 = 0
        self.schongewesen9 = 0  

        # Load and resize images
        self.photo_tictactoefeld = Image.open("feld.png")
        self.new_photofeld = self.photo_tictactoefeld.resize((int(self.screen_width / 2), int(self.screen_width / 2)))
        self.photo_feld2 = ImageTk.PhotoImage(self.new_photofeld)
        self.photo_circle = Image.open("o.png")
        self.new_circle = self.photo_circle.resize((int(self.screen_width / 6.5), int(self.screen_width / 6.5)))
        self.photo_circle2 = ImageTk.PhotoImage(self.new_circle)
        self.photo_cross = Image.open("x.png")
        self.new_cross = self.photo_cross.resize((int(self.screen_width / 6.5), int(self.screen_width / 6.5)))
        self.photo_cross2 = ImageTk.PhotoImage(self.new_cross)

        # Fügt das Tic-Tac-Toe Spielfeld und die Bilder für die "O"- und "X"-Symbole hinzu
        self.Label_tictactoefeld = Label(self.tictactoe, image=self.photo_feld2)
        self.Label_tictactoefeld.place(x=(self.screen_width / 2 - self.screen_width / 4), y=(self.screen_height - (self.screen_width / 2)) / 2)
        self.Label_tictactoefeld.bind("<Button-1>", self.place)  # Verknüpft das Spielfeld mit der Platzierungsfunktion

        # Create label lists for O and X
        self.Label_o1 = Label(self.tictactoe, image=self.photo_circle2)
        self.Label_x1 = Label(self.tictactoe, image=self.photo_cross2)
        self.Label_o2 = Label(self.tictactoe, image=self.photo_circle2)
        self.Label_x2 = Label(self.tictactoe, image=self.photo_cross2)
        self.Label_o3 = Label(self.tictactoe, image=self.photo_circle2)
        self.Label_x3 = Label(self.tictactoe, image=self.photo_cross2)
        self.Label_o4 = Label(self.tictactoe, image=self.photo_circle2)
        self.Label_x4 = Label(self.tictactoe, image=self.photo_cross2)
        self.Label_o5 = Label(self.tictactoe, image=self.photo_circle2)
        self.Label_x5 = Label(self.tictactoe, image=self.photo_cross2)
        self.Label_o6 = Label(self.tictactoe, image=self.photo_circle2)
        self.Label_x6 = Label(self.tictactoe, image=self.photo_cross2)
        self.Label_o7 = Label(self.tictactoe, image=self.photo_circle2)
        self.Label_x7 = Label(self.tictactoe, image=self.photo_cross2)
        self.Label_o8 = Label(self.tictactoe, image=self.photo_circle2)
        self.Label_x8 = Label(self.tictactoe, image=self.photo_cross2)
        self.Label_o9 = Label(self.tictactoe, image=self.photo_circle2)
        self.Label_x9 = Label(self.tictactoe, image=self.photo_cross2)

        self.tictactoe.mainloop()

    def place(self, event=None):
        self.xkor = event.x
        self.ykor = event.y
        
        if self.xkor < self.screen_width /6 and self.ykor < self.screen_height/3:
            if self.schongewesen1 == 0:
                if self.dranncounter%2 == 0:
                    self.Label_o1.place(x=(self.screen_width /2 -self.screen_width /4.2), y=(self.screen_height-(self.screen_width /2)) /1.5)
                    self.board[0] = "O" 
                else:
                    self.Label_x1.place(x=(self.screen_width /2 -self.screen_width /4.2), y=(self.screen_height-(self.screen_width /2)) /1.5)
                    self.board[0] = "X"  
                self.dranncounter += 1
                self.schongewesen1 +=1
        elif self.xkor < self.screen_width /6 and self.ykor > self.screen_height/3 and self.ykor < self.screen_height/1.6666:
            if self.schongewesen2 == 0:
                if self.dranncounter%2 == 0:
                    self.Label_o2.place(x=(self.screen_width /2 -self.screen_width /4.2), y=(self.screen_height-(self.screen_width /2)) /0.31)
                    self.board[1] = "O"
                else:
                    self.Label_x2.place(x=(self.screen_width /2 -self.screen_width /4.2), y=(self.screen_height-(self.screen_width /2)) /0.31)
                    self.board[1] = "X"
                self.dranncounter += 1
                self.schongewesen2 +=1
        elif self.xkor < self.screen_width /6 and self.ykor > self.screen_height/1.6666:
            if self.schongewesen3 == 0:
                if self.dranncounter%2 == 0:
                    self.Label_o3.place(x=(self.screen_width /2 -self.screen_width /4.2), y=(self.screen_height-(self.screen_width /2)) /0.175)
                    self.board[2] = "O"
                else:
                    self.Label_x3.place(x=(self.screen_width /2 -self.screen_width /4.2), y=(self.screen_height-(self.screen_width /2)) /0.175)
                    self.board[2] = "X"
                self.dranncounter += 1
                self.schongewesen3 +=1
        elif self.xkor < self.screen_width /3 and self.ykor < self.screen_height/3:
            if self.schongewesen4 == 0:
                if self.dranncounter%2 == 0:
                    self.Label_o4.place(x=(self.screen_width /2 -self.screen_width /12.5), y=(self.screen_height-(self.screen_width /2)) /1.5)
                    self.board[3] = "O"
                else:
                    self.Label_x4.place(x=(self.screen_width /2 -self.screen_width /12.5), y=(self.screen_height-(self.screen_width /2)) /1.5)
                    self.board[3] = "X"
                self.dranncounter += 1
                self.schongewesen4 +=1
        elif self.xkor < self.screen_width /3 and self.ykor > self.screen_height/3 and self.ykor < self.screen_height/1.6666:
            if self.schongewesen5 == 0:
                if self.dranncounter%2 == 0:
                    self.Label_o5.place(x=(self.screen_width /2 -self.screen_width /12.5), y=(self.screen_height-(self.screen_width /2)) /0.31)
                    self.board[4] = "O"
                else:
                    self.Label_x5.place(x=(self.screen_width /2 -self.screen_width /12.5), y=(self.screen_height-(self.screen_width /2)) /0.31)
                    self.board[4] = "X"
                self.dranncounter += 1
                self.schongewesen5 +=1
        elif self.xkor < self.screen_width /3 and self.ykor > self.screen_height/1.6666:
            if self.schongewesen6 == 0:
                if self.dranncounter%2 == 0:
                    self.Label_o6.place(x=(self.screen_width /2 -self.screen_width /12.5), y=(self.screen_height-(self.screen_width /2)) /0.175)
                    self.board[5] = "O"
                else:
                    self.Label_x6.place(x=(self.screen_width /2 -self.screen_width /12.5), y=(self.screen_height-(self.screen_width /2)) /0.175)
                    self.board[5] = "X"
                self.dranncounter += 1
                self.schongewesen6 +=1
        elif self.xkor > self.screen_width /3 and self.ykor < self.screen_height/3:
            if self.schongewesen7 == 0:
                if self.dranncounter%2 == 0:
                    self.Label_o7.place(x=(self.screen_width /2 +self.screen_width /12.5), y=(self.screen_height-(self.screen_width /2)) /1.5)
                    self.board[6] = "O"
                else:
                    self.Label_x7.place(x=(self.screen_width /2 +self.screen_width /12.5), y=(self.screen_height-(self.screen_width /2)) /1.5)
                    self.board[6] = "X"
                self.dranncounter += 1
                self.schongewesen7 +=1
        elif self.xkor > self.screen_width /3 and self.ykor > self.screen_height/3 and self.ykor < self.screen_height/1.6666:
            if self.schongewesen8 == 0:
                if self.dranncounter%2 == 0:
                    self.Label_o8.place(x=(self.screen_width /2 +self.screen_width /12.5), y=(self.screen_height-(self.screen_width /2)) /0.31)
                    self.board[7] = "O"
                else:
                    self.Label_x8.place(x=(self.screen_width /2 +self.screen_width /12.5), y=(self.screen_height-(self.screen_width /2)) /0.31)
                    self.board[7] = "X"
                self.dranncounter += 1
                self.schongewesen8 +=1
        elif self.xkor > self.screen_width /3 and self.ykor > self.screen_height/1.6666:
            if self.schongewesen9 == 0:
                if self.dranncounter%2 == 0:
                    self.Label_o9.place(x=(self.screen_width /2 +self.screen_width /12.5), y=(self.screen_height-(self.screen_width /2)) /0.175)
                    self.board[8] = "O"
                else:
                    self.Label_x9.place(x=(self.screen_width /2 +self.screen_width /12.5), y=(self.screen_height-(self.screen_width /2)) /0.175)
                    self.board[8] = "X"
                self.dranncounter += 1
                self.schongewesen9 +=1
        print(self.board)
        self.check_winner()
        self.check_draw()

        

    def check_winner(self):
        for symbol, color in [("O", "blau"), ("X", "rot")]:  # Assign "O" to "blau" and "X" to "rot"
            if self.board[0] == symbol and self.board[1] == symbol and self.board[2] == symbol:  
                self.gewonnen(color)  
            elif self.board[3] == symbol and self.board[4] == symbol and self.board[5] == symbol:  
                self.gewonnen(color)  
            elif self.board[6] == symbol and self.board[7] == symbol and self.board[8] == symbol:  
                self.gewonnen(color)  
            elif self.board[0] == symbol and self.board[3] == symbol and self.board[6] == symbol:  
                self.gewonnen(color)  
            elif self.board[1] == symbol and self.board[4] == symbol and self.board[7] == symbol:  
                self.gewonnen(color)  
            elif self.board[2] == symbol and self.board[5] == symbol and self.board[8] == symbol:  
                self.gewonnen(color)  
            elif self.board[0] == symbol and self.board[4] == symbol and self.board[8] == symbol:  
                self.gewonnen(color)  
            elif self.board[2] == symbol and self.board[4] == symbol and self.board[6] == symbol:  
                self.gewonnen(color)

    def check_draw(self):
        if 0 not in self.board:  
            winner_window = Toplevel(self.tictactoe)
            winner_window.attributes("-fullscreen", True)
            winner_window.configure(bg="khaki")
            winner_message = f"Niemand gewinnt, gleichstand"
            Label(winner_window, text=winner_message, font=("Comic Sans MS", 100), fg="green4", bg="khaki").pack(pady=50)
            Button(winner_window, text="Return to Main Screen", font=("Comic Sans MS", 30),fg="green4", bg="khaki", command=lambda: self.return_to_main(winner_window)).pack(pady=20)

    def gewonnen(self, gewinner):
        if gewinner == "blau":
            self.main_app.score_blue += 1  # Update blue score in main
        else:
            self.main_app.score_red += 1  # Update red score in main    

        # Update the label in the main screen
        self.main_app.score_label.config(text=f"Blau: {self.main_app.score_blue} | Rot: {self.main_app.score_red}")
        
        
        winner_window = Toplevel(self.tictactoe)  # Erstellt ein neues Fenster für den Gewinner
        winner_window.attributes("-fullscreen", True)
        winner_window.configure(bg="khaki")
        winner_message = f"{gewinner} gewinnt!"  # Zeigt den Gewinner an
        Label(winner_window, text=winner_message, font=("Comic Sans MS", 100), fg="green4", bg="khaki").pack(pady=50)
        Button(winner_window, text="Return to Main Screen", font=("Comic Sans MS", 30), fg="green4", bg="khaki", command=lambda: self.return_to_main(winner_window)).pack(pady=20)

    def return_to_main(self, winner_window):
        winner_window.destroy()
        self.tictactoe.destroy()



if __name__ == "__main__":
    TicTacToeGame()
