# for one word
with open("censor.txt") as f:
    content = f.read()


content = content.replace("donkey", "ceS####")

with open("censor.txt", "w") as f:
    f.write(content)
