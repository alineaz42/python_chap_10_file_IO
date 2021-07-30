# for multiple word
words = ["donkey", "mota", "kaddu"]

with open("censor.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "########")
    with open("censor.txt", 'w') as f:
        f.write(content)
