import tkinter as tk
def click(event):
    current = str(entry.get())
    button_text = event.widget["text"]
    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)
# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)
entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)
# Define button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]
# Create button grid
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font=("Arial", 18), height=2, width=6)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", click)
root.mainloop()