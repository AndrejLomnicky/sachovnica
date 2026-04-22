import tkinter as tk
win = tk.Tk()
canvas = tk.Canvas(win, width=400, height=400, bg="white")
canvas.pack()
win.title("pisomka geometricke utvary")
def kresli():
    stred = 200
    krok = 20
# vlavo hore
    for i in range(0, stred, krok):
        canvas.create_line(0, stred, i, 0,fill="blue")
        canvas.create_line(stred, stred, i, 0, fill="red")
# kruznice
    sx, sy = 300, 100
    for r in range(0, 110, krok):  # polomery- mala bodka,20, 40, 60, 80, 100
        canvas.create_oval(sx - r, sy - r, sx + r, sy + r)
# vlavo dole
    for riadok in range(10):
        for stlpec in range(10):
            x1 = stlpec * krok
            y1 = stred + (riadok * krok)
            x2 = x1 + krok
            y2 = y1 + krok
            if (riadok + stlpec) % 2 == 0:
                farba = "pink"
            else:
                farba = "yellow"

            canvas.create_rectangle(x1, y1, x2, y2, fill=farba)
# vpravo dole
    for i in range(10):
        x_zel = stred + (i * krok)
        y_zel = stred + (i * krok)
        canvas.create_rectangle(x_zel, y_zel, x_zel + krok, y_zel + krok, fill="green")
        x_zlt = stred + (i * krok)
        y_zlt = 400 - krok - (i * krok)
        canvas.create_rectangle(x_zlt, y_zlt, x_zlt + krok, y_zlt + krok, fill="yellow")
kresli()
win.mainloop()



























