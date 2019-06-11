import tkinter as tk
from tkinter import messagebox
mainWindow=tk.Tk()
mainWindow.title("calculator")

heading_label1 = tk.Label(mainWindow,text="first number")
heading_label1.pack()

first_number=tk.Entry(mainWindow)
first_number.pack()

heading_label2= tk.Label(mainWindow,text="second number")
heading_label2.pack()


second_number=tk.Entry(mainWindow)
second_number.pack()


operations=tk.Label(mainWindow,text="operations")
operations.pack()

def addition():
    number1=int(first_number.get())
    number2=int(second_number.get())
    add=number1+number2
    print(add)

def subtraction():
    number1=int(first_number.get())
    number2=int(second_number.get())
    sub=number1-number2
    print(sub)

def multiply():
    number1=int(first_number.get())
    number2=int(second_number.get())
    mul=number1*number2
    print(mul)

def division():
    number1=int(first_number.get())
    number2=int(second_number.get())
    try :
        div = (number1 / number2)
        print(div)
    except ZeroDivisionError:
        messagebox.showerror("error", "cannot divide by 0.")




add_button=tk.Button(mainWindow,text='+',command=lambda:addition())
add_button.pack()

sub_button=tk.Button(mainWindow,text='-',command=lambda:subtraction())
sub_button.pack()

mul_button=tk.Button(mainWindow,text='*',command=lambda:multiply())
mul_button.pack()

div_button=tk.Button(mainWindow,text='/',command=lambda:division())
div_button.pack()

result_label=tk.Label(mainWindow,text="operations result is:")
result_label.pack()

mainWindow.mainloop()








