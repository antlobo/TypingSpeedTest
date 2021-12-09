import tkinter as tk
from tkinter import messagebox

BLUE = "#145da0"
WHITE = "#fff"
BLACK = "#000"
FONT_NAME = "Courier"


def show_result(words_per_min: int = None, chars_per_min: int = None, wrong_words: str = None) -> None:
    """
    Shows a messagebox with the results of the words per min and chars per min or the wrong words
    :param words_per_min: an integer with the number of words per minute
    :param chars_per_min: an integer with the number of chars per minute
    :param wrong_words: a string with all the wrong words the user typed
    :return: it doesn't return a value
    """
    if wrong_words:
        messagebox.showinfo("Results", f"Wrong words were: \n{wrong_words}")
    elif words_per_min and chars_per_min:
        messagebox.showinfo("Results", f"Words per min: {words_per_min} \nChars per min: {chars_per_min}")


class AppUI(tk.Tk):
    def __init__(self, start_func):
        super().__init__()
        self.title("TS Test")
        self.config(padx=50, pady=50, bg=WHITE)

        self.lbl_title = tk.Label(text="Typing Speed\nTest", fg=BLUE, font=(FONT_NAME, 45), bg=WHITE)
        self.lbl_title.grid(column=0, columnspan=3, row=0)

        self.txt_words = tk.Text(self, state="normal", highlightthickness=0,
                                 width=80, height=15,
                                 wrap="word", font=(FONT_NAME, 12))
        self.txt_words.grid(column=0, columnspan=3, row=1)
        self.txt_words.bindtags([str(self.txt_words), str(self), "all"])

        self.lbl_explanation_text = tk.Label(text="Start writing in the next box:",
                                             fg=BLACK, font=(FONT_NAME, 8), bg=WHITE)
        self.lbl_explanation_text.grid(column=0, row=2, columnspan=3)

        self.txt_type_words = tk.Text(self, state="disabled", highlightthickness=0,
                                      width=80, height=10,
                                      wrap="word", font=(FONT_NAME, 12))
        self.txt_type_words.grid(column=0, columnspan=3, row=3, pady=20)

        self.btn_start = tk.Button(text="Start test", highlightthickness=0, command=start_func)
        self.btn_start.grid(column=1, row=4)

    def start_game(self, wordlist: str) -> None:
        """
        Starts the game erasing the words in the fields and getting focus on the field to type the words
        :param wordlist: a string with all the words to be typed by the user
        :return: it doesn't return a value
        """
        self.txt_type_words.configure(state="normal")
        self.txt_type_words.delete("0.0", tk.END)
        self.txt_type_words.focus_set()

        self.txt_words.delete("0.0", tk.END)
        self.txt_words.insert(tk.END, wordlist)

    def stop_game(self) -> None:
        """
        Disables the typed words field and updates the text of the button
        :return: it doesn't return a value
        """
        self.txt_type_words.configure(state="disabled")
        self.btn_start.configure(text=f"Start test")

    def update_button_text(self, count: int) -> None:
        """
        Updates the text inside the button with the remaining seconds to start the test
        :param count: integer which represent the number of seconds remaining
        :return: it doesn't return a value
        """
        if count:
            self.btn_start.configure(text=f"Start test ({count}s)")
        else:
            self.btn_start.configure(text=f"Stop test")

    def get_typed_words(self) -> list:
        """
        Gets a list of the typed words
        :return: a list with the typed words
        """
        return self.txt_type_words.get("0.0", tk.END).split()
