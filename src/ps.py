import webbrowser  # Importing webbrowser to open sites
from tkinter import messagebox  # Importing messagebox to give info, warning, error
from tkinter import * # Importing tkinter for software builder

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

def cw(wtitle, geo):  # Define create window
    window = Tk()  # Create a Tkinter window object
    window.title(wtitle)  # Set the window's title
    window.geometry(geo)  # Set the window's geometry
    windows[wtitle] = window  # Store window in the windows dictionary with the key wtitle
    print(f"Created and stored window '{wtitle}' in windows.")  # Debugging line
    return window  # Return the created window instance

def ct(windowname, geo, text):  # Define create title with geo (for text position) and text
    if windowname in windows:  # Check if the window exists in the dictionary
        window = windows[windowname]  # Get the window object from the dictionary
        window.title(windowname)  # Set the window's title
        # Parse geo to extract x and y coordinates
        x, y = geo.split('x')  # Assuming geo is in format "x,y" (e.g., "100x150")
        label = Label(window, text=text)  # Create a label with the provided text
        label.place(x=int(x), y=int(y))  # Position the label at the specified coordinates (x, y)
        window.update()  # Force the window to update and reflect changes immediately
        print(f"Updated window '{windowname}' with text at position ({x}, {y}).")  # Debugging line
    else:
        print(f"Error: Window '{windowname}' not found.")  # Handle missing window

def wl(wname):  # Define window loop
    if wname in windows:  # Check if the window exists
        windows[wname].mainloop()  # Open the window
    else:
        print(f"Error: Window '{wname}' not found.")  # Handle missing window

    return window  # Return the window instance

def wl(wname):  # Define window loop
    if wname in windows:  # Check if the window exists
        windows[wname].mainloop()  # Open the window
    else:
        print(f"Error: Window '{wname}' not found.")  # Handle missing window

def cv(var, val):  # Define create variable
    global variables  # Ensure variables is globally accessible
    if isinstance(val, Tk):  # If the value is a Tk window, store it in the windows dictionary
        windows[var] = val
    else:
        variables[var] = val  # Otherwise, store it as a normal variable

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

def if_stmt(var, value, code_if, code_else=None):  # Define if statement
    global variables  # Ensure variables is globally accessible

    # Ensure the variable exists and has the correct value before executing code
    if var in variables and variables[var] == value:
        for line in code_if:
            # Execute the line, assuming p is a predefined object with methods
            exec(f"p.{line.strip()}", globals())
    elif code_else:
        for line in code_else:
            # Execute the else block
            exec(f"p.{line.strip()}", globals())

def execute_main(code):  # Define comments
    # Modify this function to check for triple-quoted blocks and interpret them as main code
    for line in code.splitlines():
        stripped_line = line.strip()
        if stripped_line.startswith('"""') and stripped_line.endswith('"""'):
            stripped_line = stripped_line[3:-3].strip()  # Remove triple quotes
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
        # Process multiline strings properly using triple quotes
        if code.startswith('"""') and code.endswith('"""'):
            lines = [line.strip() for line in code.strip()[3:-3].splitlines() if line.strip()]
        else:
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
    wl = staticmethod(wl)  # Add window loop to interpreter

# Create an instance for non-mainspace use
p = PustInterpreter()
