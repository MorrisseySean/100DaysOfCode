from tkinter import *
import os
from quiz_brain import QuizBrain

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
THEME_COLOR = "#375362"
Q_FONT = ('Calibri', 18, 'normal')
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250

class QuizInterface():
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
    
        # --- Setup Window -- #
        self.window = Tk()
        self.window.title("Trivia Whiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # --- Load images --- #
        self.true_image = PhotoImage(file=THIS_FOLDER+'/images/true.png')
        self.false_image = PhotoImage(file=THIS_FOLDER+'/images/false.png')
        # --- Score Label --- #
        self.score = Label(text='Score: 0', bg=THEME_COLOR, fg='white', font=('Calibri', 12, 'normal'))

        # --- Setup Canvas --- #
        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(CANVAS_WIDTH / 2, 
            CANVAS_HEIGHT / 2, 
            width=CANVAS_WIDTH-50,
            text='', 
            font=Q_FONT)
        
        # --- Set up buttons --- #
        self.true_btn = Button(image=self.true_image, command=self.true_clicked, highlightthickness=0)
        self.false_btn = Button(image=self.false_image, command=self.false_clicked, highlightthickness=0)

        # --- Place items in window --- #
        self.score.grid(row=0, column=1, sticky=('NSEW'))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)
        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        # Get the first question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # Upon recieving a new question reset the background to white
        self.canvas.config(bg='white')
        # Check if the quiz still has questions
        if self.quiz.still_has_questions():
            # If it does, get a new question and reenable the buttons
            self.canvas.itemconfig(self.canvas_text, text=self.quiz.next_question())
            self.true_btn.config(state='active')
            self.false_btn.config(state='active')
        else:
            # Show the user their score
            self.canvas.itemconfig(self.canvas_text, text=f"Game Over!\nYou answered {self.quiz.score} out of {self.quiz.question_number} questions!")

    # Deal with the true button being clicked
    def true_clicked(self):
        # Find if the answer is true or false
        answer = self.quiz.check_answer(True)
        # Disable the buttons until a new question is received 
        self.true_btn.config(state='disabled')
        self.false_btn.config(state='disabled')
        # Process the answer
        self.process_answer(answer)

    # Deal with the false button being clicked
    def false_clicked(self):        
        # Find if the answer is true or false
        answer = self.quiz.check_answer(False) 
        # Disable the buttons until a new question is received        
        self.true_btn.config(state='disabled')
        self.false_btn.config(state='disabled')
        # Process the answer
        self.process_answer(answer)

    # Show the user the results of their answer
    def process_answer(self, answer:bool):
        if answer:
            # Change the background to green
            self.canvas.config(bg='green')
            # Update the score display
            self.score.config(text=f'Score: {self.quiz.score}')
        else:
            # Change the background to red
            self.canvas.config(bg='red')
        # After 1.5s, get another question
        self.window.after(1500, func=self.get_next_question)
