# _*_ coding:utf-8 _*_
# @author Robert Carlos                                 #
# email robert.carlos@linuxmail.org                     #
# 2019-Mar (CC BY 3.0 BR)                               #

# Insira este código no seu Jupyter Notebook e salve no mesmo
# no mesmo diretório dos arquivos br_states.json e taxa_desemprego_br.csv


import json

import pandas as pd

import folium
from branca.colormap import linear

# carrega os arquivos
br_estados = 'br_states.json'
geo_json_data = json.load(open(br_estados))

esemprego_br = pd.read_csv('taxa_desemprego_br.csv', sep=';',
                           decimal=',', usecols=['Sigla', '4º trimestre 2018'])

# renomeia as colunas
desemprego_br.rename(columns={
    'Sigla': 'estado',
    '4º trimestre 2018': '2018'}, inplace=True)

colormap = linear.YlOrRd_09.scale(6, 20)

# converte o dataset para dicionário
desemprego_br_2018 = desemprego_br.set_index('estado')['2018']

# cria o mapa
mapa = folium.Map(
    width=600, height=400,
    location=[-15.77972, -47.92972],
    zoom_start=3
)

folium.GeoJson(
    geo_json_data,
    name='2018',
    style_function=lambda feature: {
        'fillColor': colormap(desemprego_br_2018[feature['id']]),
        'color': 'black',
        'weight': 0.3,
    }

).add_to(mapa)

colormap.caption = 'Taxa de desemprego no Brasil 2018'
colormap.add_to(mapa)

folium.LayerControl(collapsed=False).add_to(mapa)
mapa.save('taxa_br_2018.html')
mapa
