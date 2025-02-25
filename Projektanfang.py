from tkinter import *
import random
from PIL import Image, ImageTk 


class GUI():
    def __init__(self):
        self.fenster = Tk()
        self.fenster.attributes("-fullscreen", True)  
        self.fenster.configure(bg="khaki")
        self.dranncounter = 0
        self.schongewesen1 = 0
        self.schongewesen2 = 0
        self.schongewesen3 = 0
        self.schongewesen4 = 0
        self.schongewesen5 = 0
        self.schongewesen6 = 0
        self.schongewesen7 = 0
        self.schongewesen8 = 0
        self.schongewesen9 = 0


        self.screen_width = self.fenster.winfo_screenwidth()
        self.screen_height = self.fenster.winfo_screenheight()
        self.font_title = int(self.screen_width//9.72)
        
        self.photo_tictactoe = Image.open("tic-tac-toe.png")
        self.new_photo1 = self.photo_tictactoe.resize((int(self.screen_width / 4.5), int(self.screen_width / 4.5)))
        self.photo_tictactoe2 = ImageTk.PhotoImage(self.new_photo1)

        self.photo_pong = Image.open("pong.png")
        self.new_photo2 = self.photo_pong.resize((int(self.screen_width / 4.5), int(self.screen_width / 4.5)))
        self.photo_pong2 = ImageTk.PhotoImage(self.new_photo2)

        self.photo_tugofwar = Image.open("tug-of-war.png")
        self.new_photo3 = self.photo_tugofwar.resize((int(self.screen_width / 4.5), int(self.screen_width / 4.5)))
        self.photo_tugofwar2 = ImageTk.PhotoImage(self.new_photo3)

        self.Label_title_main = Label(text="2-Player Games", font=("Comic Sans MS",self.font_title), fg= "green4", bg="khaki")
        self.Label_title_main.place(x=0, y=0)

        self.Label_tictactoe = Label(self.fenster, image=self.photo_tictactoe2)
        self.Label_tictactoe.place(x=(self.screen_width/4.5)*(1/4), y=self.screen_height/2.7)
        self.Label_tictactoe.bind("<Button-1>", self.start_tictactoe)

        self.Label_pong = Label(self.fenster, image=self.photo_pong2)
        self.Label_pong.place(x=(self.screen_width/4.5)*(1.75), y=self.screen_height/2.7)
        self.Label_pong.bind("<Button-1>", self.start_pong)

        self.Label_tugofwar = Label(self.fenster, image=self.photo_tugofwar2)
        self.Label_tugofwar.place(x=(self.screen_width/4.5)*(3.25), y=self.screen_height/2.7)
        self.Label_tugofwar.bind("<Button-1>", self.start_tugofwar)


        self.fenster.mainloop()

    def start_tictactoe(self, event=None):
        self.fenster.destroy()
        self.tictactoe = Tk()
        self.tictactoe.attributes("-fullscreen", True)  
        self.tictactoe.configure(bg="khaki")
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        self.photo_tictactoefeld = Image.open("feld.png")
        self.new_photofeld = self.photo_tictactoefeld.resize((int(self.screen_width /2), int(self.screen_width/2)))
        self.photo_feld2 = ImageTk.PhotoImage(self.new_photofeld)
        self.photo_circle = Image.open("o.png")
        self.new_circle = self.photo_circle.resize((int(self.screen_width /6.5), int(self.screen_width/6.5)))
        self.photo_circle2 = ImageTk.PhotoImage(self.new_circle)
        self.photo_cross = Image.open("x.png")
        self.new_cross = self.photo_cross.resize((int(self.screen_width /6.5), int(self.screen_width/6.5)))
        self.photo_cross2 = ImageTk.PhotoImage(self.new_cross)


        self.Label_tictactoefeld = Label(self.tictactoe, image=self.photo_feld2)
        self.Label_tictactoefeld.place(x=(self.screen_width /2 -self.screen_width /4), y=(self.screen_height-(self.screen_width /2)) /2)
        self.Label_tictactoefeld.bind("<Button-1>", self.place)
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

    def start_pong(self, event=None):
        self.fenster.destroy()
        self.pong = Tk()
        self.pong.attributes("-fullscreen", True)  
        self.pong.configure(bg="khaki")

    def start_tugofwar(self, event=None):
        self.fenster.destroy()
        self.tugofwar = Tk()
        self.tugofwar.attributes("-fullscreen", True)  
        self.tugofwar.configure(bg="khaki")

    def gewonnen(self, gewinner):
        winner_window = Toplevel(self.tictactoe)
        winner_window.attributes("-fullscreen", True)
        winner_window.configure(bg="khaki")
        
        # Define message based on winner
        winner_message = f"{gewinner} wins!"

        # Display winner message
        Label(winner_window, text=winner_message, font=("Comic Sans MS", 100), fg="green4", bg="khaki").pack(pady=50)
        Button(winner_window, text="Return to Main Screen", font=("Comic Sans MS", 30),fg="green4", bg="khaki", command=lambda: self.return_to_main(winner_window)).pack(pady=20)
    
    def return_to_main(self, winner_window):
        winner_window.destroy() 
        self.tictactoe.destroy()
        GUI()         
        
        
    
    

    def check_winner(self):
        for symbol in ["X", "O"]:
            if self.board[0] == symbol and self.board[1] == symbol and self.board[2] == symbol:  
                self.gewonnen(symbol)  
            elif self.board[3] == symbol and self.board[4] == symbol and self.board[5] == symbol:  
                self.gewonnen(symbol)  
            elif self.board[6] == symbol and self.board[7] == symbol and self.board[8] == symbol:  
                self.gewonnen(symbol)  
            elif self.board[0] == symbol and self.board[3] == symbol and self.board[6] == symbol:  
                self.gewonnen(symbol)  
            elif self.board[1] == symbol and self.board[4] == symbol and self.board[7] == symbol:  
                self.gewonnen(symbol)  
            elif self.board[2] == symbol and self.board[5] == symbol and self.board[8] == symbol:  
                self.gewonnen(symbol)  
            elif self.board[0] == symbol and self.board[4] == symbol and self.board[8] == symbol:  
                self.gewonnen(symbol)  
            elif self.board[2] == symbol and self.board[4] == symbol and self.board[6] == symbol:  
                self.gewonnen(symbol)  
        

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

if __name__ == "__main__":
    GUI()
    
