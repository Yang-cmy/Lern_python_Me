import sys

# Check if numpy is loaded anywhere in the Python environment
if 'numpy' in sys.modules:
    print("NumPy has been imported!")
else:
    print("NumPy has NOT been imported yet.")
