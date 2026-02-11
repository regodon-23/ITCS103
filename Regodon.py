import tkinter as tk

#create main window
window = tk.Tk()
window.title("My Profile")
window.geometry("600x600")
window.resizable(False, True)
 
title_Label = tk.Label(window,text='My Profile',font=('Serif',30,'bold'),fg="green",bg='blue',anchor='center')
title_Label.pack(padx=10,pady=10)

tk.Label(window,text="Name: Gian Andrei Regodon",font='20',anchor="w").pack(fill="x",padx=20,pady=5)
tk.Label(window,text="Age: 18",font='20',anchor="w").pack(fill="x",padx=20,pady=5)
tk.Label(window,text="Course: BSIT-1A",font='20',anchor="w").pack(fill="x",padx=20,pady=5)
tk.Label(window,text="Birthday: February 23, 2007",font='20',anchor="w").pack(fill="x",padx=20,pady=5)
tk.Label(window,text="Motto: Be happy for what you have while working for what you want",font='20',anchor="w").pack(fill="x",padx=20,pady=5)

window.mainloop()