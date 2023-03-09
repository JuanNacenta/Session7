# len gives you the lenght of the entire string
print(len("hello"), len("hello!"))

# you can assing a string to any variables

a = "123"
b = "abcd"

# + will cncatenate the strings

c =  a + b
print(c)

c = c + b + c
print(c) # 123abcdabcd123abc

a = "123"
s = "abc"
a = a + "ZZZ"
print(a)

# * can only multiply with a positive intenger and repeats the string
a = "Guapa"
print(a*3)
print(4*a)
print((4//2)*a) # si pones solo una / saldra 2.0, no interger, y por tanto ssaldra error
print(int(10/3)*a) #saldra 3 bananas

# strings are iterable... we can use for on item
for letter in a:
    print(letter, end=" ! ")
for letter in a:
    print(3*letter, end="")

# while iterate a string bakcwards
a = "racecarr"
print("\n\n")
i = len(a) - 1
while i >= 0:
    print(a[i])
    i -= 1 # i= i-1