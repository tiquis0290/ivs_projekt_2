import tkinter as tk
from logic import calculate

def info():
    root2 = tk.Tk()
    root2.title("Info")
    label = tk.Label(root2, text="to be worked on")
    label.grid(row=0, column=0)
    root2.mainloop()
    

bracket = 0
absolute = 0
operators = ""


root = tk.Tk()
root.title("Calculator")


text = tk.StringVar()
text.set("")

def addnumber(char):
    global operators
    if len(operators) != 0 and operators[-1] == "2":
        text.set(text.get() + "*")
    if char == ".":
        operators += "0"
        text.set(text.get() + "0")

    operators += "0"
    text.set(text.get() + char)

def addoperator(char):
    global operators
    if len(operators) > 0 and operators[-1] != "3":
        if operators[-1] == "1":
            if len(operators) > 1 and operators[-2] != "3":
                text.set(text.get()[:-1] + char)
        else:
            text.set(text.get() + char)
            operators += "1"
    elif char == "-":
        text.set(text.get() + "0" +char)
        operators += "01"

def addbracket(char):
    global bracket
    global operators
    if len(operators) != 0 or char != "^": 
        if len(operators) > 0 and (operators[-1] == "0" or operators[-1] == "2"):
            text.set(text.get() + "*")
            operators += "1"

        if char != "":
            operators += "3"
        bracket += 1
        text.set(text.get() + char + "(")
        operators += "3"

def endbracket():
    global bracket
    global operators
    if len(operators) > 0 and operators[-1] == "0" and bracket > 0:
        bracket -= 1
        operators += "2"
        text.set(text.get() + ")")
    
def addabs():
    global absolute
    global bracket
    global operators
    if len(text.get()) > 0 and text.get()[-1] == ")" and absolute > 0:
        operators += "2"
        text.set(text.get() + "|")
        absolute -= 1
    else:
        if len(operators) > 0 and (operators[-1] == "0" or operators[-1] == "2"):
            text.set(text.get() + "*")
            operators += "1"
        text.set(text.get() + "|(")
        absolute += 1
        bracket += 1
        operators += "33"

def c():
    global absolute
    global bracket
    global operators

    if text.get()[-1] == "|":
        absolute += 1
    
    if text.get()[-1] == ")":
        bracket += 1

    if text.get()[-1] == "(":
        bracket -= 1
        if len(text.get()) > 1 and text.get()[-2] not in  "-+*/":
            absolute -= 1
            text.set(text.get()[:-1])
            operators = operators[:-1]
    
    text.set(text.get()[:-1])
    operators = operators[:-1]


def ce():
    global absolute
    global bracket
    global operators
    operators = ""
    absolute = 0
    bracket = 0
    text.set("")

def solve():
    global absolute
    global bracket
    if absolute == 0 and bracket == 0:
        try:
            text.set(calculate(text.get()))
            print(operators)
        except(e):
            text.set("error")
    else:
        text.set("Syntax error")

button = tk.Button(root, text="Information", font=("Arial", 10), padx=20, pady=10, command=info)
button.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

label = tk.Label(root, textvariable= text, font=("Arial", 30), height=2, bg="lightgray", anchor="w")
label.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nesw")

button = tk.Button(root, text="CE", font=("Arial", 18), padx=20, pady=10, command=ce)
button.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="C", font=("Arial", 18), padx=20, pady=10, command=c)
button.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="^", font=("Arial", 18), padx=20, pady=10, command=lambda: addbracket('^'))
button.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="√", font=("Arial", 18), padx=20, pady=10, command=lambda: addbracket('√'))
button.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="(", font=("Arial", 18), padx=20, pady=10, command=lambda: addbracket(''))
button.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text=")", font=("Arial", 18), padx=20, pady=10, command=lambda: endbracket())
button.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="/", font=("Arial", 18), padx=20, pady=10, command=lambda: addoperator('/'))
button.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="*", font=("Arial", 18), padx=20, pady=10, command=lambda: addoperator('*'))
button.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="7", font=("Arial", 18), padx=20, pady=10, command=lambda: addnumber('7'))
button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="8", font=("Arial", 18), padx=20, pady=10, command=lambda: addnumber('8'))
button.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="9", font=("Arial", 18), padx=20, pady=10, command=lambda: addnumber('9'))
button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="-", font=("Arial", 18), padx=20, pady=10, command=lambda: addoperator('-'))
button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="4", font=("Arial", 18), padx=20, pady=10, command=lambda: addnumber('4'))
button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="5", font=("Arial", 18), padx=20, pady=10, command=lambda: addnumber('5'))
button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="6", font=("Arial", 18), padx=20, pady=10, command=lambda: addnumber('6'))
button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="+", font=("Arial", 18), padx=20, pady=10, command=lambda: addoperator('+'))
button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="1", font=("Arial", 18), padx=20, pady=10, command=lambda: addnumber('1'))
button.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="2", font=("Arial", 18), padx=20, pady=10, command=lambda: addnumber('2'))
button.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="3", font=("Arial", 18), padx=20, pady=10, command=lambda: addnumber('3'))
button.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="=", font=("Arial", 18), padx=20, pady=10, command=solve)
button.grid(row=6, column=3, rowspan=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="|x|", font=("Arial", 18), padx=20, pady=10, command=lambda: addabs())
button.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="0", font=("Arial", 18), padx=20, pady=10, command=lambda: addnumber('0'))
button.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text=".", font=("Arial", 18), padx=20, pady=10, command=lambda: addnumber('.'))
button.grid(row=7, column=2, padx=5, pady=5, sticky="nsew")

root.mainloop()
