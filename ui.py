import tkinter as tk
from tkinter import messagebox
import ctypes
from quiz_brain import QuizBrain

ctypes.windll.shcore.SetProcessDpiAwareness(1)


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.__THEME_COLOR = "#375362"

        self.window = tk.Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20)
        self.window.resizable(False, False)
        self.window.config(bg=self.__THEME_COLOR)

        self.flash_after = self.window.after(0)

        self.__TRUE_IMG = tk.PhotoImage(file="assets/true.png")
        self.__FALSE_IMG = tk.PhotoImage(file="assets/false.png")

        self.score = tk.Label(bg=self.__THEME_COLOR, fg="#fff", font=("arial", 12, "normal"))
        self.score.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = tk.Canvas(width=500, height=350, highlightthickness=0)
        self.canvas_text = self.canvas.create_text(
            250,
            175,
            font=("arial", 16, "italic"),
            width=480
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true_btn = tk.Button(image=self.__TRUE_IMG, command=self.check_true_pressed_answer)
        self.true_btn.config(borderwidth=0, highlightthickness=0)
        self.true_btn.grid(row=2, column=0, padx=20, pady=20)

        self.false_btn = tk.Button(image=self.__FALSE_IMG, command=self.check_false_pressed_answer)
        self.false_btn.config(borderwidth=0, highlightthickness=0)
        self.false_btn.grid(row=2, column=1, padx=20, pady=20)

        self.next_question()
        self.window.mainloop()

    def flash_canvas(self, is_right: bool):
        self.canvas.config(bg=("green" if is_right else "red"))
        self.canvas.itemconfig(self.canvas_text, text=("Correct" if is_right else "Wrong"))
        self.flash_after = self.window.after(500, self.next_question)

    def check_true_pressed_answer(self):
        is_right = self.quiz.check_answer("True")
        self.flash_canvas(is_right)

    def check_false_pressed_answer(self):
        is_right = self.quiz.check_answer("False")
        self.flash_canvas(is_right)

    def next_question(self):
        self.canvas.config(bg="#fff")

        score = self.quiz.get_score()
        self.score.config(text=f"Score: {score}")

        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question_text)
        else:
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            self.canvas.itemconfig(self.canvas_text,
                                   text=f"You scored {self.quiz.get_score()} out of {self.quiz.get_question_number()}")
            messagebox.showinfo("You've completed the quiz",
                                f"You scored {self.quiz.get_score()} out of {self.quiz.get_question_number()}")
