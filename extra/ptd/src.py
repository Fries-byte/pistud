'''
 * ptd loader
 * loading ptd(s)
'''

import urllib.request
custom_keys = {}
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
        
        
newkey("ptd::main", 'load("https://raw.githubusercontent.com/Fries-byte/stud-list/refs/heads/main/main/src.py")')
newkey("ptd::math", 'load("https://raw.githubusercontent.com/Fries-byte/stud-list/refs/heads/main/math/src.py")')
newkey("ptd::sys", 'load("https://raw.githubusercontent.com/Fries-byte/stud-list/refs/heads/main/sys/src.py")')
newkey("ptd::ui", 'load("https://raw.githubusercontent.com/Fries-byte/stud-list/refs/heads/main/ui/src.py")')
newkey("ptd::utils", 'load("https://raw.githubusercontent.com/Fries-byte/stud-list/refs/heads/main/utils/src.py")')
