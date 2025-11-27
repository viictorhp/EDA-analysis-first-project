# Funciones utilizadas en el segundo notebook (edaanalysis2) de visualización en gráficas y tablas.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# 1 - Tabla Frecuencia por país

def freq_country_table (df):
    country_table = df["country"].value_counts().reset_index()
    country_table.columns = ["country", "athlete_count"]
    country_table = country_table.sort_values(by="athlete_count", ascending=False).head(10)
    return country_table

# 2 - Gráfico frecuencia por país

def graph_country_table (df):
    country_table = freq_country_table(df)
    country_table.head(10).plot(
    x="country", 
    y="athlete_count", 
    kind="bar", 
    color="coral",
    legend=False)
    plt.xlabel("Country")
    plt.ylabel("Number of athletes")
    plt.title("Top 10 Countries by Athlete Count")
    plt.xticks(rotation=75)
    plt.show()