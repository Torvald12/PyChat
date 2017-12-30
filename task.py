from tkinter import *

def f2c_count():
    frh = entry1.get()
    cls = (int(frh) - 32)/1.8
    task1.delete(0.0, END)
    task1.insert(0.0, cls)

def factorial():
    num = int(entry2.get())
    fact = 1
    for i in range(0, num):
        fact = fact * (i + 1)
    task2.delete(0.0, END)
    task2.insert(0.0, fact)

def fib():
    nf = int(entry3.get())
    fib1 = fib2 = 1
    i = 2
    fib_sum = 1
    while i < nf:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1
    task3.delete(0.0, END)
    task3.insert(0.0, fib_sum)


root = Tk()
root.title("Pusya's Task")
root.geometry("400x300")

app = Frame(root)
app.grid()

lbl = Label(app, text = "Hello, Pusyanya!:*")
lbl.grid()

lbl1 = Label(app, text = "Температура по Фаренгейту: ")
lbl1.grid()

entry1 = Entry(app)
entry1.grid()

bttn1 = Button(app, text = "Узнать температуру по Цельсию!", command = f2c_count)
bttn1.grid()

task1 = Text(app, width = 15, height = 1, wrap = NONE)
task1.grid()

lbl2 = Label(app, text = "Число для вычисления его факториала: ")
lbl2.grid()

entry2 = Entry(app)
entry2.grid()

bttn2 = Button(app, text = "Узнать факториал!", command = factorial)
bttn2.grid()

task2 = Text(app, width = 15, height = 1, wrap = NONE)
task2.grid()

lbl3 = Label(app, text = "Порядковый номер числа в ряду Фибоначчи: ")
lbl3.grid()

entry3 = Entry(app)
entry3.grid()

bttn3 = Button(app, text = "Узнать число!", command = fib)
bttn3.grid()

task3 = Text(app, width = 15, height = 1, wrap = NONE)
task3.grid()

root.mainloop()
