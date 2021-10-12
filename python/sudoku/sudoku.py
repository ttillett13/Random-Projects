import time
import tkinter as tk
from tkinter import ttk
import SudokuGenerator as sg
from tkmacosx import Button


class Sudoku(tk.Frame):

    size = 9
    entries = {}
    puzzle = []
    solution = []
    start_time = 0

    def __init__(self, puzzle, solution, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.puzzle = puzzle
        self.solution = solution
        self.create_widgets()
        self.start_time = time.time()

    def check_solution(self):
        end_time = time.time()
        time_took = int(end_time-self.start_time)
        minutes = int(time_took / 60)
        seconds = int(time_took % 60)
        congrats_text = "You completed the puzzle in " + str(minutes) + "m" + str(seconds) + "s."
        correct = True
        for location in self.entries.keys():
            row = location[0]
            col = location[1]
            entry = self.entries[location]
            value = entry.get()
            if value:
                if int(value) == self.solution[row][col]:
                    entry.config({"background": "Green"})
                else:
                    entry.config({"background": "Red"})
                    correct = False
            else:
                entry.config({"background": "White"})
                correct = False
        if correct:
            self.label1.config({"text": "Congratulations!"})
            self.label2.config({"text": congrats_text})

    def create_widgets(self):
        print(self.winfo_geometry())
        for i in range(self.size):
            f = tk.Frame(self)
            for j in range(self.size):
                value = self.puzzle[i][j]
                if value != 0:
                    item = tk.Label(f, text=str(value), width="2", padx=4)
                    item.pack(side=tk.LEFT, fill="x")
                else:
                    item = tk.Entry(f, width="2")
                    item.pack(side=tk.LEFT, fill="x")
                    self.entries[(i,j)] = item
                if (j+1) % 3 == 0:
                    sep = tk.ttk.Separator(f, orient='vertical')
                    sep.pack(side=tk.LEFT, fill="y")
            f.pack()
            #f.pack(fill="both", expand=1)
            if (i+1) % 3 == 0:
                sep = tk.ttk.Separator(self, orient='horizontal')
                sep.pack(fill="x")
        f = tk.Frame(self)
        self.button = Button(f, text="Check", command=self.check_solution)
        self.button.pack()
        f.pack(fill="both")
        self.label1 = tk.Label(f, text="")
        self.label1.pack()
        self.label2 = tk.Label(f, text="")
        self.label2.pack()
        f.pack(fill="both")


sudoku = sg.SudokuGenerator("easy")
app = Sudoku(sudoku.puzzle, sudoku.solution)
app.master.title('Sudoku')
app.master.geometry("%dx%d%+d%+d" % (300, 330, 250, 125))
app.mainloop()
#print(attempt)