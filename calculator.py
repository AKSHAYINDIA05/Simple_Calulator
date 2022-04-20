from tkinter import *

root = Tk()
root.title("Calculator")

number = Entry(root, width=50, borderwidth=5)
number.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

def button_click(num):
    current = number.get()
    number.delete(0, END)
    number.insert(0, str(current) + str(num))


def button_clear_fun():
    number.delete(0, END)
    

def button_add():
    first_number = number.get()
    global f_num 
    global operation
    operation = "addition"
    f_num = int(first_number)
    number.delete(0, END)



def button_subtract():
    first_number = number.get()
    global f_num 
    global operation
    operation = "subtraction"
    f_num = int(first_number)
    number.delete(0, END)


def button_multiplication():
    first_number = number.get()
    global f_num 
    global operation
    operation = "mulitplication"
    f_num = int(first_number)
    number.delete(0, END)


def button_division():
    first_number = number.get()
    global f_num 
    global operation
    operation = "division"
    f_num = int(first_number)
    number.delete(0, END)

def button_equal_fun():
    second_number = number.get()
    number.delete(0, END)
    if operation == "addition":
        number.insert(0, f_num + int(second_number))
    if operation == "subtraction":
        number.insert(0, f_num - int(second_number))
    if operation == "multiplication":
       number.insert(0, f_num * int(second_number))
    if operation == "division":
        number.insert(0, f_num / int(second_number))
    





button_1 = Button(root, text="1", padx=30, pady=30, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=30, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=30, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=30, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=30, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=30, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=30, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=30, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=30, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=30, command=lambda: button_click(0))
button_sum = Button(root, text="+", padx=30, pady=30, command = button_add)
button_sub = Button(root, text="-", padx=30, pady=30, command= button_subtract)
button_mul = Button(root, text="*", padx=30, pady=30, command= button_multiplication)
button_div = Button(root, text="/", padx=30, pady=30, command= button_division)
button_equal = Button(root, text="=", padx=30, pady=30, command=button_equal_fun)
button_clear = Button(root, text="CLEAR", padx=30, pady=30, command=lambda: button_clear_fun())




button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_sum.grid(row=1, column=4)
button_sub.grid(row=2, column=4)
button_mul.grid(row=3, column=4)
button_div.grid(row=4, column=4)
button_equal.grid(row=4, column=2)
button_clear.grid(row=0, column=4)




root.mainloop()