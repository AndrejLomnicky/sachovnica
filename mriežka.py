from PIL import Image, ImageDraw

# 1. Príprava plátna (400x400)
size = 400
img = Image.new("RGB", (size, size), "white")
draw = ImageDraw.Draw(img)

stred = 200
krok = 20

# 3. VLAVO HORE: Mriežka
for i in range(0,201, krok):
    draw.line((i, 0, i, stred), fill="black")
    draw.line((0, i, stred, i), fill="black")

# 4. VPRAVO HORE: Šikmé čiary
for i in range(200,401,20):
    draw.line((i, 0, 200, i-200), fill="black")
# 5. VLAVO DOLE: Schodíky
x, y = 0, stred
for _ in range(10):
    draw.line((x, y, x + krok, y), fill="black", width=1)
    x += krok
    draw.line((x, y, x, y + krok), fill="black", width=1)
    y += krok

# 6. VPRAVO DOLE: Geometrické lúče

draw.line((200, 200, size, size), fill="black", width=1)
draw.line((200, 400, 400, 200), fill="black", width=1)

img.show()
#sústredné kružnice,sústredné štvorce pozrieť