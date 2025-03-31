import pathlib as pl

import numpy as np
import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

# Charger les données CSV
associations_df = pd.read_csv(data / 'associations_etudiantes.csv')
evenements_df = pd.read_csv(data / 'evenements_associations.csv')

## Vous devez ajouter les routes ici : 

@app.route('/alive', methods=['GET'])
def alive():
  if request.method == 'GET':
    if app.status_code == 200:
       print(f"+200 OK : {serveur : alive}")
  else:
    return "Méthode non autorisée", 405
  
@app.route('/associations', methods=['GET'])
def associations():
  if request.method == 'GET':
    l = associations_df['nom']
    print(l)
  else:
    return "Méthode non autorisée", 405
  
@app.route('/association/<int:id>', methods=['GET'])
def association(id):
  if request.method == 'GET':
    if id in associations():
      pass
    else:
      print(f"404 Not Found : {error : Association not found}")
  else:
    return "Méthode non autorisée", 405
  
@app.route('/evenements', methods=['GET'])
def evenements(id):
  if request.method == 'GET':
    l = evenements_df['nom']
    print(l)
  else:
    return "Méthode non autorisée", 405
  
@app.route('/evenement/<int:id>', methods=['GET'])
def association(id):
  if request.method == 'GET':
    if id in evenements():
      pass
    else:
      print(f"404 Not Found : {error : Event not found}")
  else:
    return "Méthode non autorisée", 405




if __name__ == '__main__':
    app.run(debug=False)
