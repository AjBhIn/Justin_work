
import tkinter as tk
import time
from PIL import Image, ImageTk

# Global Variables
score = 0
total_questions = 0

# Main Window
root = tk.Tk()
root.title("Justin's Quiz Game")
root.geometry("600x650")  # Sets the GUI width and height
root.configure(bg="#A4D2CF")  # Sets the background color of the quiz program

# Photo Images
# logo = ImageTk.PhotoImage(file=r"logo.png")
logo = tk.PhotoImage(file = "logo.png")
easy = ImageTk.PhotoImage(file=r"Easy Mode.png")
hard = ImageTk.PhotoImage(file=r"Hard Mode.png")
easyv2 = ImageTk.PhotoImage(file=r"Easy Mode 2.png")
hardv2 = ImageTk.PhotoImage(file=r"Hard Mode 2.png")
canada_flag = ImageTk.PhotoImage(file="image 12.png")

# Welcome Screen
def welcome_screen():
   global total_questions
   welcome_label = tk.Label(root, text="Welcome to Justin's Quiz Game!", font=("Helvetica", 22, "bold"),
                            bg="#A4D2CF")  # Sets the background color of the label and makes the text bold
   welcome_label.place(x=300, y=100, anchor="center")  # Sets the x and y position of the label in the welcome screen

   quiz_logo = tk.Label(root, image=logo, bg="#A4D2CF")  # Image of quiz logo
   quiz_logo.place(x=146, y=170)  # Centres the logo

   play_button = tk.Button(root, text="PLAY", font=("Helvetica", 16, "bold"), bg="#1CB9F6", fg="#000000", 
                           command=rules_screen, relief=tk.SOLID, bd=2, cursor="hand2")  # Sets the background color, text color, and font for the play button
   play_button.place(x=200, y=550, width=200, height=50)  # Sets the x and y position of the play button in the welcome screen

# Rules Screen
def rules_screen():
   clear_screen()  # Clears the screen

   rules_frame = tk.Frame(root, bg="#A4D2CF")  # Create the frame for the rules screen with the background color
   rules_frame.pack(fill=tk.BOTH, expand=True)

   rules_label = tk.Label(rules_frame, text="Rules of the Quiz Game", font=("Helvetica", 18, "bold"), bg="#A4D2CF",
                          fg="#000000")  # Sets the background color of the rules label and makes the title text bold
   rules_label.pack(pady=10)

   rules_box = tk.Frame(rules_frame, bg="#1CB9F6", bd=2, relief=tk.SOLID)  # Creates a frame for the rules box with a border
   rules_box.pack(pady=10, padx=20)

   rules_title = tk.Label(rules_box, text="Hello, Player", font=("Helvetica", 14, "bold"), bg="#1CB9F6", fg="#000000")
   rules_title.pack(pady=5)

   rules_content = tk.Label(rules_box,
                            text="• Do not cheat\n• Do not google the answers\n• Your answers will be recorded\n• Statistics of your quiz will be shown at the end\n• You will have the option to export your statistics to a text file\n• Have fun!",
                            font=("Helvetica", 14), bg="#1CB9F6", fg="#000000")  # Lists the rules of the quiz game
   rules_content.pack(padx=10, pady=5)

   guide_label = tk.Label(rules_frame, text="Quiz Modes", font=("Helvetica", 18, "bold"), bg="#A4D2CF",
                          fg="#000000")  # Creates the label for the game modes guide
   guide_label.pack(pady=10)

   guide_box = tk.Frame(rules_frame, bg="#1CB9F6", bd=2, relief=tk.SOLID)  # Creates a frame for the game modes guide box with a black border
   guide_box.pack(pady=10, padx=20)

   guide_text = tk.Label(guide_box,
                         text="You will have the choice to \nplay between two different quiz game modes",
                         font=("Helvetica", 14, "bold"), bg="#1CB9F6", fg="#000000")  # Title of the game modes guide
   guide_text.pack(padx=10, pady=5)

   easy_mode_label = tk.Label(guide_box, text="⋆ EASY MODE: \n• Multiple choice answers for the quiz.",
                              font=("Helvetica", 14, "bold"), bg="#1CB9F6", fg="green")  # Easy mode description
   easy_mode_label.pack(padx=10, pady=5)

   hard_mode_label = tk.Label(guide_box, text="⋆ HARD MODE: \n• Type in the name of the country in the textbox. \n• 10-second time limit for each question.",
                              font=("Helvetica", 14, "bold"), bg="#1CB9F6", fg="red")  # Hard mode description
   hard_mode_label.pack(padx=10, pady=5)

   ok_button = tk.Button(rules_frame, text="Okay", font=("Helvetica", 16, "bold"), bg="#1CB9F6", fg="#000000",
                         relief=tk.SOLID, bd=2, padx=10, pady=5,
                         command=game_screen)  # Goes to game screen when the button is clicked
   ok_button.pack(pady=20)

