import tkinter as tk
import random

from GameUI.SudokuCell import SudokuCell

# TODO: Add button for cell input support
# TODO: Ask for name and surname and save the result under db with format name_surname.txt
# TODO-OPTIONAL: Auto solve button
class Sudoku:
    def __init__(self, sudoku_generator):
        self.input_fields = None
        self.sudoku_generator = sudoku_generator
        self.window = tk.Tk()
        self.window.maxsize(width=500, height=440)
        self.window.minsize(width=500, height=440)
        self.make_grid()
        self.window.mainloop()

    def make_grid(self):
        self.input_fields = []
        sudoku_array = self.sudoku_generator.get_sudoku()
        for row in range(0, len(sudoku_array[0])):
            x_cord = 0
            for element in sudoku_array[row]:
                if random.randint(0, 9) > 6:
                    temp = SudokuCell(element, self.window, justify='center')
                    self.input_fields.append(temp)
                else:
                    v = tk.StringVar(self.window, value=str(element))
                    temp = tk.Entry(readonlybackground='#ADD8E6', textvariable=v, justify='center', state='readonly')
                temp.place(x=x_cord, y=row * 40, width=40, height=40)
                x_cord = x_cord + 40
        reset_button = tk.Button(self.window, text="New Sudoku", command=self.make_grid)
        submit_button = tk.Button(self.window, text="Submit", command=self.all_answers)
        reset_button.place(relx=0.5, rely=0.95, anchor='center')
        submit_button.place(relx=0.5, rely=0.87, anchor='center')


        input_one = tk.Button(self.window, text="1", command=lambda: self.set_text("1", self.window.focus_get()))
        input_one.place(relx=0.75, rely=0.25)
        input_two = tk.Button(self.window, text="2", command=lambda: self.set_text("2", self.window.focus_get()))
        input_two.place(relx=0.83, rely=0.25)
        input_three = tk.Button(self.window, text="3", command=lambda: self.set_text("3", self.window.focus_get()))
        input_three.place(relx=0.91, rely=0.25)
        input_four = tk.Button(self.window, text="4", command=lambda: self.set_text("4", self.window.focus_get()))
        input_four.place(relx=0.75, rely=0.15)
        input_five = tk.Button(self.window, text="5", command=lambda: self.set_text("5", self.window.focus_get()))
        input_five.place(relx=0.83, rely=0.15)
        input_six = tk.Button(self.window, text="6", command=lambda: self.set_text("6", self.window.focus_get()))
        input_six.place(relx=0.91, rely=0.15)
        input_seven = tk.Button(self.window, text="7", command=lambda: self.set_text("7", self.window.focus_get()))
        input_seven.place(relx=0.75, rely=0.05)
        input_eight = tk.Button(self.window, text="8", command=lambda: self.set_text("8", self.window.focus_get()))
        input_eight.place(relx=0.83, rely=0.05)
        input_nine = tk.Button(self.window, text="9", command=lambda: self.set_text("9", self.window.focus_get()))
        input_nine.place(relx=0.91, rely=0.05)
        input_clear = tk.Button(self.window, text="Clear", command=lambda: self.set_text("", self.window.focus_get()))
        input_clear.place(relx=0.81, rely=0.35)

    def set_text(self, text, entry):
        entry.input_value(text)
        return

    #TODO: Refactor this. Make a win function-> ask for name surname then save sudoku solution in .txt
    def all_answers(self):
        for cell in self.input_fields:
            if not cell.solved():
                fail_button = tk.Button(self.window, text="The solution does not fit. Try again :)",
                                        command=lambda: fail_button.place_forget())
                fail_button.place(relx=0.5, rely=0.5, anchor='center')
                return False
        win_button = tk.Button(self.window, text="You Won!  Press here for a new puzzle!", command=self.make_grid)
        win_button.place(relx=0.5, rely=0.5, anchor='center')
