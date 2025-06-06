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
import os # Importing os for bash and key inputs(s)
import sys # Importing sys to support .ptd files
import ctypes, time # Importing ctypes and time for simulating key input(s)
# Storage
variables = {}
functions = {}
windows = {}
buttons = {}
custom_keys = {}

# Pistud Keywords
def press(key, Os, delay):
    Os = Os.lower()
    time.sleep(delay)

    special_keys = {
        "enter": "\n",
        "tab": "\t",
        "space": " ",
        "backspace": "@backspace<--@"
    }

    if key.lower() in special_keys:
        key = special_keys[key.lower()]

    if Os == "linux":
        if key == "\n":
            os.system("xdotool key Return")
        elif key == "\t":
            os.system("xdotool key Tab")
        elif key == " ":
            os.system("xdotool key space")
        elif key.lower() == "backspace":
            os.system("xdotool key BackSpace")
        else:
            os.system(f"xdotool type '{key}'")

    elif Os == "windows":
        if key == "\n":
            vk = 0x0D
        elif key == "\t":
            vk = 0x09
        elif key == " ":
            vk = 0x20
        elif key.lower() == "backspace":
            vk = 0x08
        else:
            vk = ord(key.upper())

        ctypes.windll.user32.keybd_event(vk, 0, 0, 0)
        ctypes.windll.user32.keybd_event(vk, 0, 2, 0)

    elif Os == "macos":
        if key == "\n":
            os.system("""osascript -e 'tell application "System Events" to key code 36'""")  # Enter
        elif key == "\t":
            os.system("""osascript -e 'tell application "System Events" to key code 48'""")  # Tab
        elif key == " ":
            os.system("""osascript -e 'tell application "System Events" to keystroke space'""")  # Space
        elif key.lower() == "backspace":
            os.system("""osascript -e 'tell application "System Events" to key code 51'""")  # Delete
        else:
            os.system(f"""osascript -e 'tell application "System Events" to keystroke "{key}"'""")

    else:
        raise KeyError("System is not defined. Try using 'Linux', 'Windows', or 'MacOS'.")

def newkey(key, code):
    custom_keys[key] = code

def py(execpython):
    exec(execpython)

def bash(executeos):
    output = os.popen(executeos).read()
    print(output)

def load(packport):
    exec(urllib.request.urlopen(packport).read().decode())

def cw(wtitle, geo):
    window = Tk()
    window.title(wtitle)
    window.geometry(geo)
    windows[wtitle] = window
    return window

def ct(windowname, geo, text):
    if windowname in windows:
        window = windows[windowname]
        x, y = map(int, geo.split('x'))
        label = Label(window, text=text)
        label.place(x=x, y=y)
    else:
        print(f"Error: Window '{windowname}' not found.")

def wl(wname):
    if wname in windows:
        windows[wname].mainloop()
    else:
        print(f"Error: Window '{wname}' not found.")

def let(var_name, value):
    if var_name.startswith("{") and var_name.endswith("}"):
        var_name = var_name[1:-1]
        if var_name in variables:
            var_name = variables[var_name]
    if value.startswith("{") and value.endswith("}"):
        value = value[1:-1]
        if value in variables:
            value = variables[value]

def wo(url):
    webbrowser.open(url)

def mb(type, title, message):
    method_name = "show" + type
    method = getattr(messagebox, method_name, None)
    if method:
        method(title, message)
    else:
        print(f"Error: '{method_name}' is not a valid messagebox type.")

def pln(text, *args):
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

def iln(prompt):
    return input(prompt)

def if_stmt(var, value, code_if, code_else=None):
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

def cb(windowname, geo, size, name):
    if windowname in windows:
        window = windows[windowname]
        x, y = map(int, geo.split(','))
        width, height = map(int, size.split(','))
        button = Button(window, text=name)
        button.place(x=x, y=y, width=width, height=height)
        windows[f"{windowname}_{name}_button"] = button
    else:
        print(f"Error: Window '{windowname}' not found.")

def bc(name, code):
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

def define(name, param, param_type, code):
    def func(value):
        variables[param] = value
        exec(code.replace(f"{{{param}}}", str(value)), globals())
    custom_keys[name] = func

