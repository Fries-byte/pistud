# NOTE:
# THIS IS A OLD TEST FILE, THIS WILL PROBABLY NOT WORK
###
import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(src_path)
import p


# Testing variables
p.cv("Vari", "val")

# Expected output:
# (nothing, but varaible created)
#

# Testing giving value by user input
variable = p.iln("Input: ")
p.pln(variable)

# Expected output:
# (User Input)
#

# Testing printing value
p.cv("testVAR", "valuet")
p.pln("valuet")

# Expected output:
# valuet 
#


# Result: No Errors
