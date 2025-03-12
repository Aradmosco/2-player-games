from tkinter import *
from PIL import Image, ImageTk

class TugOfWarGUI:
    def __init__(self):
        self.tugofwarfenster = Tk()
        self.tugofwarfenster.attributes("-fullscreen", True)
        self.tugofwarfenster.configure(bg="khaki")
        self.screen_width = self.tugofwarfenster.winfo_screenwidth()
        self.screen_height = self.tugofwarfenster.winfo_screenheight()
       
        self.position =  self.screen_width/4
        self.left_boundary = self.screen_width/3 - self.screen_width/4
        self.right_boundary = self.screen_width/1.5 - self.screen_width/4
        self.step_size = self.screen_width/100
       

        self.canvas = Canvas(self.tugofwarfenster, width=self.screen_width, height=self.screen_height, bg="khaki", bd=0, highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_line(self.screen_width // 3, 0, self.screen_width // 3, self.screen_height, fill="black", width=3)
        self.canvas.create_line(self.screen_width * 2 // 3, 0, self.screen_width * 2 // 3, self.screen_height, fill="black", width=3)
       
        self.image_tugofwar = Image.open("tugofwar.png")
        self.image_tugofwar_resized = self.image_tugofwar.resize((self.screen_width // 2, self.screen_height // 2))  # Resize the image to exactly half the screen size
        self.photo_tugofwar = ImageTk.PhotoImage(self.image_tugofwar_resized)
        self.Label_tugofwar = Label(self.tugofwarfenster, image=self.photo_tugofwar)

        self.Label_tugofwar.place(x=self.position, y=170)

       
        # Key bindings
        self.tugofwarfenster.bind("a", self.move_left)
        self.tugofwarfenster.bind("l", self.move_right)

        # Instructions
        self.info_label = Label(self.tugofwarfenster, text="Drücken Sie 'A' (links) vs 'L'(rechts)", font=("Arial", 14), bg="lightblue")
        self.info_label.place(x=0,y=0)
        self.tugofwarfenster.mainloop()

    def move_left(self, event):
        if self.position > self.left_boundary:
            self.position -= self.step_size
            self.Label_tugofwar.place(x=self.position, y=170)
        else:
            self.gewonnen("rot")

    def move_right(self, event):
        if self.position < self.right_boundary:
            self.position += self.step_size
            self.Label_tugofwar.place(x=self.position, y=170)
        else:
            self.gewonnen("blau")

    def gewonnen(self, gewinner):
        winner_window = Toplevel(self.tugofwarfenster)  # Erstellt ein neues Fenster für den Gewinner
        winner_window.attributes("-fullscreen", True)
        winner_window.configure(bg="khaki")
        winner_message = f"{gewinner} gewinnt!"  # Zeigt den Gewinner an
        Label(winner_window, text=winner_message, font=("Comic Sans MS", 100), fg="green4", bg="khaki").pack(pady=50)
        Button(winner_window, text="Return to Main Screen", font=("Comic Sans MS", 30), fg="green4", bg="khaki", command=lambda: self.return_to_main(winner_window)).pack(pady=20)

    # Setzt das Spiel zurück und kehrt zum Hauptbildschirm zurück
    def return_to_main(self, winner_window):
        winner_window.destroy()  # Schließt das Gewinner-Fenster
        self.tugofwarfenster.destroy()  # Schließt das Fenster
       

if __name__ == "__main__":
    TugOfWarGUI()
