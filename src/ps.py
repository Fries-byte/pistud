'''
 * PiStud's interpreter source
 * Created by PiStud-Lang (GitHub)
 * and written by Fries-byte (GitHub)
 * Learn more on our website or README.md
 *
 * 2025 - presents | The Programming Language PiStud
'''

import webbrowser  # Importing webbrowser to open sites
from tkinter import messagebox  # Importing messagebox to give info, warning, error
from tkinter import *  # Importing tkinter for software builder
import urllib.request  # Importing urllib to import packages
import os # Importing os for bash

'''
*  Storage:
'''
variables = {}
functions = {}
windows = {}
buttons = {}
custom_keys = {}

'''
*  Pistud Keywords
'''
def newkey(key, code):  # Define newkey
    custom_keys[key] = code 

def py(execpython):  # Define executing python code
    exec(execpython)

def bash(executeos): # Define executing bash
    output = os.popen(executeos).read()
    print(output)
    
def load(packport):  # Define package loader
    exec(urllib.request.urlopen(packport).read().decode())  # Gets and decodes the package
    
def cw(wtitle, geo):  # Define create window
    window = Tk()
    window.title(wtitle)
    window.geometry(geo)
    windows[wtitle] = window
    return window

def ct(windowname, geo, text):  # Define create text
    if windowname in windows:
        window = windows[windowname]
        x, y = map(int, geo.split('x'))
        label = Label(window, text=text)
        label.place(x=x, y=y)
    else:
        print(f"Error: Window '{windowname}' not found.")

def wl(wname):  # Define window loop
    if wname in windows:
        windows[wname].mainloop()
    else:
        print(f"Error: Window '{wname}' not found.")

def let(var_name, value): # Define letting variable being created
    if var_name.startswith("{") and var_name.endswith("}"):
        var_name = var_name[1:-1]
        if var_name in variables:
            var_name = variables[var_name]
    if value.startswith("{") and value.endswith("}"):
        value = value[1:-1]
        if value in variables:
            value = variables[value]

def wo(url):  # Define web open
    webbrowser.open(url)

def mb(type, title, message):  # Define message box
    method_name = "show" + type
    method = getattr(messagebox, method_name, None)
    if method:
        method(title, message)
    else:
        print(f"Error: '{method_name}' is not a valid messagebox type.")

def pln(text, *args):  # Define print
    text = text.replace("*n", "\n")
    text = text.replace("*t", "\t")
    for var_name in variables:
        placeholder = "{" + var_name + "}"
        if placeholder in text:
            text = text.replace(placeholder, str(variables[var_name]))
    for i, arg in enumerate(args):
        placeholder = "{" + str(i) + "}"
        if placeholder in text:
            text = text.replace(placeholder, str(arg))
    print(text)

def iln(prompt):  # Define input line
    return input(prompt)

def if_stmt(var, value, code_if, code_else=None):  # Define if statement
    if var in variables:
        if variables[var] == value:
            try:
                for line in code_if:
                    if callable(line): 
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
        x, y = map(int, geo.split(','))
        width, height = map(int, size.split(','))
        button = Button(window, text=name)
        button.place(x=x, y=y, width=width, height=height)
        windows[f"{windowname}_{name}_button"] = button
    else:
        print(f"Error: Window '{windowname}' not found.")

def bc(name, code):  # Define button click
    for key, button in windows.items():
        if key.endswith(f"_{name}_button"):
            def on_click():
                for line in code:
                    line = line.strip()
                    if line.startswith("fn("):
                        func_name = line[3:-1]
                        if func_name in functions:
                            for func_line in functions[func_name]:
                                exec(func_line.strip(), globals())
                        else:
                            print(f"Error: Function '{func_name}' not found.")
                    else:
                        print(f"Error: Invalid code '{line}'.")
            button.config(command=on_click)
            print(f"Click event bound to button '{name}'.")
            return
    print(f"Error: Button '{name}' not found.")

def define(name, param, param_type, code): # Define define (weird)
    def func(value):
        variables[param] = value
        exec(code.replace(f"{{{param}}}", str(value)), globals())
    
    custom_keys[name] = func 

'''
*  Other keywords:
'''
def fn(name=None, variable=None, code=None):  # Define functions
    if name and code:
        lines = [line.strip() for line in code.strip().splitlines() if line.strip()]
        functions[name] = {"code": lines, "variable": variable}
        if name == "main":
            if variable is not None:
                variables[variable] = None
            for line in lines:
                exec(line, globals())
    elif name in functions:
        func = functions[name]
        if func["variable"] is not None:
            for line in func["code"]:
                updated_line = line.replace(f"{{{func['variable']}}}", str(variable))
                exec(updated_line, globals())
        else:
            for line in func["code"]:
                exec(line, globals())
    else:
        print(f"Function '{name}' not found.")

def slice(code):  # Define slice keyword
    execute_main(code)

def loop(code, n):  # Define loop
    if n == 0: # Loop
        while True:
            execute_main(code)
    else:
        for _ in range(n):
            execute_main(code)

def math(expression):  # Define math
    try:
        for var_name, var_value in variables.items():
            placeholder = "{" + var_name + "}"
            if placeholder in expression:
                expression = expression.replace(placeholder, str(var_value))
        return eval(expression, {}, variables)
    except Exception as e:
        print(f"Error evaluating math expression: {e}")
        return None

def catch(code, error_handler): # Define catch
    try:
        exec(code, globals())
    except Exception as e:
        error_message = str(e)
        for line in error_handler:
            line = line.replace("{!error!}", "Error Found").replace("{!reason!}", error_message)
            exec(line, globals())

# Register 'slice' as a custom keyword
newkey('slice', 'slice')

newkey('epic', 'pln("...*nEPIC, thats how the Fries-Byte calls the language since its easy for everyone (f-b thinks.), and hed spend his free-time on building this source free program*nnFries-Byte or f-b knew that in the last few years, there are only around 30~ million programmer, no ones intrested or its to hard, so f-b build this to make it easier to program in!*n epic text too!*n...")') # Define funneh print

'''
*  Read and interpret before running:
'''
def execute_main(code):  
    for line in code.splitlines():
        stripped_line = line.strip()
        if "//" in stripped_line:
            stripped_line = stripped_line.split("//", 1)[0].strip()
        if stripped_line == "":
            continue
        try:
            if stripped_line in custom_keys:  
                custom_keys[stripped_line]()
            else:
                parts = stripped_line.split(" ", 1)
                if parts[0] in custom_keys:
                    if len(parts) > 1:
                        custom_keys[parts[0]](parts[1])
                    else:
                        custom_keys[parts[0]]("")
                else:
                    exec(stripped_line, globals())
        except Exception as e:
            print(f"Error in mainspace: {e}")

'''
*  Require ps. before keyword:
'''
class PustInterpreter:
    let = staticmethod(let)
    wo = staticmethod(wo)
    pln = staticmethod(pln)
    iln = staticmethod(iln)
    fn = staticmethod(fn)
    if_stmt = staticmethod(if_stmt)
    mb = staticmethod(mb)
    wl = staticmethod(wl)
    cb = staticmethod(cb)
    newkey = staticmethod(newkey)
    math = staticmethod(math)
    catch = staticmethod(catch)
    slice = staticmethod(slice)

'''
*  ps
'''
ps = PustInterpreter()
