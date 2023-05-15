from flask import Flask
from flask import render_template
from flask import request
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.utils as plotly_utils

app = Flask(__name__)

@app.route('/')
@app.route('/about/')
def index():
    return render_template('about.html')

def plotMutation(mut, data):
    fig = go.Figure()

    temp = data[data['Nature mutation'] == mut]
    temp['Date mutation'] = pd.to_datetime(temp['Date mutation'], format='%d/%m/%Y')
    result = temp.groupby(temp['Date mutation'].dt.to_period("M"))['Valeur fonciere'].sum()
    result.index = result.index.to_timestamp()
    x = result.index
    y = result.values

    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color="#0b53c1", width=2.4), name=mut, hovertemplate='(%{x}, %{y})'))

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


@app.route('/widget/')
def DynamicPlot():
    Data = pd.read_csv('valeursfoncieres-2019.txt', sep='|')
    columns_to_keep = ['Date mutation', 'Nature mutation', 'Valeur fonciere', 'Code postal', 'Commune', 'Code departement', 'Code commune', 'Nombre de lots', 'Code type local', 'Type local', 'Surface reelle bati', 'Nombre pieces principales', 'Surface terrain']
    Data['Date mutation'] = pd.to_datetime(Data['Date mutation'], format='%d/%m/%Y')
    Data['Code departement'] = Data['Code departement'].astype(str)
    Data = Data[columns_to_keep]
    Data = Data.dropna()
    Data['Valeur fonciere'] = pd.to_numeric(Data['Valeur fonciere'].str.replace(',', '.'))

    MUTATIONS = Data['Nature mutation'].unique()
    graphJSON = {}

    for mutation in MUTATIONS:
        graphJSON[mutation] = plotMutation(mutation, Data)

    return render_template('Widget.html', graphJSON=graphJSON)




@app.route('/2018/')
def data2017():
    return render_template('2018.html')

@app.route('/2019/')
def data2018():
    return render_template('2019.html')

@app.route('/2020/')
def data2019():
    return render_template('2020.html')

@app.route('/2021/')
def data2020():
    return render_template('2021.html')

@app.route('/2022/')
def data2021():
    return render_template('2022.html')

@app.route('/comparaison/')
def datacomp():
    return render_template('Comparaison.html')