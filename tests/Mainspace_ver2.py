import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(src_path)
import p

# Testing the new mainspace system
p.fn("main", """

pln("This is Pust")


""") # if a function is named "main" the function will run automaticlly

# Expected Output:
# This is Pust
#


# Result: No Errors
