import tkinter as tk
def click(button):
    if button == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    elif button == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, button)
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
display = tk.Entry(window, font=("Arial", 20))
display.pack(fill="x", padx=10,pady=10)
buttons=[
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "C","0","=","+"
]
for button in buttons:
    tk.Button(
        window,
        text=button,
        font=("Arial", 18),
        command=lambda b=button: click(b)
    ).pack(side="left",padx=5,pady=5)
window.mainloop()
