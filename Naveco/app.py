from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import Go
import GTFS

gtfs = GTFS.GTFS()
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    source = request.form['source']
    destination = request.form['destination']
    path = Go.astar(gtfs, source, destination)
    strrr = "Your path start at : " + path[0].sadr
   #  print("Your path start at : " + path[0].sadr)
    for s in path:
        strrr = strrr + s.nomstop
        # print(s.nomstop)
        if s.actual_route:
           strrr = strrr + "On line : "
           # print("On line : ")
           strrr = strrr + s.actual_route.rshortname
           # print(s.actual_route.rshortname)
    print(strrr)

   # return render_template('pass.html', s=source, d=destination)
    return render_template('pass.html', s= strrr)


def affichage (source,destination):
    print("la source est",source, "la destination", destination)

#@app.route("/next")
#def suite():
#    return render_template("page_suivante.html")


if __name__ == '__main__':

    app.run(debug=True)

