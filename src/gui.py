import tkinter as tk
from logic import calculate

def info():
    root2 = tk.Tk()
    root2.title("Info")
    label = tk.Label(root2, text="to be worked on")
    label.grid(row=0, column=0)
    root2.mainloop()
    



root = tk.Tk()
root.title("Calculator")


text = tk.StringVar()
text.set("")

def addchar(char):
    text.set(text.get() + char)

def c():
    text.set(text.get()[:-1])

def ce():
    text.set("")

def solve():
    text.set(calculate(text.get()))

button = tk.Button(root, text="Information", font=("Arial", 10), padx=20, pady=10, command=info)
button.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

label = tk.Label(root, textvariable= text, font=("Arial", 30), height=2, bg="lightgray", anchor="w")
label.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nesw")

button = tk.Button(root, text="CE", font=("Arial", 18), padx=20, pady=10, command=ce)
button.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="C", font=("Arial", 18), padx=20, pady=10, command=c)
button.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="^", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('^'))
button.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="√", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('√('))
button.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="(", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('('))
button.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text=")", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar(')'))
button.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="/", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('/'))
button.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="*", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('*'))
button.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="7", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('7'))
button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="8", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('8'))
button.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="9", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('9'))
button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="-", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('-'))
button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="4", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('4'))
button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="5", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('5'))
button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="6", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('6'))
button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="+", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('+'))
button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="1", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('1'))
button.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="2", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('2'))
button.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="3", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('3'))
button.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="=", font=("Arial", 18), padx=20, pady=10, command=solve)
button.grid(row=6, column=3, rowspan=2, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="|x|", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('|'))
button.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text="0", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('0'))
button.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")

button = tk.Button(root, text=".", font=("Arial", 18), padx=20, pady=10, command=lambda: addchar('.'))
button.grid(row=7, column=2, padx=5, pady=5, sticky="nsew")

root.mainloop()
