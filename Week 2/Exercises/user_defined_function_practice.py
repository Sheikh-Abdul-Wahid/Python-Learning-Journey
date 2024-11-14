def convert():
    farenheit = ((c) * 9/5) + 32
    print(farenheit)

c = int(input("Enter celsius value: "))
convert()

# 0R

def convert():
    farenheit = ((c) * 9/5) + 32
    return farenheit

c = int(input("Enter celsius value: "))
print(convert())

# 0R

def convert(c):
    return ((c) * 9/5) + 32

c = int(input("Enter celsius value: "))
print(f"{convert(c)}°F")

