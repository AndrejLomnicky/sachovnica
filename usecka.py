from PIL import Image

a1 = int(input("zadaj x1: "))
a2 = int(input("zadaj y1: "))
b1 = int(input("zadaj x2: "))
b2 = int(input("zadaj y2: "))

img = Image.new("RGB", (300, 300), "white")

if a1 == b1: #ak je usecka kolma
    if a2 < b2:
        y = a2
        while y <= b2:
            img.putpixel((a1, y), (0, 0, 0))
            y += 1
    else:
        y = b2
        while y <= a2:
            img.putpixel((a1, y), (0, 0, 0))
            y += 1
else:
    a = (b2 - a2) / (b1 - a1)
    b = a2 - a * a1

    if a1 < b1:
        x = a1
        while x <= b1: #pomalorastuca
            y = int(a * x + b)
            img.putpixel((x, y), (0, 0, 0))
            x += 1
    else:
        x = b1        #rychlorastuca
        while x <= a1:
            y = int(a * x + b)
            img.putpixel((x, y), (0, 0, 0))
            x += 1
img.show()




