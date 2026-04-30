import math
import tkinter as tk
import datetime as dt

win=tk.Tk()
win.title("godiny")
canvas = tk.Canvas(win, width=800, height=800,bg="white")
canvas.pack()

s1 = 400
s2 = 400
kratka_ruc = 75
dlha_ruc = 150
polomer_cisla = dlha_ruc + 5
hrubka_h = 3
hrubka_s = 1
hrubka_m = 2

rucicka_m = canvas.create_line(s1, s2, s1, s2 - dlha_ruc, fill='black', width=hrubka_m)
rucicka_s = canvas.create_line(s1, s2, s1, s2 - dlha_ruc, fill='black', width=hrubka_s)
rucicka_h = canvas.create_line(s1, s2, s1, s2 - kratka_ruc, fill='black', width=hrubka_h)

#def kresli(): # verzia na punkáča
    #canvas.delete("all")
    #cas = dt.datetime.now()
    #uhol_minuta = math.radians(cas.minute*6 - 90)
    #canvas.create_line(s1,s2,s1+dlha_ruc*math.cos(uhol_minuta),s2+dlha_ruc*math.sin(uhol_minuta),width=hrubka_h)
    #uhol_sekunda =math.radians(cas.second*6 - 90)
    #canvas.create_line(s1,s2,s1+kratka_ruc*math.cos(uhol_sekunda),s2+kratka_ruc*math.sin(uhol_sekunda),width=hrubka_s)
    #uhol_hodina = (math.radians(cas.hour) * 30 + math.radians(cas.minute) * 0.5)-90
    #canvas.create_line(s1,s2,s1+dlha_ruc*math.cos(uhol_hodina),s2+dlha_ruc*math.sin(uhol_hodina),width=hrubka_h)
    #canvas.after(1000, kresli)
polomer_cifernika = polomer_cisla + 25
canvas.create_oval(s1-polomer_cifernika, s2-polomer_cifernika, s1+polomer_cifernika, s2+polomer_cifernika, outline="black", width=2)

def draw():
    cas = dt.datetime.now()
    uhol_minuta = math.radians(cas.minute * 6 - 90)
    uhol_sekunda = math.radians(cas.second * 6 - 90)
    uhol_hodina = math.radians((cas.hour * 30 + cas.minute * 0.5) - 90)
    canvas.coords(rucicka_m, s1, s2, s1 + dlha_ruc * math.cos(uhol_minuta), s2 + dlha_ruc * math.sin(uhol_minuta))
    canvas.coords(rucicka_s, s1, s2, s1 + dlha_ruc * math.cos(uhol_sekunda), s2 + dlha_ruc * math.sin(uhol_sekunda))
    canvas.coords(rucicka_h, s1, s2, s1 + kratka_ruc * math.cos(uhol_hodina), s2 + kratka_ruc * math.sin(uhol_hodina))
    canvas.after(1000, draw)
    for i in range(12):
        uhol = math.radians(i * 30 - 90)
        x = s1 + polomer_cisla * math.cos(uhol)
        y = s2 + polomer_cisla * math.sin(uhol)
        canvas.create_text(x, y, text=str(i if i != 0 else 12), font=('Arial', 14, 'bold'))
draw()
win.mainloop()
#domaca uloha poslať úlohu nie na punkáča

