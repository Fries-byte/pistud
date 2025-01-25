import webbrowser  # Importing webbrowser to open sites
from tkinter import messagebox  # Importing messagebox to give info, warning, error
from tkinter import *

variables = {}  # Dictionary to store variables
functions = {}  # Dictionary to store functions

def cw(wtitle, geo):  # Define create window
    window = Tk()
    window.title(wtitle)  # Set the window's title
    window.geometry(geo)  # Set the window's geometry
    return window  # Return the created window instance

def ct(window, text_content):  # Define create text for the window
    label = Label(window, text=text_content, font=("Arial", 12))
    label.pack(pady=10)
    return label

def wl(window):  # Define window loop
    window.mainloop()

def cv(var, val):  # Define create variable
    global variables
    variables[var] = val

def wo(url):  # Define web open
    webbrowser.open(url)

def mb(type, title, message):  # Define message box
    method_name = "show" + type
    method = getattr(messagebox, method_name, None)
    if method:
        method(title, message)
    else:
        print(f"Error: '{method_name}' is not a valid messagebox type.")

def pln(l):  # Define print line
    if l in variables:
        print(variables[l])
    else:
        print(l)

def iln(prompt):  # Define input line
    return input(prompt)

def preprocess_code(code):
    """
    Transform custom `if_stmt` syntax with `{}` into valid Python syntax using indentation.
    """
    lines = code.splitlines()
    processed_lines = []
    indent_stack = []

    for line in lines:
        stripped = line.strip()

        # Handle opening brace
        if stripped.endswith("{"):
            indent_stack.append("    ")  # Add a new level of indentation
            processed_lines.append(line.replace("{", ":").rstrip())
            continue

        # Handle closing brace
        if stripped == "}":
            if indent_stack:
                indent_stack.pop()  # Remove one level of indentation
            continue

        # Add current indentation
        current_indent = "".join(indent_stack)
        processed_lines.append(current_indent + stripped)

    return "\n".join(processed_lines)

def execute_main(code):
    code = preprocess_code(code)  # Preprocess code to handle `{}` syntax
    for line in code.splitlines():
        stripped_line = line.strip()
        if "//" in stripped_line:
            stripped_line = stripped_line.split("//", 1)[0].strip()  # Remove inline comments
        if stripped_line == "":
            continue
        try:
            exec(stripped_line, globals())
        except Exception as e:
            print(f"Error in mainspace: {e}")

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
    cv("var", iln("Please type something: "))
    if_stmt("var", includes => "hello") {
        pln("You included hello!")
        wo("https://example.com")
    } else {
        pln("No hello detected.")
    }
    """)
