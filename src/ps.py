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
buttons = {}  # Dictionary to store created buttons


# Define create window
def cw(wtitle, geo):  
    window = Tk()
    window.title(wtitle)
    window.geometry(geo)
    windows[wtitle] = window
    return window


# Define create text
def ct(windowname, pos, size, text):  
    """
    Create and place text within a parent window.
    :param windowname: Parent window name.
    :param pos: Text position in "x,y" format.
    :param size: Text size in "width,height" format.
    :param text: Text to display.
    """
    if windowname in windows:
        x, y = map(int, pos.split(','))  # Parse x and y coordinates
        width, height = map(int, size.split(','))  # Parse width and height
        label = Label(windows[windowname], text=text, width=width, height=height)
        label.place(x=x, y=y)
        windows[windowname].update()
    else:
        print(f"Error: Window '{windowname}' not found.")


# Define create button
def cb(parent, pos, size, text):  
    if parent in windows:
        x, y = map(int, pos.split(','))
        width, height = map(int, size.split(','))
        button = Button(windows[parent], text=text)
        button.place(x=x, y=y, width=width, height=height)
        buttons[text] = button
        return button
    else:
        print(f"Error: Window '{parent}' not found.")


# Define button click
def bc(button_text, code):  
    if button_text in buttons:
        def on_click():
            for line in code:
                try:
                    exec(line, globals())
                except Exception as e:
                    print(f"Error executing button code: {e}")

        buttons[button_text].config(command=on_click)
    else:
        print(f"Error: Button '{button_text}' not found.")


# Define window loop
def wl(wname):  
    if wname in windows:
        windows[wname].mainloop()
    else:
        print(f"Error: Window '{wname}' not found.")


# Define create variable
def cv(var, val):  
    variables[var] = val


# Define web open
def wo(url):  
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Error opening URL: {e}")


# Define message box
def mb(type, title, message):  
    method_name = "show" + type.capitalize()
    method = getattr(messagebox, method_name, None)
    if method:
        method(title, message)
    else:
        print(f"Error: '{method_name}' is not a valid messagebox type.")


# Define print line
def pln(l):  
    if l in variables:
        print(variables[l])
    else:
        print(l)


# Define if statement
def if_stmt(variable, **kwargs):  
    """
    Execute conditional logic.
    :param variable: Variable name or value to check.
    :param kwargs: Supports 'includes', '=>', 'code', and 'else'.
    """
    includes = kwargs.get("includes")
    value = kwargs.get("=>")
    code = kwargs.get("code", [])
    else_code = kwargs.get("else", [])

    # Handle includes logic
    if includes and variable in variables:
        if includes in variables[variable]:
            execute_code_block(code)
        else:
            execute_code_block(else_code)
    elif variable in variables and variables[variable] == value:
        execute_code_block(code)
    elif variable == value:
        execute_code_block(code)
    else:
        execute_code_block(else_code)


# Execute a block of code
def execute_code_block(code):  
    """
    Execute a list of code lines.
    :param code: List of strings containing code lines.
    """
    for line in code:
        try:
            exec(line, globals())
        except Exception as e:
            print(f"Error executing code: {e}")


# Define mainspace execution
def execute_main(code):  
    """
    Parse and execute mainspace code.
    :param code: Multiline string of code.
    """
    for line in code.splitlines():
        stripped_line = line.strip()
        if stripped_line.startswith('"""') and stripped_line.endswith('"""'):
            stripped_line = stripped_line[3:-3].strip()  # Remove triple quotes
        if "//" in stripped_line:
            stripped_line = stripped_line.split("//", 1)[0].strip()  # Remove inline comments
        if stripped_line == "":
            continue  # Ignore blank lines
        try:
            exec(stripped_line, globals())
        except Exception as e:
            print(f"Error in mainspace: {e}")


# Define function
def fn(name=None, code=None):  
    """
    Define or execute functions.
    :param name: Name of the function.
    :param code: Multiline string of function code.
    """
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


# Alias functions for the PustInterpreter
class PustInterpreter:
    cv = staticmethod(cv)
    wo = staticmethod(wo)
    pln = staticmethod(pln)
    wl = staticmethod(wl)
    ct = staticmethod(ct)
    cb = staticmethod(cb)
    bc = staticmethod(bc)
    fn = staticmethod(fn)
    mb = staticmethod(mb)
    if_stmt = staticmethod(if_stmt)


# Create an instance for non-mainspace use
ps = PustInterpreter()
