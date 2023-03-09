import os
print("Test a path exists or not:")
path = r'built'
print(os.path.exists(path))
os.remove('built')