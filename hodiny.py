import math
import tkinter as tk
import datetime as dt
win=tk.Tk()
win.title("moje hodinky")
canvas = tk.Canvas(win, width=800, height=800,bg="white")
canvas.pack()
s1 = 400
s2 = 400
kratka_ruc = 75
dlha_ruc = 150
polomer_cisla = dlha_ruc + 5
hrubka_h = 3
hrubka_s = 1
cas = dt.datetime.now()
print(cas.hour, cas.minute, cas.second)
uhol_minuta = math.radians(cas.minute*6 - 90)
canvas.create_line(s1,s2,s1+dlha_ruc*math.cos(uhol_minuta),s2+dlha_ruc*math.sin(uhol_minuta),width=hrubka_h)
uhol_sekunda =math.radians(cas.second*6 - 90)
canvas.create_line(s1,s2,s1+kratka_ruc*math.cos(uhol_sekunda),s2+kratka_ruc*math.sin(uhol_sekunda),width=hrubka_s)
uhol_hodina = (math.radians(cas.hour) * 30 + math.radians(cas.minute) * 0.5)-90
canvas.create_line(s1,s2,s1+dlha_ruc*math.cos(uhol_hodina),s2+dlha_ruc*math.sin(uhol_hodina),width=hrubka_h)

polomer_cifernika = polomer_cisla + 25
canvas.create_oval(s1-polomer_cifernika, s2-polomer_cifernika, s1+polomer_cifernika, s2+polomer_cifernika, outline="black", width=3)

for hodina in range(1, 13):
    uhol = math.radians(hodina * 30 - 90)
    x = s1 + polomer_cisla * math.cos(uhol)
    y = s2 + polomer_cisla * math.sin(uhol)
    canvas.create_text(x, y, text=str(hodina), font=("Arial", 14, "bold"))

win.mainloop()
