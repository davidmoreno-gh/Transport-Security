import streamlit as st
from backend import load_data, plot_choropleth

def main():
    st.title('Mapa Coroplético de Accidentes con Víctimas en España')
 
    data = load_data()
    
    year = st.slider(
    'Selecciona el año',
    min_value=int(data['year'].min()),
    max_value=int(data['year'].max()),
    step=1,
    key="unique_year_slider")

    
    fig = plot_choropleth(year)
    st.pyplot(fig)  

if __name__ == '__main__':
    main()