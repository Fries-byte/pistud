'''
 * ptd loader
 * loading ptd(s)
'''

import urllib.request
custom_keys = {}
functions = {}
def fn(name=None, variable=None, code=None):
    if name and code:
        lines = [line.strip() for line in code.strip().splitlines() if line.strip()]
        functions[name] = {"code": lines, "variable": variable}
        if name == "main":
            for line in lines:
                if line.startswith("define("):
                    exec(line, globals())
                else:
                    slice(line)
    elif name in functions:
        func = functions[name]
        if func["variable"] is not None:
            for line in func["code"]:
                updated_line = line.replace(f"{{{func['variable']}}}", str(variable))
                slice(updated_line)
        else:
            for line in func["code"]:
                slice(line)
                
def newkey(key, code):
    custom_keys[key] = code

def load(packport):
    try:
        response = urllib.request.urlopen(packport)
        raw_content = response.read().decode()
        
        executable_code = []
        for line in raw_content.splitlines():
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith("'''") and not stripped_line.startswith('#'):
                executable_code.append(stripped_line)
        exec("\n".join(executable_code), globals())
    except Exception as e:
        print(f"Error loading package from {packport}: {e}")

def execute_main(code):  
    line_num = 0
    for line in code.splitlines():
        line_num += 1
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
            print(f"Error on line {line_num}: {e}")
            return line_num
    return None
        
newkey("ptd::main", 'load("https://raw.githubusercontent.com/Fries-byte/stud-list/refs/heads/main/main/src.py")')
newkey("ptd::math", 'load("https://raw.githubusercontent.com/Fries-byte/stud-list/refs/heads/main/math/src.py")')
newkey("ptd::sys", 'load("https://raw.githubusercontent.com/Fries-byte/stud-list/refs/heads/main/sys/src.py")')
newkey("ptd::ui", 'load("https://raw.githubusercontent.com/Fries-byte/stud-list/refs/heads/main/ui/src.py")')
newkey("ptd::utils", 'load("https://raw.githubusercontent.com/Fries-byte/stud-list/refs/heads/main/utils/src.py")')
