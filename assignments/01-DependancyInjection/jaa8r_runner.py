import sys
for key in sys.modules:
    sys.modules[key] = None
import jaa8r_diffuser
