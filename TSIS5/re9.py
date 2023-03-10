import re
def spaces(text):
    x = ""
    words = re.findall(r"[A-Z][a-z]+",text)
    for i, word in enumerate(words):
        if i != 0:
            x += " " + word
        else:
            x += word
    return x

text = input()
print(spaces(text))
