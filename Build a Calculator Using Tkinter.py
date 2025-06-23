import tkinter as tk

# Function to update the expression
def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the expression
def button_clear():
    global expression
    expression = ""
    input_text.set(expression)

# Function to evaluate the expression
def button_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result  # To allow chaining of operations
    except:
        input_text.set("Error")
        expression = ""

# Main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

expression = ""
input_text = tk.StringVar()

# Input field
input_frame = tk.Frame(window, bd=2, relief=tk.RIDGE)
input_frame.pack(pady=10)

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18), justify='right', bd=5, relief=tk.RIDGE)
input_field.pack(ipady=10, ipadx=5)

# Buttons frame
btns_frame = tk.Frame(window)
btns_frame.pack()

# First row
tk.Button(btns_frame, text='7', width=5, height=2, command=lambda: button_click(7)).grid(row=0, column=0)
tk.Button(btns_frame, text='8', width=5, height=2, command=lambda: button_click(8)).grid(row=0, column=1)
tk.Button(btns_frame, text='9', width=5, height=2, command=lambda: button_click(9)).grid(row=0, column=2)
tk.Button(btns_frame, text='/', width=5, height=2, command=lambda: button_click('/')).grid(row=0, column=3)

# Second row
tk.Button(btns_frame, text='4', width=5, height=2, command=lambda: button_click(4)).grid(row=1, column=0)
tk.Button(btns_frame, text='5', width=5, height=2, command=lambda: button_click(5)).grid(row=1, column=1)
tk.Button(btns_frame, text='6', width=5, height=2, command=lambda: button_click(6)).grid(row=1, column=2)
tk.Button(btns_frame, text='*', width=5, height=2, command=lambda: button_click('*')).grid(row=1, column=3)

# Third row
tk.Button(btns_frame, text='1', width=5, height=2, command=lambda: button_click(1)).grid(row=2, column=0)
tk.Button(btns_frame, text='2', width=5, height=2, command=lambda: button_click(2)).grid(row=2, column=1)
tk.Button(btns_frame, text='3', width=5, height=2, command=lambda: button_click(3)).grid(row=2, column=2)
tk.Button(btns_frame, text='-', width=5, height=2, command=lambda: button_click('-')).grid(row=2, column=3)

# Fourth row
tk.Button(btns_frame, text='0', width=5, height=2, command=lambda: button_click(0)).grid(row=3, column=0)
tk.Button(btns_frame, text='.', width=5, height=2, command=lambda: button_click('.')).grid(row=3, column=1)
tk.Button(btns_frame, text='=', width=5, height=2, command=button_equal).grid(row=3, column=2)
tk.Button(btns_frame, text='+', width=5, height=2, command=lambda: button_click('+')).grid(row=3, column=3)

# Clear button
tk.Button(window, text='Clear', width=22, height=2, command=button_clear).pack(pady=10)

window.mainloop()
