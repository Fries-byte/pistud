# =--=--=--=--=--=--=--=--=--=--=--=--=
# PiStud's interpreter supporter source
# Created by PiStud-Lang (GitHub)
# and written by Fries-byte (GitHub)
# Learn more on our website or README.md
#
# 2025 - presents | The Programming Language PiStud
# =--=--=--=--=--=--=--=--=--=--=--=--=

# -- NOTE
# All imports had to be removed due to the interpreters mistaking python imports as user-created imports
# -- INFO
# When using newkey, make sure its outside of a function like thus:
# ps.newkey("call", "pln('hello world!')")
#

variables = {}
functions = {}
custom_keys = {}

def newkey(key, code):
    custom_keys[key] = code  # Store the custom key and its associated code

def redokey(code):
    for key, value in custom_keys.items():
        code = code.replace(key, value)
    return code

def upvar(var, val):
    if var in variables:
        variables[var] = val
    else:
        print(f"Error: Variable '{var}' not found.")

def py(execpython):
    try:
        compiled_code = compile(execpython, '<string>', 'exec')
        exec(compiled_code, globals(), locals())
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
    except Exception as e:
        print(f"Error executing Python code: {e}")

def let(var, val):
    variables[var] = val

def pln(text, *args):
    text = text.replace("*n", "\n").replace("*t", "\t")
    for var_name, var_value in variables.items():
        text = text.replace(f"{{{var_name}}}", str(var_value))
    for i, arg in enumerate(args):
        text = text.replace(f"{{{i}}}", str(arg))
    print(text)

def iln(prompt):
    return input(prompt)

def if_stmt(var, value, code_if, code_else=None):
    if var in variables and variables[var] == value:
        try:
            for line in code_if:
                cleaned_line = line.split("//")[0].strip()
                if cleaned_line:
                    compiled_line = compile(cleaned_line, '<string>', 'exec')
                    exec(compiled_line, globals(), locals())
        except SyntaxError as e:
            print(f"Syntax Error in if block: {e}")
        except Exception as e:
            print(f"Error in if block: {e}")
    elif code_else:
        try:
            for line in code_else:
                cleaned_line = line.split("//")[0].strip()
                if cleaned_line:
                    compiled_line = compile(cleaned_line, '<string>', 'exec')
                    exec(compiled_line, globals(), locals())
        except SyntaxError as e:
            print(f"Syntax Error in else block: {e}")
        except Exception as e:
            print(f"Error in else block: {e}")
    else:
        print(f"Variable '{var}' not found.")

def execute_main(code):
    # Replace custom keys in the code before execution
    code = redokey(code)
    for line in code.splitlines():
        stripped = line.split("//")[0].strip()
        if stripped:
            try:
                compiled_line = compile(stripped, '<string>', 'exec')
                exec(compiled_line, globals(), locals())
            except SyntaxError as e:
                print(f"Syntax Error in execution: {e}")
            except Exception as e:
                print(f"Error in execution: {e}")

def fn(name=None, code=None):
    if name and code:
        functions[name] = [line.split("//")[0].strip() for line in code.strip().splitlines() if line.split("//")[0].strip()]
        if name == "main":
            execute_main(code)
    elif name in functions:
        for line in functions[name]:
            try:
                compiled_line = compile(line, '<string>', 'exec')
                exec(compiled_line, globals(), locals())
            except SyntaxError as e:
                print(f"Syntax Error in function '{name}': {e}")
            except Exception as e:
                print(f"Error in function '{name}': {e}")
    else:
        print(f"Function '{name}' not found.")

def loop(code, n):
    if n == 0:
        while True:
            execute_main(code)
    else:
        for _ in range(n):
            execute_main(code)

class PustInterpreter:
    let = staticmethod(let)
    pln = staticmethod(pln)
    iln = staticmethod(iln)
    fn = staticmethod(fn)
    if_stmt = staticmethod(if_stmt)
    newkey = staticmethod(newkey)

ps = PustInterpreter()
