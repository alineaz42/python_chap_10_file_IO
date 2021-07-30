# __________________________File I/O__________________________
# text file editable ex: text
# binary file  not editable  ex: jpb

# open to open a file receives two parameter 1.Name 2. mode
# modes are: r(read) w(write) a(append) +(updatin)
# by default the mode is r
f = open("sample.text", 'r')
# data = f.read() # read runs only once
data = f.read(5)  # reads only the five char from the file
print(data)
f.close()

# rb to read binary file
# rt to read text file
