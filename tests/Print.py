import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(src_path)
import p


# Testing print
p.pln("Hello World!")

# Expected output:
# Hello World!
#

# Testing printing varaibles
p.cv("vari", "Hello Variable")
p.pln("vari")

# Expected output:
# Hello Variable
#

# Result: No Errors
