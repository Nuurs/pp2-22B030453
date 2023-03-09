import os
print('Exist:', os.access('/Users/nursultantolegen/tolegen', os.F_OK))
print('Readable:', os.access('/Users/nursultantolegen/tolegen', os.R_OK))
print('Writable:', os.access('/Users/nursultantolegen/tolegen', os.W_OK))
print('Executable:', os.access('/Users/nursultantolegen/tolegen', os.X_OK))