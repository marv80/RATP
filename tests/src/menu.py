import tkinter

app = tkinter.Tk()
app.geometry("640x480")
app.title("NAVECO menu")
mainmenu = tkinter.Menu(app)

first_menu = tkinter.Menu(mainmenu, tearoff=0)
first_menu.add_command(label="BUS")
first_menu.add_command(label="METRO")
first_menu.add_command(label="RER")
first_menu.add_command(label="TRAMWAY")
first_menu.add_command(label="EXIT", command=app.quit)

second_menu = tkinter.Menu(mainmenu, tearoff=0)
second_menu.add_command(label="Find my route")

third_menu = tkinter.Menu(mainmenu, tearoff=0)

mainmenu.add_cascade(label=" Display lines", menu=first_menu)
mainmenu.add_cascade(label=" Routes", menu=second_menu)
mainmenu.add_cascade(label=" Display the RATP map", menu=third_menu)

app.config(menu=mainmenu)
app.mainloop()
