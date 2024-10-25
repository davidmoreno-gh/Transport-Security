import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import geopandas as gpd

@st.cache


def load_data():
    data = pd.read_csv("df_final2.csv")
    #data['year'] = pd.to_datetime(data['year'], format='%Y')
    return data


def plot_choropleth(year):
    # Cargar los datos
    df_final2 = pd.read_csv('df_final2.csv', delimiter=',', thousands='.', decimal=',')
    url = 'https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/spain-communities.geojson'
    spain = gpd.read_file(url)

    # Crear un diccionario de mapeo para los nombres de las regiones
    mapping = {
    'Andalucia': 'Andalucía',
    'Aragon': 'Aragón',
    'Asturias': 'Asturias',
    'Cantabria': 'Cantabria',
    'Castilla-Leon': 'Castilla y León',
    'Castilla-La Mancha': 'Castilla-La Mancha',
    'Cataluña': 'Cataluña',
    'Ceuta': 'Ceuta',
    'Extremadura': 'Extremadura',
    'Galicia': 'Galicia',
    'Baleares': 'Islas Baleares',
    'Canarias': 'Canarias',
    'Madrid': 'Madrid',
    'Melilla': 'Melilla',
    'Murcia': 'Murcia',
    'Navarra': 'Navarra',
    'Pais Vasco': 'País Vasco',
    'Rioja': 'La Rioja',
    'Valencia': 'C. Valenciana'}

    # Reemplazar los valores en la columna 'name' del dataframe 'spain'
    spain['name'] = spain['name'].replace(mapping)
    
    # Filtrar los datos para el año seleccionado
    df_year = df_final2[df_final2['year'] == year]
    
    # Merge the geographical data with the accident rate data for the selected year
    spain_merged_year = spain.merge(df_year, left_on='name', right_on='region')
    
    # Seleccionar el año
    year = st.slider('Selecciona el año', min_value=int(df_final2['year'].min()), max_value=int(df_final2['year'].max()), step=1)

    # Create the choropleth map
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    
    spain_merged_year.plot(
        column='acc_victims_rate_per_100k',
        ax=ax,
        legend=True,
        legend_kwds={'label': 'Accidentes con Víctimas', 'orientation': 'horizontal'},
        cmap='YlOrRd',
        missing_kwds={'color': 'lightgrey'}
    )
    
    ax.axis('off')
    plt.title(f'Accidentes con Víctimas en {year}')
    return fig