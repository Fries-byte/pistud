import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(src_path)
import p

# Testing Functions
p.fn("function", ['pln("Hello World!")'])
p.fn("function") # Running the function

# Expected output:
# Hello World!
#

# Not testing every keywords in Pust


# Result: No Errors