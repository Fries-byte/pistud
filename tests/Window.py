import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(src_path)
import p


# Testing create window
p.cv("windowname", p.cw("Title", "400x300"))
p.wl("windowname")

# Expected output:
# (nothing)
#

# Result: No Errors
