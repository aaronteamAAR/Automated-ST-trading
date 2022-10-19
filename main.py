from io import StringIO
import sys


buffer = StringIO()
sys.stdout = buffer

print('This will be stored in the print_output variable')
print_output = buffer.getvalue()

# 👇️ restore stdout to default for print()
sys.stdout = sys.__stdout__

# 👇️ -> This will be stored in the print_output variable
print('->', print_output)