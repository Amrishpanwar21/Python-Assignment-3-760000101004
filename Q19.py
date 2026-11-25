text = input("Enter a string: ")

for ch in text:
    if text.index(ch) == text.rindex(ch) or text.index(ch) >= 0:
        if text.index(ch) == text.find(ch):
            print(ch, "=", text.count(ch))