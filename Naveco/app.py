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
    return render_template('result_path.html', s= strrr)


def affichage (source, destination): print("la source est", source, "la destination", destination)

@app.route("/get_line")
def suite():
    return render_template("get_line.html")

@app.route('/get_line', methods=['POST'])
def get_line():
    line = request.form['get_line']
    for r in gtfs.gtfs_routes:
        if r.rshortname == line:
           str_line = "" + r.rname
        for s in r.rstops:
            str_line = str_line + s.nomstop
    return render_template('result_line.html', s= str_line)

@app.route("/get_stop")
def suite_stop():
    return render_template("get_stop.html")

@app.route('/get_stop', methods=['POST'])
def get_stop():
    stop = request.form['get_stop']
    for s in gtfs.gtfs_stops:
        if s.nomstop == stop:
            str = s.nomstop
            #print(s.nomstop)
           # for r in s.sroutes:
            #    str ="Ligne : " + r.rshortname + r.rname
    return render_template('result_stop.html', s=str)


if __name__ == '__main__':

    app.run(debug=True)

