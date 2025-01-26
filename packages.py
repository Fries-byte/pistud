import urllib.request
if name == "versions":
  if version == 6.5:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Pust-Lang/pust/refs/heads/main/src/ps.py").read().decode())
  elif version == 6:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Pust-Lang/pust/refs/heads/main/src/ps_ver6.py").read().decode())
  elif version == 5:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Pust-Lang/pust/refs/heads/main/src/ps_ver5.py").read().decode())
  elif version == 4:
    exec(urllib.request.urlopen("https://github.com/Pust-Lang/pust/raw/refs/heads/main/src/ps_ver4.py").read().decode())
  elif version == 3:
    exec(urllib.request.urlopen("https://github.com/Pust-Lang/pust/raw/refs/heads/main/src/ps_ver3.py").read().decode())
  elif version == 2:
    exec(urllib.request.urlopen("https://github.com/Pust-Lang/pust/raw/refs/heads/main/src/ps_ver2.py").read().decode())
  elif version == 1:
    exec(urllib.request.urlopen("https://raw.githubusercontent.com/Pust-Lang/pust/refs/heads/main/src/ps_ver1.py").read().decode())
    
if name == "gopust":
    if version == 1:
      exec(urllib.request.urlopen("https://raw.githubusercontent.com/Pust-Lang/pust/refs/heads/main/src/ps_ver1.py").read().decode())
