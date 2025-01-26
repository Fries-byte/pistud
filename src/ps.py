import webbrowser  # Importing webbrowser to open sites
from tkinter import messagebox  # Importing messagebox to give info, warning, error
from tkinter import *  # Importing tkinter for software builder

# =--=--=--=--=--=--=--=--=--=--=--=--=
# Pust's Interpreter source
# Created by Pust-Lang (GitHub)
# and written by Fries-byte (GitHub)
# Learn more on our website or README.md
#
# 2025 - presents | The Programming Language Pust
# =--=--=--=--=--=--=--=--=--=--=--=--=

variables = {}
functions = {}
windows = {}
buttons = {}

def cw(wtitle, geo):  # Create a window
    window = Tk()
    window.title(wtitle)
    window.geometry(geo)
    windows[wtitle] = window
    return window

def ct(windowname, geo, text):  # Create text in a window
    if windowname in windows:
        window = windows[windowname]
        x, y = map(int, geo.split('x'))
        label = Label(window, text=text)
        label.place(x=x, y=y)
    else:
        print(f"Error: Window '{windowname}' not found.")

def wl(wname):  # Start window loop
    if wname in windows:
        windows[wname].mainloop()
    else:
        print(f"Error: Window '{wname}' not found.")

def cv(var, val):  # Create variable
    if isinstance(val, Tk):
        windows[var] = val
    else:
        variables[var] = val

def wo(url):  # Open a website
    webbrowser.open(url)

def mb(type, title, message): # Define message box
    method_name = "show" + type # Includes "show"
    method = getattr(messagebox, method_name, None)
    if method:
        method(title, message)
    else:
        print(f"Error: '{method_name}' is not a valid messagebox type.")


def pln(l):  # Print a line
    if l in variables:
        print(variables[l])
    else:
        print(l)

def iln(prompt):  # Input line
    return input(prompt)

def if_stmt(var, value, code_if, code_else=None):
    if var in variables:
        if variables[var] == value:
            try:
                for line in code_if:
                    if callable(line):  # Check if it's a callable
                        line()
                    else:
                        exec(line.strip(), globals())
            except Exception as e:
                print(f"Error in if condition block: {e}")
        elif code_else:
            try:
                for line in code_else:
                    if callable(line):
                        line()
                    else:
                        exec(line.strip(), globals())
            except Exception as e:
                print(f"Error in else condition block: {e}")
    else:
        print(f"Error: Variable '{var}' not found.")

def cb(windowname, geo, size, name):  # Define create button
    if windowname in windows:
        window = windows[windowname]
        x, y = map(int, geo.split(','))  # Extract x and y coordinates
        width, height = map(int, size.split(','))  # Extract width and height
        button = Button(window, text=name)
        button.place(x=x, y=y, width=width, height=height)
        windows[f"{windowname}_{name}_button"] = button  # Store button for reference
    else:
        print(f"Error: Window '{windowname}' not found.")

def bc(name, code):  # Define button click
    # Find the button in the stored windows
    for key, button in windows.items():
        if key.endswith(f"_{name}_button"):  # Match button by name
            # Bind the click event to execute the provided code
            def on_click():
                for line in code:
                    line = line.strip()
                    if line.startswith("fn("):  # Ensure only functions are executed
                        func_name = line[3:-1]  # Extract function name
                        if func_name in functions:
                            for func_line in functions[func_name]:
                                exec(func_line.strip(), globals())
                        else:
                            print(f"Error: Function '{func_name}' not found.")
                    else:
                        print(f"Error: Invalid code '{line}'.")
            button.config(command=on_click)  # Bind the click handler to the button
            print(f"Click event bound to button '{name}'.")
            return
    print(f"Error: Button '{name}' not found.")

def execute_main(code):  # Execute mainspace code
    for line in code.splitlines():
        stripped_line = line.strip()
        if "//" in stripped_line:
            stripped_line = stripped_line.split("//", 1)[0].strip()
        if stripped_line == "":
            continue
        try:
            exec(stripped_line, globals())
        except Exception as e:
            print(f"Error in mainspace: {e}")

def fn(name=None, code=None):  # Define functions
    if name and code:
        lines = [line.strip() for line in code.strip().splitlines() if line.strip()]
        functions[name] = lines
        if name == "main":
            execute_main(code)
    elif name in functions:
        for line in functions[name]:
            exec(line.strip(), globals())
    else:
        print(f"Function '{name}' not found.")

class PustInterpreter:
    cv = staticmethod(cv)
    wo = staticmethod(wo)
    pln = staticmethod(pln)
    iln = staticmethod(iln)
    fn = staticmethod(fn)
    if_stmt = staticmethod(if_stmt)
    mb = staticmethod(mb)
    wl = staticmethod(wl)
    cb = staticmethod(cb)

ps = PustInterpreter()
