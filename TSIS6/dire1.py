import os
for root, directories, files in os.walk(r"/Users/nursultantolegen/tolegen"):
    print(root)
    for x in directories:
        print(x)
    for i in files:
        print(i)
