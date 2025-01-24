# NOTE:
# THIS IS A OLD TEST FILE, THIS WILL PROBABLY NOT WORK
###
import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(src_path)
import p


# Testing input
p.iln("Input: ")

# Expected output:
# (nothing)
#

# Testing input, output the input by variable
variable = p.iln("Input: ")
p.pln(variable)

# Expected output:
# (User Input)
#

# Result: No Errors
