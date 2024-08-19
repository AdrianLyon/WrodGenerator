import sys
print(sys.executable)

try:
    import docx
    import pandas as pd
    print("Modules are available!")
except ImportError as e:
    print(f"Module not found: {e}")
