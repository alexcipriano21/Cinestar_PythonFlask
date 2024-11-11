from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cines", defaults={'id' : None })
@app.route("/cines/<id>")
def cines(id):
    if id is None:
        data = requests.get('https://oaemdl.es/cinestar_sweb_php/cines')
        cines = data.json()['data']
        return render_template('cines.html', cines = cines)

    data = requests.get('https://oaemdl.es/cinestar_sweb_php/cines')
    cine = data.json()['data']
    return render_template('cine.html', cine = cine)

@app.route("/peliculas/<id>")
def peliculas(id):
    if id == 'cartelera' or id == 'estrenos':
        data = requests.get(f'https://oaemdl.es/cinestar_sweb_php/peliculas/{id}')
        peliculas = data.json()['data']
        return render_template('peliculas.html', peliculas = peliculas)

    data = requests.get(f'https://oaemdl.es/cinestar_sweb_php/peliculas/{id}')
    pelicula = data.json()['data']
    return render_template('pelicula.html', pelicula = pelicula)

if __name__ == "__main__":
    app.run(debug=True)
