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

    def divide(self):
        print("divide")
        if self.rhs is not "":
            self.lhs = float(self.rhs)
        self.rhs = ""
        self.operand = "divide"

    def multiply(self):
        print("multiply")
        if self.rhs is not "":
            self.lhs = float(self.rhs)
        self.rhs = ""
        self.operand = "multiply"

    def subtract(self):
        print("subtract")
        if self.rhs is not "":
            self.lhs = float(self.rhs)
        self.rhs = ""
        self.operand = "subtract"

    def add(self):
        print("add")
        if self.rhs is not "":
            self.lhs = float(self.rhs)
        self.rhs = ""
        self.operand = "add"

    def equals(self):
        print("equals")
        self.calculate()

    def seven(self):
        print("seven")
        self.rhs = self.rhs + "7"
        self.result.configure(text=self.rhs)

    def eight(self):
        print("eight")
        self.rhs = self.rhs + "8"
        self.result.configure(text=self.rhs)

    def nine(self):
        print("nine")
        self.rhs = self.rhs + "9"
        self.result.configure(text=self.rhs)

    def four(self):
        print("four")
        self.rhs = self.rhs + "4"
        self.result.configure(text=self.rhs)

    def five(self):
        print("five")
        self.rhs = self.rhs + "5"
        self.result.configure(text=self.rhs)

    def six(self):
        print("six")
        self.rhs = self.rhs + "6"
        self.result.configure(text=self.rhs)

    def one(self):
        print("one")
        self.rhs = self.rhs + "1"
        self.result.configure(text=self.rhs)

    def two(self):
        print("two")
        self.rhs = self.rhs + "2"
        self.result.configure(text=self.rhs)

    def three(self):
        print("three")
        self.rhs = self.rhs + "3"
        self.result.configure(text=self.rhs)

    def zero(self):
        print("zero")
        self.rhs = self.rhs + "0"
        self.result.configure(text=self.rhs)

    def decimal(self):
        print("decimal")
        self.rhs = self.rhs + "."
        self.result.configure(text=self.rhs)

    def digit(self, digit):
        print(digit)
        self.rhs = self.rhs + digit
        self.result.configure(text=self.rhs)


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
        self.divide = tk.Button(f1, text="/", width=7, command=self.divide)
        self.divide.pack(side=tk.LEFT)
        f1.pack()

        f2 = tk.Frame(self)
        self.seven = tk.Button(f2, text="7", width=7, command=lambda x="7": self.digit(x))
        self.seven.pack(side=tk.LEFT)
        self.eight = tk.Button(f2, text="8", width=7, command=self.eight)
        self.eight.pack(side=tk.LEFT)
        self.nine = tk.Button(f2, text="9", width=7, command=self.nine)
        self.nine.pack(side=tk.LEFT)
        self.multiply = tk.Button(f2, text="X", width=7, command=self.multiply)
        self.multiply.pack(side=tk.LEFT)
        f2.pack()

        f3 = tk.Frame(self)
        self.four = tk.Button(f3, text="4", width=7, command=self.four)
        self.four.pack(side=tk.LEFT)
        self.five = tk.Button(f3, text="5", width=7, command=self.five)
        self.five.pack(side=tk.LEFT)
        self.six = tk.Button(f3, text="6", width=7, command=self.six)
        self.six.pack(side=tk.LEFT)
        self.subtract = tk.Button(f3, text="-", width=7, command=self.subtract)
        self.subtract.pack(side=tk.LEFT)
        f3.pack()

        f4 = tk.Frame(self)
        self.one = tk.Button(f4, text="1", width=7, command=self.one)
        self.one.pack(side=tk.LEFT)
        self.two = tk.Button(f4, text="2", width=7, command=self.two)
        self.two.pack(side=tk.LEFT)
        self.three = tk.Button(f4, text="3", width=7, command=self.three)
        self.three.pack(side=tk.LEFT)
        self.add = tk.Button(f4, text="+", width=7, command=self.add)
        self.add.pack(side=tk.LEFT)
        f4.pack()

        f5 = tk.Frame(self)
        self.zero = tk.Button(f5, text="0", width=15, command=self.zero)
        self.zero.pack(side=tk.LEFT)
        self.decimal = tk.Button(f5, text=".", width=7, command=self.decimal)
        self.decimal.pack(side=tk.LEFT)
        self.equals = tk.Button(f5, text="=", width=7, command=self.equals)
        self.equals.pack(side=tk.LEFT)
        f5.pack()

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()





app = Calculator()
app.master.title('Simple Calculator')
app.mainloop()