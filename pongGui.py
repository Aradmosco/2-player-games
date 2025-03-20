from tkinter import *
from PIL import Image, ImageTk

class PongGame:
    def __init__(self, root):
        # Create the main game window in fullscreen mode
        self.fenster = Toplevel(root)
        self.fenster.attributes("-fullscreen", True)
        self.fenster.configure(bg="green")

        # Get screen dimensions
        self.screen_width = self.fenster.winfo_screenwidth()
        self.screen_height = self.fenster.winfo_screenheight()

        # Create a canvas for rendering game elements
        self.canvas = Canvas(self.fenster, width=self.screen_width, height=self.screen_height, bg="khaki")
        self.canvas.pack()

        # Load and resize images for paddles and ball
        self.paddlered_img = Image.open("paddlered.png").resize((30, 150))
        self.paddleblue_img = Image.open("paddleblue.png").resize((30, 150))
        self.ball_img = Image.open("ball.png").resize((50, 50))

        # Convert images to be used in Tkinter
        self.paddlered_photo = ImageTk.PhotoImage(self.paddlered_img)
        self.paddleblue_photo = ImageTk.PhotoImage(self.paddleblue_img)
        self.ball_photo = ImageTk.PhotoImage(self.ball_img)

        # Create the left paddle
        self.paddle_left = self.canvas.create_image(50, self.screen_height//2, anchor="center", image=self.paddlered_photo)

        # Create the right paddle
        self.paddle_right = self.canvas.create_image(self.screen_width - 50, self.screen_height//2, anchor="center", image=self.paddleblue_photo)

        # Create the ball
        self.ball = self.canvas.create_image(self.screen_width//2, self.screen_height//2, anchor="center", image=self.ball_photo)

        # Initial ball movement values
        self.ball_dx = 6  # Ball movement speed in X direction
        self.ball_dy = 6  # Ball movement speed in Y direction
        self.paddle_speed = 30  # Paddle movement speed

        # Score tracking
        self.score_left = 0
        self.score_right = 0
        self.max_score = 3  # Winning score

        # Score display label
        self.score_label = Label(self.fenster, text=f"{self.score_left} - {self.score_right}", font=("Arial", 30), bg="khaki")
        self.score_label.place(x=self.screen_width//2 - 50, y=20)

        # Key bindings for paddle movement
        self.fenster.bind("<w>", lambda event: self.move_paddle(self.paddle_left, -self.paddle_speed))  # Move left paddle up
        self.fenster.bind("<s>", lambda event: self.move_paddle(self.paddle_left, self.paddle_speed))   # Move left paddle down
        self.fenster.bind("<Up>", lambda event: self.move_paddle(self.paddle_right, -self.paddle_speed))  # Move right paddle up
        self.fenster.bind("<Down>", lambda event: self.move_paddle(self.paddle_right, self.paddle_speed))  # Move right paddle down

        # Start the game loop
        self.update_game()
        self.fenster.mainloop()

    def move_paddle(self, paddle, dy):
        """Moves a paddle up or down while keeping it within screen limits."""
        x, y = self.canvas.coords(paddle)
        if 50 < y + dy < self.screen_height - 50:  # Prevent paddles from moving off-screen
            self.canvas.move(paddle, 0, dy)

    def update_game(self):
        """Handles ball movement, collision detection, and scoring."""
        x, y = self.canvas.coords(self.ball)  # Get current ball position

        # Ball collision with top or bottom walls
        if y <= 0 or y >= self.screen_height:
            self.ball_dy = -self.ball_dy  # Reverse ball's vertical movement direction
            self.ball_dx += 2  # Increase ball speed after each bounce
            self.ball_dy += 2

        # Ball collision with left paddle
        paddle_x, paddle_y = self.canvas.coords(self.paddle_left)
        if x <= 80 and paddle_y - 75 < y < paddle_y + 75:  # If ball is within paddle range
            self.ball_dx = abs(self.ball_dx)  # Ensure ball moves right after hitting the left paddle
            self.ball_dx += 2  # Increase ball speed
            self.ball_dy += 2

        # Ball collision with right paddle
        paddle_x, paddle_y = self.canvas.coords(self.paddle_right)
        if x >= self.screen_width - 80 and paddle_y - 75 < y < paddle_y + 75:  # If ball is within paddle range
            self.ball_dx += 2  # Increase ball speed
            self.ball_dy += 2
            self.ball_dx = -abs(self.ball_dx)  # Ensure ball moves left after hitting the right paddle
            

        # Ball goes out of bounds (Scoring System)
        if x <= 0:  # Ball goes off the left side (right player scores)
            self.score_right += 1
            self.update_score()
            self.ball_dx = 6  # Reset ball speed after a point
            self.ball_dy = 6
        elif x >= self.screen_width:  # Ball goes off the right side (left player scores)
            self.score_left += 1
            self.update_score()
            self.ball_dx = 6  # Reset ball speed after a point
            self.ball_dy = 6

        # Move the ball based on current speed and direction
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        self.fenster.after(20, self.update_game)  # Call this function every 20ms to update game state

    def update_score(self):
        """Updates the score display and checks for a winner."""
        self.score_label.config(text=f"{self.score_left} - {self.score_right}")  # Update the score label

        # Check if a player has won
        if self.score_left >= self.max_score:
            self.display_winner("Player Left Wins!")  # Left player wins
        elif self.score_right >= self.max_score:
            self.display_winner("Player Right Wins!")  # Right player wins
        else:
            self.reset_ball()  # Reset ball position after each point

    def reset_ball(self):
        """Resets the ball position and speed after a point is scored."""
        self.canvas.coords(self.ball, self.screen_width//2, self.screen_height//2)  # Move ball to center
        self.ball_dx *= -1  # Reverse the ball's movement direction
        self.ball_dx = 6  # Reset ball speed
        self.ball_dy = 6

    def display_winner(self, message):
        """Displays a winner message and provides an option to return to the main screen."""
        winner_window = Toplevel(self.fenster)  # Create a new window for winner message
        winner_window.attributes("-fullscreen", True)
        winner_window.configure(bg="khaki")

        # Display winner text
        Label(winner_window, text=message, font=("Arial", 50), bg="khaki").pack(pady=50)

        # Button to return to the main screen
        Button(winner_window, text="Return to Main Screen", font=("Arial", 30),
               command=lambda: self.return_to_main(winner_window)).pack(pady=20)

    def return_to_main(self, winner_window):
        """Closes the winner screen and main game window."""
        winner_window.destroy()  # Close winner screen
        self.fenster.destroy()  # Close main game window

# Run Pong if script is executed directly
if __name__ == "__main__":
    PongGame()

