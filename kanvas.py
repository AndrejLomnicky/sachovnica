#widgety/komponenty, canvas-plátno na kreslenie
#bude program na kreslenie na hodinu!!!
import tkinter as tk
win = tk.Tk()
win.title("moje prve okienko")

pocitadlo = 0
def akcia():
    global pocitadlo
    print(f"akcia {pocitadlo}")
    pocitadlo += 1
    farba = canvas.itemcget(2,"fill")
    print(farba)
    if farba == "black":
        canvas.itemconfig(2,fill="red")
    else:
        canvas.itemconfig(2,fill="black")
canvas = tk.Canvas(win, width=400, height=400, bg="coral")
canvas.pack() #vytvorene objekty dava podseba
button = tk.Button(win, text="stlač ma oci", width=50, bg="hotpink", command=akcia)
button.pack()
obj1 = canvas.create_line(0,0,400,400)
obj2 = canvas.create_rectangle(100,100,200,200,fill="blue", outline="black")
obj3 = canvas.create_oval(200,200,300,400,fill="white", outline="black") #može byť aj elipsa
print(obj1, obj2, obj3)
canvas.itemconfig(2, fill="black")
win.mainloop()
