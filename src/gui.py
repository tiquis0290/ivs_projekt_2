import tkinter as tk
import libs.calc_mathlib as math

def info():
    root2 = tk.Tk()
    root2.title("Info")
    label = tk.Label(root2, text="Vitajte v kalkulačke!\nTáto kalkulačka je navrhnutá na základe Pythonu a používa knižnicu tkinter na tvorbu grafického rozhrania. Podporuje nasledujúce operácie:\n\nSčítanie: Zadajte dve čísla a stlačte tlačidlo '+' alebo klávesovú skratku '+'.\nOdčítanie: Zadajte dve čísla a stlačte tlačidlo '-' alebo klávesovú skratku '-'.\nNásobenie: Zadajte dve čísla a stlačte tlačidlo '*' alebo klávesovú skratku '*'.\nDelenie: Zadajte dve čísla a stlačte tlačidlo '/' alebo klávesovú skratku '/'.\nMocnenie: Zadajte základ, stlačte tlačidlo '^' a zadajte exponent.\nOdmocnina: Zadajte základ, stlačte tlačidlo 'y√x' a zadajte index.\nAbsolútna hodnota: Zadajte číslo a stlačte tlačidlo '|x|'.\nFaktoriál: Zadajte číslo a stlačte tlačidlo '!'.\n\nPoužite tieto tlačidlá alebo klávesové skratky na vykonávanie operácií a výpočtov.\n\nĎakujeme, že používate našu kalkulačku!", justify="left")
    label.grid(row=0, column=0)
    root2.mainloop()
    



root = tk.Tk()
root.title("Calculator")

x = ""
operation = ""
next_operation = ""
y = ""


text = tk.StringVar()

def setText():
    global x
    global y
    global operation
    if operation == "√":
        text.set(str(y) + "|" + str(operation) + str(x))
    else:
        text.set(str(x) + str(operation) + str(y) + "|")

def fnegate():
    global y
    global x
    if y == "":
        x = math.mul(float(x),-1)
        if int(x) == x:
            x = int(x)
    else:
        y = math.mul(float(y),-1)
        if int(y) == y:
            y = int(y)
    setText()

def addchar(char):
    global x
    global y
    global operation
    if operation == "":
        if char != "." or "." not in str(x):
            x = str(x)
            x += char
    else:
        if char != "." or "." not in str(y):
            y = str(y)
            y += char
    setText()

def twoOperation(char):
    global x
    global y
    global operation
    global next_operation
    if operation != "":
        if y == "":
            operation = char
            setText()
        else:
            next_operation = char
            solve()
    else:
        try:
            x = float(y)
        except:
            x = float(x)
        if int(x) == x:
            x = int(x)
        y = ""
        operation = char
        setText()

def ce():
    global x
    global y
    global operation
    if y != "":
        y = str(y)[:-1]
        setText()
    else:
        c()

def c():
    global x
    global y
    global operation
    x = ""
    y = ""
    operation = ""
    setText()

def oneOperation(char):
    global x 
    global y
    global operation
    if operation != "" and y != "":
            solve()
    try:
        x = float(y)
    except:
        x = float(x)
    if int(x) == x:
        x = int(x)
    y = 0
    operation = char
    solve()

def solve():
    global x
    global y
    global operation
    global next_operation
    if y != "":
        y = float(y)
    else:
        y = 0
    if  x != "":
        x = float(x)
    else:
        x = 0
    if operation == "":
        operation = "+"
    print(x, operation, y)
    try:
        if operation == "+":
            result = math.add(x, y)
        elif operation == "-":
            result = math.sub(x, y)
        elif operation == "*":
            result = math.mul(x, y)
        elif operation == "/":
            result = math.div(x, y)
        elif operation == "^":
            result = math.pow(x, y)
        elif operation == "√":
            result = math.root(x,y)
        elif operation == "|":
            result = math.abs(x)
        elif operation == "!":
            if int(x) == x:
                x = int(x)
            if isinstance(x, int) or x < 0:
                try:
                    result = math.fac(x)
                except:
                    c()
                    text.set("Error: number too large")
            else:
                c()
                text.set("Error: number must be whole and positive")
        else:
            result = y
        print(result)
        y = ""
        if int(result) == result:
            result = int(result)
        x = str(result)
        operation = next_operation
        next_operation = ""
        setText()
    except:
        c()
        text.set("Error: math library failed")



setText()

button = tk.Button(root, text="info", font=("Arial", 18), padx=0, pady=0, command=lambda: info())
button.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

label = tk.Label(root, textvariable= text, font=("Arial", 30), height=2, bg="lightgray", anchor="w")
label.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nesw")

button = tk.Button(root, text="CE", font=("Arial", 18), padx=20, pady=10, command=ce)
button.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="C", font=("Arial", 18), padx=20, pady=10, command=c)
button.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="^", font=("Arial", 18), padx=20, pady=10, command=lambda: twoOperation('^'))
button.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="y√x", font=("Arial", 18), padx=20, pady=10, command=lambda: twoOperation('√'))
button.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="|x|", font=("Arial", 18), padx=20, pady=10, command=lambda: oneOperation('|'))
button.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="!", font=("Arial", 18), padx=20, pady=10, command=lambda: oneOperation('!'))
button.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="/", font=("Arial", 18), padx=20, pady=10, command=lambda: twoOperation('/'))
button.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="*", font=("Arial", 18), padx=20, pady=10, command=lambda: twoOperation('*'))
button.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="7", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('7'))
button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="8", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('8'))
button.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="9", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('9'))
button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="-", font=("Arial", 18), padx=20, pady=10, command=lambda: twoOperation('-'))
button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="4", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('4'))
button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="5", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('5'))
button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="6", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('6'))
button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="+", font=("Arial", 18), padx=20, pady=10, command=lambda: twoOperation('+'))
button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="1", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('1'))
button.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="2", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('2'))
button.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="3", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('3'))
button.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="=", font=("Arial", 18), padx=20, pady=10, command=solve)
button.grid(row=6, column=3, rowspan=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="+/-", font=("Arial", 18), padx=20, pady=10, command=lambda: fnegate())
button.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="0", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('0'))
button.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text=".", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('.'))
button.grid(row=7, column=2, padx=5, pady=5, sticky="nsew")

root.bind('<Delete>', lambda event: c())
root.bind('<BackSpace>', lambda event: ce())

root.bind('<KeyPress-0>', lambda event: addchar('0'))
root.bind('<KeyPress-1>', lambda event: addchar('1'))
root.bind('<KeyPress-2>', lambda event: addchar('2'))
root.bind('<KeyPress-3>', lambda event: addchar('3'))
root.bind('<KeyPress-4>', lambda event: addchar('4'))
root.bind('<KeyPress-5>', lambda event: addchar('5'))
root.bind('<KeyPress-6>', lambda event: addchar('6'))
root.bind('<KeyPress-7>', lambda event: addchar('7'))
root.bind('<KeyPress-8>', lambda event: addchar('8'))
root.bind('<KeyPress-9>', lambda event: addchar('9'))

root.bind('<KeyPress-plus>', lambda event: twoOperation('+'))
root.bind('<KeyPress-minus>', lambda event: twoOperation('-'))
root.bind('<KeyPress-asterisk>', lambda event: twoOperation('*'))
root.bind('<KeyPress-slash>', lambda event: twoOperation('/'))
root.bind('<KeyPress-Return>', lambda event: solve())
root.bind('<KeyPress-period>', lambda event: addchar('.'))
root.bind('<KeyPress-comma>', lambda event: addchar('.'))

root.mainloop()