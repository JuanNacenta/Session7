a = "abcdefghijklmnop"
print(a[3:6])
print(a[13:17], a[-3:-1], a[13:]) # [3:] del 3 hasta el final, el comienzo incluido el final no
print(a[:10])

# step slice
print(a[:10:2]) # va una si, una no, una si , una no. De dos en dos
print(a[:10:2], a[::3]) # todos pero de 3 en 3

# you can use negative start, stop and even stop
print(a[10:3:-1])
print(a[::-1]) # reverseed string

# chech if a string is palindorme
a = "racecar"
if a == a[::-1]:
    print(a, "is a plindorme")
else:
    print("not so much")