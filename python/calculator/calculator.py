import tkinter as tk


class Calculator(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    lhs = 0
    rhs = ""
    total = 0
    operand = None


    def clear(self):
        print("clear")
        self.lhs = 0
        self.rhs = ""
        self.total = 0
        self.result.configure(text="0")

    def togglepm(self):
        print("toggle plus/minus")
        if self.rhs is not "":
            self.rhs = str(float(self.rhs) * -1)
            self.result.configure(text=self.rhs)
        else:
            self.lhs = self.lhs * -1
            self.result.configure(text=self.lhs)

    def equals(self):
        print("equals")
        self.calculate()

    def digit(self, digit):
        print(digit)
        self.rhs = self.rhs + digit
        self.result.configure(text=self.rhs)

    def operator(self, operation):
        print(operation)
        if self.rhs is not "":
            self.lhs = float(self.rhs)
        self.rhs = ""
        self.operand = operation

    def percent(self):
        print("percent")
        if self.rhs is not "":
            self.rhs = str(float(self.rhs)/100)
            self.result.configure(text=self.rhs)
        else:
            self.total = self.total / 100
            self.result.configure(text=self.total)

    def calculate(self):
        total = 0
        if self.rhs is not "":
            rhs = float(self.rhs)
        else:
            rhs = 0
        if self.operand is "divide":
            total = self.lhs / rhs
        elif self.operand is "multiply":
            total = self.lhs * rhs
        elif self.operand is "add":
            total = self.lhs + rhs
        elif self.operand is "subtract":
            total = self.lhs - rhs
        self.operand = None
        self.total = total
        self.lhs = total
        self.rhs = ""
        self.result.configure(text=total)

    def makeButton(self, frame, text, width, command):
        self.button = tk.Button(frame, text=text, width=width, command=command)
        self.button.pack(side=tk.LEFT)

    def createWidgets(self):
        self.result = tk.Label(self, text="0", width=30, anchor=tk.E)
        self.result.pack()

        f1 = tk.Frame(self)
        self.makeButton(f1, "C", 7, self.clear)
        self.makeButton(f1, "+/-", 7, self.togglepm)
        self.makeButton(f1, "%", 7, self.percent)
        self.makeButton(f1, "/", 7, lambda x="divide": self.operator(x))
        f1.pack()

        f2 = tk.Frame(self)
        self.makeButton(f2, "7", 7, lambda x="7": self.digit(x))
        self.makeButton(f2, "8", 7, lambda x="8": self.digit(x))
        self.makeButton(f2, "9", 7, lambda x="9": self.digit(x))
        self.makeButton(f2, "X", 7, lambda x="multiply": self.operator(x))
        f2.pack()

        f3 = tk.Frame(self)
        self.makeButton(f3, "4", 7, lambda x="4": self.digit(x))
        self.makeButton(f3, "5", 7, lambda x="5": self.digit(x))
        self.makeButton(f3, "6", 7, lambda x="6": self.digit(x))
        self.makeButton(f3, "-", 7, lambda x="subtract": self.operator(x))
        f3.pack()

        f4 = tk.Frame(self)
        self.makeButton(f4, "1", 7, lambda x="1": self.digit(x))
        self.makeButton(f4, "2", 7, lambda x="2": self.digit(x))
        self.makeButton(f4, "3", 7, lambda x="3": self.digit(x))
        self.makeButton(f4, "+", 7, lambda x="add": self.operator(x))
        f4.pack()

        f5 = tk.Frame(self)
        self.makeButton(f5, "0", 15, lambda x="0": self.digit(x))
        self.makeButton(f5, ".", 7, lambda x=".": self.digit(x))
        self.makeButton(f5, "=", 7, self.equals)
        f5.pack()

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


app = Calculator()
app.master.title('Simple Calculator')
app.mainloop()