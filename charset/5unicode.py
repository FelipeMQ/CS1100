print("你".encode("utf-8"))
print("好".encode("utf-8"))

print("\u4F60\u597D".encode())

a,b,c,d,e = "soy un hacker de CS1100".split(" ")
print(a)
print(b)

print("a\0b\0c\0d\0e\0f\0g\0".split("\0"))
print("a\0b\0c\0d\0e\0f\0g\0".rstrip("\0").split("\0"))
print(type("\0"))