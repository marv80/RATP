import tkinter
import Go


app = tkinter.Tk()
app.geometry("640x480")
app.title("NAVECO menu")
mainmenu = tkinter.Menu(app)

w = tkinter.Label(app, text="Welcome to NavEco", font=("Helvetica", 16))
w.pack()

L1 = tkinter.Label(app, text="Departure Station")
L1.pack()
ENT1 = tkinter.Entry(app, bd=5)
ENT1.pack()
E1 = tkinter.StringVar()
E1 = ENT1.get()
L2 = tkinter.Label(app, text="Arrival Station")
L2.pack()
ENT2 = tkinter.Entry(app, bd=5)
ENT2.pack()
E2=tkinter.StringVar()
E2 = ENT2.get()

def Shortest_Path(beg, en):
    liste = Go.astar(beg, en)
    t = tkinter.Text(app)
    for x in liste:
        t.insert(tkinter.END, x.nomstop + '\n')
    t.pack()
button1 = tkinter.Button(app, text = "Go", width=25, command= lambda :Shortest_Path(E1, E2))
button1.pack()

first_menu = tkinter.Menu(mainmenu, tearoff=0)
first_menu.add_command(label="EXIT", command=app.quit)

second_menu = tkinter.Menu(mainmenu, tearoff=0)
second_menu.add_command(label="Find my route")

third_menu = tkinter.Menu(mainmenu, tearoff=0)

mainmenu.add_cascade(label=" Display lines", menu=first_menu)
mainmenu.add_cascade(label=" Routes", menu=second_menu)
mainmenu.add_cascade(label=" Display the RATP map", menu=third_menu)


app.config(menu=mainmenu)
app.mainloop()
