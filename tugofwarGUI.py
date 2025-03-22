from tkinter import *
from PIL import Image, ImageTk

class TugOfWarGUI:
    def __init__(self, main_app):
        self.main_app = main_app
        self.tugofwarfenster = Toplevel(main_app.fenstermain)
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

        # Flag to ensure 'gewonnen' is called only once
        self.game_over = False

        # Key bindings
        self.tugofwarfenster.bind("a", self.move_left)
        self.tugofwarfenster.bind("l", self.move_right)

        # Instructions
        self.info_label = Label(self.tugofwarfenster, text="Drücken Sie 'A' (links) vs 'L'(rechts)", font=("Arial", 14), bg="lightblue")
        self.info_label.place(x=0,y=0)
        self.tugofwarfenster.mainloop()

    def move_left(self, event):
        if self.game_over:
            return  # Prevent further movement if the game is over

        if self.position > self.left_boundary:
            self.position -= self.step_size
            self.Label_tugofwar.place(x=self.position, y=170)
        else:
            self.tugofwarfenster.unbind("a")
            self.tugofwarfenster.unbind("l")
            self.game_over = True  # Set the flag to prevent further calls
            self.gewonnen("rot")

    def move_right(self, event):
        if self.game_over:
            return  # Prevent further movement if the game is over

        if self.position < self.right_boundary:
            self.position += self.step_size
            self.Label_tugofwar.place(x=self.position, y=170)
        else:
            self.tugofwarfenster.unbind("a")
            self.tugofwarfenster.unbind("l")
            self.game_over = True  # Set the flag to prevent further calls
            self.gewonnen("blau")

    def gewonnen(self, gewinner):
        if self.game_over:  # Ensure the method is called only once
            

            if gewinner == "blau":
                self.main_app.score_blue += 1  # Update blue score in main
            else:
                self.main_app.score_red += 1  # Update red score in main    

            # Update the label in the main screen
            self.main_app.score_label.config(text=f"Blau: {self.main_app.score_blue} | Rot: {self.main_app.score_red}")
            
            winner_window = Toplevel(self.tugofwarfenster)  # Create a new window for the winner
            winner_window.attributes("-fullscreen", True)
            winner_window.configure(bg="khaki")
            winner_message = f"{gewinner} gewinnt!"  # Display the winner
            Label(winner_window, text=winner_message, font=("Comic Sans MS", 100), fg="green4", bg="khaki").pack(pady=50)
            Button(winner_window, text="Return to Main Screen", font=("Comic Sans MS", 30), fg="green4", bg="khaki", command=lambda: self.return_to_main(winner_window)).pack(pady=20)

    # Reset the game and return to the main screen
    def return_to_main(self, winner_window):
        winner_window.destroy()  # Close the winner window
        self.tugofwarfenster.destroy()  # Close the game window

if __name__ == "__main__":
    TugOfWarGUI()
