import streamlit as st
import plotly.express as px
import pandas as pd

co2_path = "data/CO2_per_capita.csv"
co2_df = pd.read_csv(co2_path, sep=";")
co2_df.dropna(inplace=True, axis=0)
def top_n_emitters(df, start_year=2008, end_year=2011, nb_displayed=10):    
    #years filter
    df_filtre = df[(df["Year"]>=start_year) & (df["Year"] <= end_year)]
    #do the mean for each country
    #sort the values and keep nb_displayed
    top_10_countries = df_filtre.groupby("Country Name")["CO2 Per Capita (metric tons)"].mean().sort_values(ascending = False)[:nb_displayed]
    #create the fig
    #return the fig
    return top_10_countries

st.title("Consommation de CO2 pour les n pays les plus consommateurs")
st.write('Welcome to my first Streamlit app!')

start_year = st.select_slider("Choisis l'année de départ"
                 ,options=sorted(co2_df["Year"].unique()))
end_year = st.select_slider("Choisis l'année de fin"
                 ,options=sorted(co2_df["Year"].unique()))
nb_countries = st.select_slider("Choisis le nombre de pays"
                                ,options=[3,5,10,20,30])

top_n_countries = top_n_emitters(co2_df, start_year, end_year, nb_countries)
fig = px.histogram(data_frame = top_n_countries,x=top_n_countries.index,
              y=top_n_countries)
st.plotly_chart(fig)

fig2 = px.scatter_geo(data_frame=co2_df, locations="Country Code",
                      size ="CO2 Per Capita (metric tons)",
                      hover_name="CO2 Per Capita (metric tons)")
st.plotly_chart(fig2)

if st.button("Cliquez ici pour une surprise !"):
    st.snow()