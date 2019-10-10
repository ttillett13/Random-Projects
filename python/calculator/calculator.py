import tkinter as tk
from tkmacosx import Button


class Calculator(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    lhs = 0
    rhs = ""
    total = 0
    operand = None
    small_width = 55
    large_width = 110
    height = 60
    result_font = ("Helvetica", 50)
    label_font = 10


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
            self.rhs = self.total
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

    def makeButton(self, frame, text, width, height, command, bg, fg):
#        self.button = tk.Button(frame, text=text, width=width, command=command, highlightbackground=bg, fg=fg)
        self.button = Button(frame, text=text, width=width, height=height, command=command, bg=bg, fg=fg)
        self.button.pack(side=tk.LEFT)

    def createWidgets(self):
        print(self.winfo_geometry())
        self.result = tk.Label(self, text="0",anchor=tk.E, font=self.result_font, bg="#3C3C3C", fg="#D4D4D2")
        self.result.pack(fill="both", expand=1)

        f1 = tk.Frame(self)
        self.makeButton(f1, "C", self.small_width, self.height, self.clear, "#696969", "#D4D4D2")
        self.makeButton(f1, "+/-", self.small_width, self.height, self.togglepm, "#696969", "#D4D4D2")
        self.makeButton(f1, "%", self.small_width, self.height, self.percent, "#696969", "#D4D4D2")
        self.makeButton(f1, "/", self.small_width, self.height, lambda x="divide": self.operator(x), "#FF9500", "#D4D4D2")
        f1.pack(fill="both", expand=1)

        f2 = tk.Frame(self)
        self.makeButton(f2, "7", self.small_width, self.height, lambda x="7": self.digit(x), "#8C8C8C", "#D4D4D2")
        self.makeButton(f2, "8", self.small_width, self.height, lambda x="8": self.digit(x), "#8C8C8C", "#D4D4D2")
        self.makeButton(f2, "9", self.small_width, self.height, lambda x="9": self.digit(x), "#8C8C8C", "#D4D4D2")
        self.makeButton(f2, "X", self.small_width, self.height, lambda x="multiply": self.operator(x), "#FF9500", "#D4D4D2")
        f2.pack(fill="both", expand=1)

        f3 = tk.Frame(self)
        self.makeButton(f3, "4", self.small_width, self.height, lambda x="4": self.digit(x), "#8C8C8C", "#D4D4D2")
        self.makeButton(f3, "5", self.small_width, self.height, lambda x="5": self.digit(x), "#8C8C8C", "#D4D4D2")
        self.makeButton(f3, "6", self.small_width, self.height, lambda x="6": self.digit(x), "#8C8C8C", "#D4D4D2")
        self.makeButton(f3, "-", self.small_width, self.height, lambda x="subtract": self.operator(x), "#FF9500", "#D4D4D2")
        f3.pack(fill="both", expand=1)

        f4 = tk.Frame(self)
        self.makeButton(f4, "1", self.small_width, self.height, lambda x="1": self.digit(x), "#8C8C8C", "#D4D4D2")
        self.makeButton(f4, "2", self.small_width, self.height, lambda x="2": self.digit(x), "#8C8C8C", "#D4D4D2")
        self.makeButton(f4, "3", self.small_width, self.height, lambda x="3": self.digit(x), "#8C8C8C", "#D4D4D2")
        self.makeButton(f4, "+", self.small_width, self.height, lambda x="add": self.operator(x), "#FF9500", "#D4D4D2")
        f4.pack(fill="both", expand=1)

        f5 = tk.Frame(self)
        self.makeButton(f5, "0", self.large_width, self.height, lambda x="0": self.digit(x), "#8C8C8C", "#D4D4D2")
        self.makeButton(f5, ".", self.small_width, self.height, lambda x=".": self.digit(x), "#8C8C8C", "#D4D4D2")
        self.makeButton(f5, "=", self.small_width, self.height, self.equals, "#FF9500", "#D4D4D2")
        f5.pack(fill="both", expand=1)

        #self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        #self.quitButton.pack()


app = Calculator()
app.master.title('Simple Calculator')
app.master.geometry("%dx%d%+d%+d" % (220, 365, 250, 125))
app.mainloop()