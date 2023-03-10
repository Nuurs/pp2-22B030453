import re

def snake_to_camel(text):
    camelcase = ""
    words = re.split(r"[_]",text)
    for i, word in enumerate(words):
        if i != 0:
            camelcase += word.capitalize()
        else:
            camelcase += word
    return camelcase

text = input()

print(snake_to_camel(text))
 