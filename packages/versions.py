import urllib.request
if version == 6.5:
  code7 = urllib.request.urlopen("https://raw.githubusercontent.com/Pust-Lang/pust/refs/heads/main/src/ps.py").read().decode()
  exec(code7)
elif version == 6:
  code6 = urllib.request.urlopen("https://raw.githubusercontent.com/Pust-Lang/pust/refs/heads/main/src/ps_ver6.py").read().decode()
  exec(code6)
elif version == 5:
  code5 = urllib.request.urlopen("https://raw.githubusercontent.com/Pust-Lang/pust/refs/heads/main/src/ps_ver5.py").read().decode()
  exec(code5)
elif version == 4:
  code4 = urllib.request.urlopen("https://github.com/Pust-Lang/pust/raw/refs/heads/main/src/ps_ver4.py").read().decode()
  exec(code4)
elif version == 3:
  code3 = urllib.request.urlopen("https://github.com/Pust-Lang/pust/raw/refs/heads/main/src/ps_ver3.py").read().decode()
  exec(code3)
elif version == 2:
  code2 = urllib.request.urlopen("https://github.com/Pust-Lang/pust/raw/refs/heads/main/src/ps_ver2.py").read().decode()
  exec(code2)
elif version == 1:
  code1 = urllib.request.urlopen("https://raw.githubusercontent.com/Pust-Lang/pust/refs/heads/main/src/ps_ver1.py").read().decode()
  exec(code1)
