import webbrowser  # Importing webbrowser to open sites

# =--=--=--=--=--=--=--=--=--=--=--=--=
# Pust's Interpreter source
# Created by Pust-Lang (GitHub)
# Learn more on our website or README.md
# =--=--=--=--=--=--=--=--=--=--=--=--=

variables = {}  # Dictionary to store variables
functions = {}  # Dictionary to store functions

def cv(var, val):  # Define variables
    variables[var] = val  # Store the variable name and its value in the dictionary

def wo(url):  # Define web browser
    webbrowser.open(url)  # Open your web browser with the URL

def pln(l):  # Define Print
    if l in variables:  # Check if `l` is a variable name
        print(variables[l])  # Print its value from the dictionary
    else:
        print(l)  # Print the value directly

def iln(prompt):  # Define input
    return input(prompt)  # Take input from the user and return it

def if_stmt(var, value, code_if, code_else=None):  
    """
    Check if the variable equals the value.
    Execute `code_if` if true, and `code_else` (if provided) if false.
    """
    if var in variables and variables[var] == value:
        for line in code_if:
            exec(line, globals())
    elif code_else:
        for line in code_else:
            exec(line, globals())

def fn(name=None, code=None):  # Define and run functions
    """
    If `name` and `code` are provided, define the function.
    If `name` is provided but `code` is None, run the function.
    Automatically run the 'main' function if defined.
    """
    if name and code:
        functions[name] = code  # Define the function
        if name == "main":  # Automatically run the 'main' function
            for line in code:
                exec(f"p.{line}")
    elif name:
        if name in functions:  # Run a previously defined function
            for line in functions[name]:
                exec(f"p.{line}")
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


# Create an instance for non-mainspace use
p = PustInterpreter()

# Example usage of the interpreter
if __name__ == "__main__":
    # Non-mainspace usage
    p.cv("status", "active")
    p.if_stmt("status", "active", 
        ["p.pln('Status is active!')"], 
        ["p.pln('Status is inactive.')"]
    )

    # Mainspace usage
    p.fn("main", [
        "cv('role', 'guest')",
        "if_stmt('role', 'admin', [\"pln('Welcome, Admin!')\"], [\"pln('Welcome, Guest.')\"])"
    ])
