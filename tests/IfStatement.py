import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(src_path)
import p


# Testing if statment
p.cv("variable", "value")
p.if_stmt("variable", "value", ['pln("if")'], ['pln("else")'])

# Expected output:
# if
#

# Testing if statment from input
p.cv("variable", p.iln("Hello: "))
p.if_stmt("variable", "World", ['pln("correct")'], ['pln("It was World!")'])

# Expected output:
# (User Input: World): correct
# (User Input: (anything)): It was World!
#

# Result: No Errors
