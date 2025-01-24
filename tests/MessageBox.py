import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
sys.path.append(src_path)
import p

# Testing message box
# Type: Info
p.mb("info", "InfoBox", "Hello World")

# Type: Warning
p.mb("warning", "WarningBox", "Hello World")

# Type: Error
p.mb("error", "ErrorBox", "Hello World")

# Expected output:
# (nothing)
#


# Result: No Errors
