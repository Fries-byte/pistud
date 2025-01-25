if version == 5:
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
      window = Tk()
      window.title(wtitle)  # Set the window's title
      window.geometry(geo)  # Set the window's geometry
      return window  # Return the created window instance
  
  def ct(ttitle, geo):  # Define create window
      window.title(wtitle)  # Set the window's title
      window.geometry(geo)  # Set the window's geometry
      return window  # Return the created window instance
  
  def wl(wname):  # Define window loop
      if wname in windows:  # Check if the window exists
          windows[wname].mainloop()  # Open the window
      else:
          print(f"Error: Window '{wname}' not found.")  # Handle missing window
  
  def cv(var, val):  # Define create variable
      global variables  # Ensure `variables` is globally accessible
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
      wl = staticmethod(wl)  # Add window loop to interpreter
  
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
      cv("mywindow", cw("My Auto Window", "400x300")) // Create a window and store it as a variable
      wl("mywindow") // Open the window
      """)
else:
  break

  if version == 4:
    import webbrowser  # Importing webbrowser to open sites
  from tkinter import messagebox  # Importing messagebox to give info, warning, error
  
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
  
  p = PustInterpreter()
  
  if __name__ == "__main__":
      p.fn("main", """
  // Define a nested function
  fn("Best", ['wo("https://google.com")'])
  
  // Define a variable with input
  cv("var", iln("Hello World: "))
  
  // Check the variable using if-else
  if_stmt("var", "a", ['mb("error", "epic", "wrong input!")'], ['fn("Best")'])
  """)

else:
  break
  
if version == 3:
  import webbrowser  # Importing webbrowser to open sites
from tkinter import messagebox # Importing messagebox to give info, warning, error

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

def cv(var, val):  # Define variables
    variables[var] = val  # Store the variable name and its value in the dictionary

def wo(url):  # Define web browser
    webbrowser.open(url)  # Open your web browser with the URL

def mb(type, title, message): # Define message box
    method_name = "show" + type # Includes "show"
    method = getattr(messagebox, method_name, None)
    if method:
        method(title, message)
    else:
        print(f"Error: '{method_name}' is not a valid messagebox type.")

def pln(l):  # Define Print
    if l in variables:  # Check if `l` is a variable name
        print(variables[l])  # Print its value from the dictionary
    else:
        print(l)  # Print the value directly

def iln(prompt):  # Define input
    value = input(prompt)  # Take input from the user
    return value

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
    mb = staticmethod(mb)

# Create an instance for non-mainspace use
p = PustInterpreter()

# Example usage of the interpreter
if __name__ == "__main__":
    # Outside mainspace usage with input and if_stmt
    p.cv("variable", p.iln("Type 1: "))
    p.if_stmt("variable", "1", 
        ["p.pln('Correct!')"], 
        ["p.pln('Wrong!')"]
    )

    # Inside mainspace usage
    p.fn("main", [
        "cv('guess', iln('Guess the word: '))",
        "if_stmt('guess', 'Pust', [\"pln('You guessed correctly!')\"], [\"pln('Try again!')\"])"
    ])
else:
  break
if version == 2:
  import webbrowser  # Importing webbrowser to open sites
  
  # =--=--=--=--=--=--=--=--=--=--=--=--=
  # Pust's Interpreter source
  # Created by Pust-Lang (GitHub)
  # and written by Fries-byte (GitHub)
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
      value = input(prompt)  # Take input from the user
      return value
  
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
      # Outside mainspace usage with input and if_stmt
      p.cv("variable", p.iln("Type 1: "))
      p.if_stmt("variable", "1", 
          ["p.pln('Correct!')"], 
          ["p.pln('Wrong!')"]
      )
  
      # Inside mainspace usage
      p.fn("main", [
          "cv('guess', iln('Guess the word: '))",
          "if_stmt('guess', 'Pust', [\"pln('You guessed correctly!')\"], [\"pln('Try again!')\"])"
      ])
else:
  break
  
if version == 1:
  # Pust's Interpreter source
  # Created by Pust-Lang (GitHub)
  # Learn more on our website or README.md
  # =--=--=--=--=--=--=
  
  variables = {}  # Dictionary to store variables
  functions = {}  # Dictionary to store functions
  
  def cv(var, val):  # Define variables
      # Store the variable name and its value in the dictionary
      variables[var] = val
  # Example usage: cv("variable", "value")
  
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
          "fn('say_hi', [\"pln('Hi from inside another function!')\"])",  # Add a nested function
          "fn('say_hi')"  # Run the nested function
      ])
else:
  break
