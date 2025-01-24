import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(src_path)
import p


# Testing the new variable system
p.cv("variable", p.iln("Hello"))
p.pln("variable")

# Expected output:
# (user input)
#

# Result: No Errors
