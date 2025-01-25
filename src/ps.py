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

variables = {}  # Dictionary to store variables
functions = {}  # Dictionary to store functions
windows = {}  # Dictionary to store created windows

# Function to create window
def cw(wtitle, geo):  
    window = Tk()
    window.title(wtitle)  
    window.geometry(geo)  
    return window

# Function to handle window loop
def wl(wname):  
    if wname in windows:  
        windows[wname].mainloop()  
    else:
        print(f"Error: Window '{wname}' not found.")

# Function to create or assign variable
def cv(var, val):  
    global variables  
    variables[var] = val  

# Function to open URL
def wo(url):  
    webbrowser.open(url)

# Function to show message box
def mb(type, title, message):  
    method_name = "show" + type  
    method = getattr(messagebox, method_name, None)
    if method:
        method(title, message)
    else:
        print(f"Error: '{method_name}' is not a valid messagebox type.")

# Function to print a value (or variable)
def pln(l):  
    if l in variables:
        print(variables[l])  
    else:
        print(l)  

# Function to get input from the user
def iln(prompt):  
    value = input(prompt)  
    return value

# Function to handle if statements
def if_stmt(var, value, code_if, code_else=None):  
    global variables  
    if var in variables and variables[var] == value:
        for line in code_if:
            exec(line, globals())
    elif code_else:
        for line in code_else:
            exec(line, globals())

# Function to execute the main code
def execute_main(code):  
    for line in code.splitlines():
        stripped_line = line.strip()
        if "//" in stripped_line:
            stripped_line = stripped_line.split("//", 1)[0].strip()  # Remove inline comments
        if stripped_line == "":
            continue  
        try:
            if stripped_line.split('(')[0] in dir(PustInterpreter):  
                exec(f"ps.{stripped_line}", globals())
            else:
                exec(stripped_line, globals())
        except Exception as e:
            print(f"Error in mainspace: {e}")

# Function to define a function
def fn(name=None, code=None):  
    if name and code:
        lines = [line.strip() for line in code.strip().splitlines() if line.strip()]
        functions[name] = lines  
        if name == "main":  
            execute_main(code)
    elif name:
        if name in functions:
            for line in functions[name]:
                execute_main(line)
        else:
            print(f"Function '{name}' is not defined.")

# Alias the functions for mainspace and non-mainspace use
class PustInterpreter:
    cv = staticmethod(cv)
    wo = staticmethod(wo)
    pln = staticmethod(pln)
    iln = staticmethod(iln)
    fn = staticmethod(fn)
    if_stmt = staticmethod(if_stmt)
    mb = staticmethod(mb)
    wl = staticmethod(wl)

# Create an instance for non-mainspace use
ps = PustInterpreter()