# Other keywords
def fn(name=None, variable=None, code=None):
    if name and code:
        lines = [line.strip() for line in code.strip().splitlines() if line.strip()]
        functions[name] = {"code": lines, "variable": variable}
        if name == "main":
            if variable is not None:
                variables[variable] = None
            execute_main(code)
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

def slice(code):
    execute_main(code)

def loop(code, n):
    if n == 0:
        while True:
            execute_main(code)
    else:
        for _ in range(n):
            execute_main(code)

def math(expression):
    try:
        for var_name, var_value in variables.items():
            placeholder = "{" + var_name + "}"
            if placeholder in expression:
                expression = expression.replace(placeholder, str(var_value))
        return eval(expression, {}, variables)
    except Exception as e:
        print(f"Error evaluating math expression: {e}")
        return None

def catch(code, error_handler):
    try:
        exec(code, globals())
    except Exception as e:
        error_message = str(e)
        for line in error_handler:
            line = line.replace("{!error!}", "Error Found").replace("{!reason!}", error_message)
            exec(line, globals())

newkey('epic', 'pln("...*nEPIC, thats how the Fries-Byte calls the language since its easy for everyone (f-b thinks.), and hed spend his free-time on building this source free program*nnFries-Byte or f-b knew that in the last few years, there are only around 30~ million programmer, no ones intrested or its to hard, so f-b build this to make it easier to program in!*n epic text too!*n...")')

def parse_shrp_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    data = {
        "variables": {},
        "scripts": {},
        "type": "direct"
    }
    current_section = None

    for line in content.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        if line.startswith("type:"):
            data["type"] = line.split(":", 1)[1].strip().strip('"')
            continue
        
        if line.endswith(": {"):
            current_section = line[:-3].strip().lower()
            continue
        
        elif line == "}":
            current_section = None
            continue
        
        elif current_section == "variables":
            if "=" in line:
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().rstrip(',')
                data["variables"][key] = value
        
        elif current_section == "scripts":
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip().rstrip(',')
                data["scripts"][key] = value

    return data

# Function to handle .shrp imports
def handle_shrp_import(import_statement):
    try:
        parts = import_statement.split()
        file_path = parts[1].replace(".shrp", ".shrp")
        variable_names = parts[3].split(",")
        
        shrp_data = parse_shrp_file(file_path)
        for var_name in variable_names:
            var_name = var_name.strip()
            if var_name in shrp_data["variables"]:
                value = shrp_data["variables"][var_name]
                variables[var_name] = value
            else:
                print(f"Error: Variable '{var_name}' not found in '{file_path}'.")
    except Exception as e:
        print(f"Error processing import statement: {e}")

def execute_main(code):
    in_comment_block = False
    cleaned_code = []
    for line in code.splitlines():
        stripped_line = line.strip()
        if "/*" in stripped_line:
            if "*/" in stripped_line:
                stripped_line = stripped_line.split("/*", 1)[0].strip() + stripped_line.split("*/", 1)[1].strip()
            else:
                in_comment_block = True
                stripped_line = stripped_line.split("/*", 1)[0].strip()
        elif "*/" in stripped_line:
            in_comment_block = False
            stripped_line = stripped_line.split("*/", 1)[1].strip()
        elif in_comment_block:
            continue   
        if "//" in stripped_line:
            stripped_line = stripped_line.split("//", 1)[0].strip()
        if stripped_line:
            cleaned_code.append(stripped_line)
    cleaned_code = "\n".join(cleaned_code)
    try:
        for line in cleaned_code.splitlines():
            line = line.strip()
            if line.startswith("from") and ".shrp import" in line:
                handle_shrp_import(line)
            elif line:
                try:
                    exec(line, globals(), variables)
                except Exception as e:
                    print(f"Error executing line: {line}\n{e}")
    except Exception as e:
        print(f"Error in mainspace: {e}")
    
def execute_ptd_file(file_path):
    code = read_ptd_file(file_path)
    if code:
        execute_main(code)

def read_ptd_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

def execute_ptd_file(file_path):
    code = read_ptd_file(file_path)
    if code:
        execute_main(code)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if file_path.endswith('.ptd'):
            execute_ptd_file(file_path)
        else:
            print("Error: The file must have a .ptd extension.")
    else:
        print("Usage: python interpreter.py <file.ptd>")

# Require ps. before keyword
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
    press = staticmethod(press)

# ps
ps = PustInterpreter()
