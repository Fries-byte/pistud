import sys, os; sys.path.append(os.path.join(os.path.dirname(__file__), '..')); import package as ps

ps.fn("main", """
  pln("Hello from PiStud!")
""")