# Game Screen
def game_screen():
   clear_screen()

   easy_button = tk.Button(root, text="Easy", command=easy_mode, font=("Helvetica", 20, "bold"), bg="#A4D2CF",
                           fg="#000000", relief=tk.RAISED, bd=2, padx=20, pady=10, cursor="hand2")
   easy_button.config(image=easy)  # Set the initial image
   easy_button.bind("<Enter>", lambda event: easy_button.config(image=easyv2))  # Change image on mouse enter
   easy_button.bind("<Leave>", lambda event: easy_button.config(image=easy))  # Change back to original image on mouse leave
   easy_button.pack(fill=tk.BOTH, expand=True)

   hard_button = tk.Button(root, text="Hard", command=hard_mode, font=("Helvetica", 20, "bold"), bg="#A4D2CF",
                           fg="#000000", relief=tk.RAISED, bd=2, padx=20, pady=10, cursor="hand2")
   hard_button.config(image=hard)  # Set the initial image
   hard_button.bind("<Enter>", lambda event: hard_button.config(image=hardv2))  # Change image on mouse enter
   hard_button.bind("<Leave>", lambda event: hard_button.config(image=hard))  # Change back to original image on mouse leave
   hard_button.pack(fill=tk.BOTH, expand=True)


# Creating teh questions using classes
class QuestionMaker:
   def __init__(self, question, image_flage, option_one, option_two, option_three, option_four, master = root):

      self.width_frame = '600'
      self.bg_frame = "#A4D2CF"
      self.question = question
      self.image_flage = image_flage
      self.option_one = option_one
      self.option_two = option_two
      self.option_three = option_three
      self.option_four = option_four


      self.question_ans_frame = tk.Frame(master, width=self.width_frame, bg = 'red', height = "640")
      self.question_ans_frame.pack()

      self.question_frame = tk.Frame(self.question_ans_frame, bg="#1CB9F6", padx=10, pady=10, borderwidth=2, relief=tk.SOLID, bd=2)
      self.question_frame.pack(pady=10)

      self.question_label = tk.Label(self.question_frame, text= self.question, font=("Helvetica", 22, "bold"), bg="#1CB9F6", fg="#000000")
      self.question_label.pack()

      self.flag_image = tk.Label(self.question_ans_frame, image = self.image_flage, background = self.bg_frame)
      self.flag_image.pack(pady=(10,20))

      self.options_frame_one = tk.Frame(self.question_ans_frame, background=self.bg_frame)
      self.options_frame_one.pack(pady=(0, 20))

      self.option_one = tk.Button(self.options_frame_one, text=self.option_one, font=("Helvetica", 22, "bold"), bg="#1CB9F6", fg="#000000")
      self.option_one.pack(side='left', padx=(50,10), ipady=1)

      self.option_two = tk.Button(self.options_frame_one, text=self.option_two, font=("Helvetica", 22, "bold"), bg="#1CB9F6", fg="#000000")
      self.option_two.pack(side='left', padx=(10,50), ipady=1)

      self.options_frame_two = tk.Frame(self.question_ans_frame, background=self.bg_frame)
      self.options_frame_two.pack()

      self.option_three = tk.Button(self.options_frame_two, text=self.option_three, font=("Helvetica", 22, "bold"), bg="#1CB9F6", fg="#000000")
      self.option_three.pack(side='left', padx=(50,10), ipady=1)

      self.option_four = tk.Button(self.options_frame_two, text=self.option_four, font=("Helvetica", 22, "bold"), bg="#1CB9F6", fg="#000000")
      self.option_four.pack(side='left', padx=(10,50), ipady=1)


      # From here, this code makes the options the same in width, as they are not from the start
      self.option_one.update()
      self.option_two.update()
      self.option_three.update()
      self.option_four.update()
      
      self.option_one_width = self.option_two.winfo_width()
      self.option_two_width = self.option_two.winfo_width()
      self.option_three_width = self.option_three.winfo_width()
      self.option_four_width = self.option_four.winfo_width()

      self.biggest_options_width = [self.option_one_width, self.option_two_width, self.option_three_width, self.option_four_width]

      self.biggest_width_found = max(self.biggest_options_width)
      self.turn_width_into_pixel = str(int(self.biggest_width_found /18))

      self.option_one.configure(width= self.turn_width_into_pixel)
      self.option_two.configure(width= self.turn_width_into_pixel)
      self.option_three.configure(width= self.turn_width_into_pixel)
      self.option_four.configure(width= self.turn_width_into_pixel)
      


