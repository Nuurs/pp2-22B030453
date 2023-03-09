with open("file.py") as f:
    with open("Ffile.py", "w") as f1:
        for line in f:
            f1.write(line)