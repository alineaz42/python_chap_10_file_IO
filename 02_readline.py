

f = open("sample.text", 'r')
# data = f.read() # read runs only once
data = f.readline()  # reads only firt line
print(data)
data = f.readline()  # reads only second line
print(data)
data = f.readline()  # reads only third line
print(data)
f.close()
