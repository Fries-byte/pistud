import webbrowser # importing webbrowser to open sites
# =--=--=--=--=--=--=--=--=--=--=--=--=
# Pust's Interpreter source
# Created by Pust-Lang (GitHub)
# Learn more on our website or README.md
# =--=--=--=--=--=--=--=--=--=--=--=--=

variables = {}  # Dictionary to store variables
functions = {}  # Dictionary to store functions

def cv(var, val):  # Define variables
    # Store the variable name and its value in the dictionary
    variables[var] = val
# Example usage: cv("variable", "value")

def wo(url): # Define web browser
    # Opening your web browser with the url
    webbrowser.open(url)
    
def pln(l):  # Define Print
    # Check if l is a variable name; if so, print its value from the dictionary
    if l in variables:
        print(variables[l])
    else:
        print(l)
# Example usage: pln("Hello World!") or pln("variable")

def iln(prompt):  # Define input
    # Take input from the user and return it
    return input(prompt)
# Example usage: user_input = iln("Enter something: ")

def fn(name=None, code=None):  # Define and run functions
    """
    If `name` and `code` are provided, define the function.
    If `name` is provided but `code` is None, run the function.
    Automatically run the 'main' function if defined.
    """
    if name and code:
        # Define the function
        functions[name] = code

        # Automatically run the 'main' function after it's defined
        if name == "main":
            for line in code:
                exec(line)
    elif name:
        # Run the function
        if name in functions:
            for line in functions[name]:
                exec(line)
        else:
            print(f"Function '{name}' is not defined.")

# Example usage of the interpreter:
if __name__ == "__main__":
    # Define and run the main function
    fn("main", [
        "pln('Welcome to Pust Interpreter!')",
        "cv('greeting', 'Hello from the main function!')",
        "pln('greeting')",
        "fn('say_hi', [\"pln('Hi from inside another function!')\"])",
        "fn('say_hi')",
        "wo('https://pust-lang.github.io/web/')" 
    ])