# Easy Mode
def easy_mode():
   global total_questions
   total_questions += 1
   clear_screen()

   timer_label = tk.Label(root, text="0:00", font=("Helvetica", 24, "bold"), bg="#A4D2CF", fg="#000000")
   timer_label.pack(pady=10)

   title_frame = tk.Frame(root, bg="#1CB9F6", padx=10, pady=10, borderwidth=2, relief=tk.SOLID, bd=2)
   title_frame.pack(pady=10)

   title_label = tk.Label(title_frame, text="You are currently playing Easy Mode!", font=("Helvetica", 22, "bold"), bg="#1CB9F6", fg="#000000") # Title of easy mode
   title_label.pack()

   countdown_text_label = tk.Label(root, text="Your game will start in...", font=("Helvetica", 32, "bold"), bg="#A4D2CF", fg="#000000")
   countdown_text_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
   countdown_text_label.after(1000, lambda: countdown_text_label.config(text=""))  # Hides the text after 1 second

   countdown_label = tk.Label(root, text="", font=("Helvetica", 150, "bold"), bg="#A4D2CF", fg="#000000")
   countdown_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

   root.update()  # Update the GUI to show the countdown labels

   def start_countdown(i):
      if i < 0:
         countdown_label.destroy()
         title_frame.destroy()
         Q1 = QuestionMaker('What flag is this?', canada_flag, "Canadaooooooo", "India", "Japan", "Lololoo")
      elif i > 0:
           countdown_label.config(text=str(i))  # Update the countdown text
           countdown_label.after(1000, start_countdown, i-1)  # Call the function again after 1 second with the next number
      elif i == 0:
           countdown_label.config(text="GO!", fg="green")  # Display "GO!" when the countdown finishes
           countdown_label.config(font=("Helvetica", 144, "bold"))  # Change the countdown font
           start_game(countdown_label, timer_label)  # Start the game
           countdown_label.after(1000, start_countdown, i-1)  # Call the function again after 1 second with the next number


   countdown_text_label.after(1000, start_countdown, 3)  # Start the countdown after 1 second

# Hard Mode
def hard_mode():
   global total_questions
   total_questions += 1
   clear_screen()

   timer_label = tk.Label(root, text="0:00", font=("Helvetica", 24, "bold"), bg="#A4D2CF", fg="#000000")
   timer_label.pack(pady=10)

   title_frame = tk.Frame(root, bg="#1CB9F6", padx=10, pady=10, borderwidth=2, relief=tk.SOLID, bd=2)
   title_frame.pack(pady=10)

   title_label = tk.Label(title_frame, text="You are currently playing Hard Mode!", font=("Helvetica", 22, "bold"), bg="#1CB9F6", fg="#000000")
   title_label.pack()

   countdown_text_label = tk.Label(root, text="Your game will start in...", font=("Helvetica", 32, "bold"), bg="#A4D2CF", fg="#000000")
   countdown_text_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
   countdown_text_label.after(1000, lambda: countdown_text_label.config(text=""))  # Hides the text after 1 second

   countdown_label = tk.Label(root, text="", font=("Helvetica", 150, "bold"), bg="#A4D2CF", fg="#000000")
   countdown_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

   root.update()  # Update the GUI to show the countdown labels


# Starting the countdown function
   def start_countdown(i):

      if i < 0:
         countdown_label.destroy()
      elif i > 0:
           countdown_label.config(text=str(i))  # Update the countdown text
           countdown_label.after(1000, start_countdown, i-1)  # Call the function again after 1 second with the next number
      elif i == 0:
           countdown_label.config(text="GO!", fg="green")  # Display "GO!" when the countdown finishes
           countdown_label.config(font=("Helvetica", 144, "bold"))  # Change the countdown font
           start_game(countdown_label, timer_label)  # Start the game
           countdown_label.after(1000, start_countdown, i-1)  # Call the function again after 1 second with the next number

   countdown_text_label.after(1000, start_countdown, 3)  # Start the countdown after 1 second

# Start the game
def start_game(countdown_label, timer_label):
   update_timer(timer_label, 0)  # Start the timer at 0 seconds

# Update the timer label
def update_timer(timer_label, seconds):
   minutes = seconds // 60
   seconds_remaining = seconds % 60
   timer_label.config(text=f"{minutes}:{seconds_remaining:02d}")
   seconds += 1
   timer_label.after(1000, update_timer, timer_label, seconds)  # Update the timer after 1 second

# Clear the screen
def clear_screen():
   for widget in root.winfo_children():
       widget.destroy()

# Wrong Answer
def wrong_answer():
   global score
   clear_screen()  # Clear the screen
   score_label = tk.Label(root, text="Incorrect!", font=("Helvetica", 16))
   score_label.pack()
   show_score()

# Correct Answer
def correct_answer():
   global score
   score += 1
   clear_screen()  # Clear the screen
   score_label = tk.Label(root, text="Correct!", font=("Helvetica", 16))
   score_label.pack()
   show_score()

# Check Answer
def check_answer(answer):
   if answer.lower() == "france":
       correct_answer()
   else:
       wrong_answer()

# Show Score
def show_score():
   score_label = tk.Label(root, text=f"Score: {score}/{total_questions}", font=("Helvetica", 16))
   score_label.pack()

# Start the quiz
welcome_screen()

# Main loop
root.mainloop()
