import urllib.request
if name == "versions":
  if version == 12:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/PiStud/refs/heads/main/src/ps.py").read().decode())
  if version == 11:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/PiStud/refs/heads/main/src/ps_ver11.py").read().decode())
  elif version == 10:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/PiStud/refs/heads/main/src/ps_ver10.py").read().decode())
  elif version == 9:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/PiStud/refs/heads/main/src/ps_ver9.py").read().decode())
  elif version == 8.5:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/pistud/refs/heads/main/src/ps_ver8.py").read().decode())
  elif version == 7:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/PiStud/refs/heads/main/src/ps_ver7.py").read().decode())
  elif version == 6:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/PiStud/refs/heads/main/src/ps_ver6.py").read().decode())
  elif version == 5:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/PiStud/refs/heads/main/src/ps_ver5.py").read().decode())
  elif version == 4:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/PiStud/refs/heads/main/src/ps_ver4.py").read().decode())
  elif version == 3:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/PiStud/refs/heads/main/src/ps_ver3.py").read().decode())
  elif version == 2:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/PiStud/refs/heads/main/src/ps_ver2.py").read().decode())
  elif version == 1:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/PiStud/refs/heads/main/src/ps_ver1.py").read().decode())
    
if name == "support":
    if version == 1:
      exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/pistud/refs/heads/main/extra/supporter/ps_support.py").read().decode())
