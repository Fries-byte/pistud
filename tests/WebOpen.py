import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(src_path)
import p


# Testing opening web browser
p.wo("https://url.com")

# Expected output:
# (nothing)
#

# Result: No Errors
