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


    def createWidgets(self):
        self.result = tk.Label(self, text="0", width=30, anchor=tk.E)
        self.result.pack()

        f1 = tk.Frame(self)
        self.clear = tk.Button(f1, text="C", width=7, command=self.clear)
        self.clear.pack(side=tk.LEFT)
        self.pm = tk.Button(f1, text="+/-", width=7, command=self.togglepm)
        self.pm.pack(side=tk.LEFT)
        self.percent = tk.Button(f1, text="%", width=7, command=self.percent)
        self.percent.pack(side=tk.LEFT)
        self.divide = tk.Button(f1, text="/", width=7, command=lambda x="divide": self.operator(x))
        self.divide.pack(side=tk.LEFT)
        f1.pack()

        f2 = tk.Frame(self)
        self.seven = tk.Button(f2, text="7", width=7, command=lambda x="7": self.digit(x))
        self.seven.pack(side=tk.LEFT)
        self.eight = tk.Button(f2, text="8", width=7, command=lambda x="8": self.digit(x))
        self.eight.pack(side=tk.LEFT)
        self.nine = tk.Button(f2, text="9", width=7, command=lambda x="9": self.digit(x))
        self.nine.pack(side=tk.LEFT)
        self.multiply = tk.Button(f2, text="X", width=7, command=lambda x="multiply": self.operator(x))
        self.multiply.pack(side=tk.LEFT)
        f2.pack()

        f3 = tk.Frame(self)
        self.four = tk.Button(f3, text="4", width=7, command=lambda x="4": self.digit(x))
        self.four.pack(side=tk.LEFT)
        self.five = tk.Button(f3, text="5", width=7, command=lambda x="5": self.digit(x))
        self.five.pack(side=tk.LEFT)
        self.six = tk.Button(f3, text="6", width=7, command=lambda x="6": self.digit(x))
        self.six.pack(side=tk.LEFT)
        self.subtract = tk.Button(f3, text="-", width=7, command=lambda x="subtract": self.operator(x))
        self.subtract.pack(side=tk.LEFT)
        f3.pack()

        f4 = tk.Frame(self)
        self.one = tk.Button(f4, text="1", width=7, command=lambda x="1": self.digit(x))
        self.one.pack(side=tk.LEFT)
        self.two = tk.Button(f4, text="2", width=7, command=lambda x="2": self.digit(x))
        self.two.pack(side=tk.LEFT)
        self.three = tk.Button(f4, text="3", width=7, command=lambda x="3": self.digit(x))
        self.three.pack(side=tk.LEFT)
        self.add = tk.Button(f4, text="+", width=7, command=lambda x="add": self.operator(x))
        self.add.pack(side=tk.LEFT)
        f4.pack()

        f5 = tk.Frame(self)
        self.zero = tk.Button(f5, text="0", width=15, command=lambda x="0": self.digit(x))
        self.zero.pack(side=tk.LEFT)
        self.decimal = tk.Button(f5, text=".", width=7, command=lambda x=".": self.digit(x))
        self.decimal.pack(side=tk.LEFT)
        self.equals = tk.Button(f5, text="=", width=7, command=self.equals)
        self.equals.pack(side=tk.LEFT)
        f5.pack()

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()





app = Calculator()
app.master.title('Simple Calculator')
app.mainloop()