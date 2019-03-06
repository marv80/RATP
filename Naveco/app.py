from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import Go
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    source = request.form['source']
    destination = request.form['destination']
    affichage(source, destination)
    return render_template('pass.html', s=source, d=destination)

def affichage (source,destination):
    print("la source est",source, "la destination", destination)

#@app.route("/next")
#def suite():
#    return render_template("page_suivante.html")


if __name__ == '__main__':

    app.run(debug=True)

