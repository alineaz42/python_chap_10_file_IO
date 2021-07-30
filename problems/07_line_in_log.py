content = True

with open("log.txt") as f:
    i = 1
    while content:
        content = f.readline()
        if "python" in content.lower():
            print(f"Yes python is present on line number {i}")
        else:
            print("Python is not present here")
        print(i)
        i += 1
