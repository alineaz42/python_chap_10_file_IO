with open("log.txt") as f:
    content = f.read()  # case censetive
if 'python' in content.lower():  # lower it for case censative case
    print("Yes python is present ")
else:
    print("Python is not present")
