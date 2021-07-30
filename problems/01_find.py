

f = open("sample.txt")
t = f.read()
if 'twinkel' in t:
    print("twinkel is present")
else:
    print("twinkel is not present")
f.close()
