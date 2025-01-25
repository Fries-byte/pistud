import webbrowser  # Importing webbrowser to open sites
from tkinter import messagebox  # Importing messagebox to give info, warning, error
from tkinter import *

# =--=--=--=--=--=--=--=--=--=--=--=--=
# Pust's Interpreter source
# Created by Pust-Lang (GitHub)
# and written by Fries-byte (GitHub)
# Learn more on our website or README.md
#
# 2025 - presents | The Programming Language Pust
# =--=--=--=--=--=--=--=--=--=--=--=--=

wname = None  # Global variable for window
variables = {}  # Dictionary to store variables
functions = {}  # Dictionary to store functions

def cw(wtitle, geo):  # Define create window
    # Create the window
    window = Tk()
    window.title(wtitle)  # Set the window's title
    window.geometry(geo)  # Set the window's geometry
    return window  # Return the created window instance

def ct(window, text_content):  # Define create text for the window
    # Add a Label widget with the provided text content
    label = Label(window, text=text_content, font=("Arial", 12))
    label.pack(pady=10)  # Pack with some padding for better layout
    return label  # Return the created Label widget

def wl(tname):  # Define window loop
    if tname == wname:  # Get the name
        wname.mainloop()  # Open the window

def cv(var, val):  # Define create variable
    global variables  # Ensure `variables` is globally accessible
    variables[var] = val  # Store the variable name and its value in the dictionary

def wo(url):  # Define web open
    webbrowser.open(url)

def mb(type, title, message):  # Define message box
    method_name = "show" + type  # Construct method name dynamically
    method = getattr(messagebox, method_name, None)
    if method:
        method(title, message)
    else:
        print(f"Error: '{method_name}' is not a valid messagebox type.")

def pln(l):  # Define print line
    if l in variables:
        print(variables[l])  # Print its value from the dictionary
    else:
        print(l)  # Print the value directly

def iln(prompt):  # Define input line
    value = input(prompt)  # Take input from the user
    return value

def if_stmt(var, value, code_if, code_else=None):  # Define input statement
    global variables  # Ensure `variables` is globally accessible
    if var in variables and variables[var] == value:
        for line in code_if:
            exec(f"p.{line.strip()}", globals())
    elif code_else:
        for line in code_else:
            exec(f"p.{line.strip()}", globals())

def execute_main(code):  # Define comments
    for line in code.splitlines():
        stripped_line = line.strip()
        if "//" in stripped_line:
            stripped_line = stripped_line.split("//", 1)[0].strip()  # Remove inline comments
        if stripped_line == "":
            continue  # Ignore blank lines
        try:
            if stripped_line.split('(')[0] in dir(PustInterpreter):  # Check if it matches Pust methods
                exec(f"p.{stripped_line}", globals())
            else:
                exec(stripped_line, globals())
        except Exception as e:
            print(f"Error in mainspace: {e}")  # Handle runtime errors gracefully

def fn(name=None, code=None):  # Define function
    if name and code:
        # Process multiline strings properly
        lines = [line.strip() for line in code.strip().splitlines() if line.strip()]
        functions[name] = lines  # Define the function
        if name == "main":  # Define mainspace
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
    ct = staticmethod(ct)
    wl = staticmethod(wl)

# Create an instance for non-mainspace use
p = PustInterpreter()

# Test code
if __name__ == "__main__":
    # Define a function outside of mainspace
    p.fn("sigma", """
    wo("https://google.com")
    """)

    # Define and run mainspace code
    p.fn("main", """
    cv("var", iln("Please type 1: "))
    if_stmt("var", "1", ["cv('vartwo', iln('What\\'s your name?: '))"], ["pln('gyat')"])
    if_stmt("vartwo", "seb", ["fn('sigma')"], ["pln('u dum')"])
    """)

    # Create a window and add text content
    my_window = p.cw("My Window", "400x300")
    p.ct(my_window, "Welcome to My Window!")
    p.wl(my_window)
