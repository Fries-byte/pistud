import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(src_path)
import p

# Testing comments
p.fn("main", """
// Hello World
pln("This is Pust") // Hello World


""")

# Expected Output:
# This is Pust
#


# Result: No Errors
