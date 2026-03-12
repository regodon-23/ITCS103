import tkinter as beach
window = beach.Tk()
window.title("Giana Andrea")
window.configure(bg = "light blue")
label = beach.Label(window, text = "Simple Calculator", font = ("times new roman", 15, "bold"),bg = "light blue", fg = "pink")
label.grid(column = 0, row = 0, padx = 50, pady = 10, columnspan = 3)

def pasay():
    num1 = int(first_entry.get())
    num2 = int(sec_entry.get())
    sum = num1 + num2
    label = beach.Label(window, text = f"The sum of {num1} and {num2} is {sum}.", font = ("times new roman", 15, "bold"), bg = "light blue", fg = "black")
    label.grid(column = 0, row = 0, columnspan = 3)
def gulat():
    num1 = int(first_entry.get())
    num2 = int(sec_entry.get())
    dif = num1 - num2
    label = beach.Label(window, text = f"The difference of {num1} and {num2} is {dif}.", font = ("times new roman", 15, "bold"), bg = "light blue", fg = "black")
    label.grid(column = 0, row = 0, columnspan = 3)
def muting():
    num1 = int(first_entry.get())
    num2 = int(sec_entry.get())
    prod = num1 * num2
    label = beach.Label(window, text = f"The product of {num1} and {num2} is {prod}.", font = ("times new roman", 15, "bold"), bg = "light blue", fg = "black")
    label.grid(column = 0, row = 0, columnspan = 3)
def kahel():
    num1 = int(first_entry.get())
    num2 = int(sec_entry.get())
    quot = num1 / num2
    label = beach.Label(window, text = f"The quotient of {num1} and {num2} is {quot}.", font = ("times new roman", 15, "bold"), bg = "light blue", fg = "black")
    label.grid(column = 0, row = 0, columnspan = 3)

first = beach.Label(window, text = "Enter a number:", font = ("times new roman", 15), bg = "light blue", )
first.grid(column = 0, row = 1)
first_entry = beach.Entry(window, width = 20)
first_entry.grid(column = 1, row = 1, columnspan = 2)
sec = beach.Label(window, text = "Enter a number:", font = ("times new roman", 15), bg = "light blue", )
sec.grid(column = 0, row = 2)
sec_entry = beach.Entry(window, width = 20)
sec_entry.grid(column = 1, row = 2, columnspan = 2)

add_btn = beach.Button(window, text = "ADDITION", width = 10, bg = "purple", command = pasay)
add_btn.grid(column = 0, row = 3, pady = 10)
sub_btn = beach.Button(window, text = "SUBTRACTION", width = 10, bg = "purple", command = gulat)
sub_btn.grid(column = 1, row = 3, pady = 10)
mul_btn = beach.Button(window, text = "MULTIPLICATION", width = 10, bg = "purple", command = muting)
mul_btn.grid(column = 0, row = 4, pady = 10)
div_btn = beach.Button(window, text = "DIVISION", width = 10, bg = "purple", command = kahel)
div_btn.grid(column = 1, row = 4, pady = 10)

window.mainloop()