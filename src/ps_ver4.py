import webbrowser  # Importing webbrowser to open sites
from tkinter import messagebox  # Importing messagebox to give info, warning, error

# =--=--=--=--=--=--=--=--=--=--=--=--=
# PiStud's Interpreter source
# Created by PiStud-Lang (GitHub)
# and written by Fries-byte (GitHub)
# Learn more on our website or README.md
#
# 2025 - presents | The Programming Language PiStud
# =--=--=--=--=--=--=--=--=--=--=--=--=

variables = {}  # Dictionary to store variables
functions = {}  # Dictionary to store functions

def cv(var, val):  
    variables[var] = val  

def wo(url):  
    webbrowser.open(url)  

def mb(type, title, message):  
    method_name = "show" + type  
    method = getattr(messagebox, method_name, None)
    if method:
        method(title, message)
    else:
        print(f"Error: '{method_name}' is not a valid messagebox type.")

def pln(l):  
    if l in variables:  
        print(variables[l])  
    else:
        print(l)  

def iln(prompt):  
    value = input(prompt)  
    return value

def if_stmt(var, value, code_if, code_else=None):  
    if var in variables and variables[var] == value:
        for line in code_if:
            exec(line, globals())
    elif code_else:
        for line in code_else:
            exec(line, globals())

def execute_main(code):  
    """
    Execute code in the mainspace.
    Handles lines with comments (`//`) and blank lines gracefully.
    """
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

def fn(name=None, code=None):  
    if name and code:
        functions[name] = code.splitlines()
        if name == "main":
            execute_main(code)
    elif name:
        if name in functions:
            for line in functions[name]:
                execute_main(line)
        else:
            print(f"Function '{name}' is not defined.")

class PustInterpreter:
    cv = staticmethod(cv)
    wo = staticmethod(wo)
    pln = staticmethod(pln)
    iln = staticmethod(iln)
    fn = staticmethod(fn)
    if_stmt = staticmethod(if_stmt)
    mb = staticmethod(mb)

ps = PustInterpreter()

if __name__ == "__main__":
    ps.fn("main", """
// Define a nested function
fn("Best", ['wo("https://google.com")'])

// Define a variable with input
cv("var", iln("Hello World: "))

// Check the variable using if-else
if_stmt("var", "a", ['mb("error", "epic", "wrong input!")'], ['fn("Best")'])
""")
