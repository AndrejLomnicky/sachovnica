#vytvor obrázok s rozmermi 200*300 kde sa šachovnicovo striedajú pixely
from PIL import Image

sirka, vyska = 200, 300
img = Image.new("RGB", (sirka, vyska), "white")
pixels = img.load()

for x in range(sirka):
    for y in range(vyska):
        if (x + y) % 2 == 0:
            pixels[x, y] = (0, 0, 0)
        else:
            pixels[x, y] = (255, 255, 255)
