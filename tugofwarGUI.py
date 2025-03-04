from tkinter import *
from PIL import Image, ImageTk

class TugOfWarGUI:
    def __init__(self):
        self.fenster = Tk()
        self.fenster.attributes("-fullscreen", True) 
        self.fenster.configure(bg="khaki")
        self.screen_width = self.fenster.winfo_screenwidth()
        self.screen_height = self.fenster.winfo_screenheight()
        
        self.position =  self.screen_width/4
        self.left_boundary = self.screen_width/8
        self.right_boundary = self.screen_width - self.screen_width/8
        self.step_size = self.screen_width/80
        
        self.image_tugofwar = Image.open("tugofwar.png")
        self.image = self.image_tugofwar.resize((int(self.screen_width/2), int(self.screen_height/2)))  # Resize if needed
        self.photo_tugofwar = ImageTk.PhotoImage(self.image_tugofwar)
        self.Label_tugofwar = Label(self.fenster, image=self.photo_tugofwar)

        # # Load images
        # self.image = Image.open("rope.png")  # Use a small image for the moving object
        # self.image = self.image.resize((60, 60))  # Resize image
        # self.image_tk = ImageTk.PhotoImage(self.image)

        # Moving label (Indicator)
        self.Label_tugofwar.place(x=self.position, y=170)

        # # Key bindings
        # self.fenster.bind("a", self.move_left)
        # self.fenster.bind("l", self.move_right)

        # Instructions
        # self.info_label = Label(self.fenster, text="Press 'A' (Left) vs 'L' (Right)", font=("Arial", 14), bg="lightblue")
        # self.info_label.pack(pady=10)

        self.fenster.mainloop()

    # def move_left(self, event):
    #     """ Move indicator to the left when Player 1 (A) presses key """
    #     if self.position > self.left_boundary:
    #         self.position -= self.step_size
    #         self.label.place(x=self.position, y=170)
    #     else:
    #         self.end_game("Player 1 Wins!")

    # def move_right(self, event):
    #     """ Move indicator to the right when Player 2 (L) presses key """
    #     if self.position < self.right_boundary:
    #         self.position += self.step_size
    #         self.label.place(x=self.position, y=170)
    #     else:
    #         self.end_game("Player 2 Wins!")

    # def end_game(self, winner_text):
    #     """ Display winner message and close the game """
    #     self.info_label.config(text=winner_text, font=("Arial", 16, "bold"))
    #     self.fenster.unbind("a")
    #     self.fenster.unbind("l")


if __name__ == "__main__":
    TugOfWarGUI()
    
