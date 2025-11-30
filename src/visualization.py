## Funciones utilizadas en el segundo notebook (edaanalysis2) de visualización en gráficas y tablas. ##

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# 1 - Tabla frecuencia por país

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

# 3 - Heatmap país - año

def heatmap_country (df):
    country_table = df.groupby(["country","year"]).size().unstack().fillna(0)
    top_countries = country_table.sum(axis=1).sort_values(ascending=False).head(10).index
    sns.heatmap(country_table.loc[top_countries], annot=False, cmap="rocket",
        vmin=country_table.loc[top_countries].min().min(),
        vmax=country_table.loc[top_countries].quantile(0.9).max())
        # vmin y vmax controlan el rango de valores que se mapea a la escala de colores del heatmap
    plt.title("Participation by country and year (top 10)")
    plt.show()

# 4 - Tabla frecuencia por género

def gender_table (df):
    gender_table = df["gender"].value_counts().reset_index()
    gender_table.columns = ["gender", "athlete_count"]
    return gender_table

# 5 - Gráfico frecuencia por género

def graph_gender (df):
    df["gender"].value_counts().plot(kind="bar", color="skyblue")
    plt.xlabel("Gender")
    plt.ylabel("Number of athletes")
    plt.title("Distribution by Gender")
    plt.xticks(rotation=360)
    plt.show()

# 6 - Tabla frecuencia por rangos de edad

def age_table (df):
    age_table = pd.cut(df["age"], bins=[15,20,25,30,35,40,45,50,55], right=False).value_counts().sort_index().reset_index()
    # pd.cut(): Esta función de pandas divide los datos continuos (en este caso edades) en intervalos (bins).
    age_table.columns = ['age_range', 'athlete_count']
    return age_table

# 7 - Gráfico frecuencia por rangos de edad

def graph_age (df):
    df["age"].hist(bins=20, color="lightgreen")
    plt.xlabel("Age")
    plt.ylabel("Number of athletes")
    plt.title("Age Distribution")
    plt.show()

# 8 - Tabla análisis temporal

def temporary_table (df):
    year_table = df.groupby("year").size().reset_index(name="athlete_count")
    return year_table

# 9 - Gráfico análisis temporal

def graph_temporary (df):
    year_table = df.groupby("year").size().reset_index(name="athlete_count")
    year_table.plot (x="year",y="athlete_count",kind="bar",legend=False,color="steelblue")
    plt.xlabel("Year")
    plt.ylabel("Number of athletes")
    plt.title("Athletes per Year")
    plt.xticks(rotation=0)
    plt.show()

# 10 - Tabla número de atletas por año y país (Top 5 países)

def top5_table (df):
    country_table = df.groupby(["country", "year"]).size().reset_index(name = "athlete_count")
    top5_country = country_table.groupby("country")["athlete_count"].sum().sort_values(ascending=False).head(5).index
    return country_table[country_table["country"].isin(top5_country)]

# 11 - Gráfica número de atletas por año y país (Top 5 países)

def top5_graph (df):
    country_table = df.groupby(["country", "year"]).size().reset_index(name = "athlete_count")
    top5_country = country_table.groupby("country")["athlete_count"].sum().sort_values(ascending=False).head(5).index
    country_table_top5 = country_table[country_table["country"].isin(top5_country)]

    for country in top5_country:
        country_data = country_table_top5[country_table_top5["country"] == country]
        plt.plot(country_data["year"], country_data["athlete_count"], marker = "o", label=country)

    plt.xlabel("Year") 
    plt.ylabel("Number of athletes") 
    plt.title("Top 5 Countries - Athletes by Year")
    plt.legend()
    plt.show()

# 12 - Distribución de edad por año y género

def age_gender_distribution (df):
    sns.boxplot(data=df, x="year", y="age", hue="gender")
    plt.title("Age distribution by year and gender")
    plt.show()

# 13 - Evolución del número de atletas por año y género

def gender_year_evolution (df):
    tabla_gen = df.groupby(["year","gender"]).size().reset_index(name="athlete_count")
    tabla_gen.pivot(index="year", columns="gender", values="athlete_count").plot(kind="bar")
    plt.ylabel("Number of athletes")
    plt.title("Athletes by year and gender")
    plt.xticks(rotation=0)
    plt.show()

# 14 - Tabla análisis de rendimiento

def performance_table (df):
    result = {"masculino" : {}, "femenino": {}}
    for year in [2021,2022]:
        df_games = df[(df["competition"] == "games") & (df["year"] == year) & (~df["rank"].isna())] # Hago que se eviten los valores nulos
    
        # Tabla masculina
        top_rank_m = (df_games[df_games["gender"] == "M"].sort_values("rank").head(10))
        table_m = top_rank_m[["competitor_name", "country", "rank"]] 
        result["masculino"][year] = table_m

        # Tabla femenina
        top_rank_f = (df_games[df_games["gender"] == "F"].sort_values("rank").head(10))
        table_f = top_rank_f[["competitor_name", "country", "rank"]] 
        result["femenino"][year] = table_f
    
    return result

# 15 - Gráfico top 10 atletas masculinos en Games - 2022

def top_m_games_2022 (df_male_2022):
    plt.figure(figsize=(8, 4))
    plt.bar(df_male_2022["competitor_name"], df_male_2022["rank"], color="blue")
    plt.xticks(rotation=45, ha="right")
    plt.gca().invert_yaxis()
    plt.ylabel("Ranking (lower is better)")
    plt.title(f"Top 10 Male Rank - Games 2022")
    plt.tight_layout()
    plt.show()

# 16 - Gráfico top 10 atletas femeninos en Games - 2022

def top_f_games_2022 (df_female_2022):
    plt.figure(figsize=(8, 4))
    plt.bar(df_female_2022["competitor_name"], df_female_2022["rank"], color="darkmagenta")
    plt.xticks(rotation=45, ha="right")
    plt.gca().invert_yaxis()
    plt.ylabel("Ranking (lower is better)")
    plt.title(f"Top 10 Female Rank - Games 2022")
    plt.tight_layout()
    plt.show()

# 17 - Tabla top atletas en Open 2023

def top_open_2023_table (df):
    df_open_2023 = df[(df["competition"] == "open") & (df["year"] == 2023) & (~df["rank"].isna())]

    top_open_athletes_m = df_open_2023[df_open_2023["gender"] == "M"].sort_values("rank").head(10)
    top_rank_open_m = top_open_athletes_m[["competitor_name", "country", "gender", "rank", "height_cm", "weight_kg"]]

    top_open_athletes_f = df_open_2023[df_open_2023["gender"] == "F"].sort_values("rank").head(10)
    top_rank_open_f = top_open_athletes_f[["competitor_name", "country", "gender", "rank", "height_cm", "weight_kg"]]

    return top_rank_open_m, top_rank_open_f

# 18 - Gráfico relación altura/rendimiento para atletas en Open 2023 masculino

def height_vs_rank_m (df):
    df_open_2023 = df[(df["competition"] == "open") & (df["year"] == 2023) & (~df["rank"].isna())]
    top_100 = df_open_2023[df_open_2023["rank"].between(1, 100) & (df_open_2023["gender"] == "M")]
    
    plt.scatter(top_100["height_cm"], top_100["rank"], color="steelblue") 
    plt.xlabel("Height (cm)")
    plt.ylabel("Ranking (lower is better)")
    plt.title("Height vs. Rank - Top Open Athletes 2023")
    plt.gca().invert_yaxis()  # Mejor ranking arriba
    plt.show()

# 19 - Gráfico relación altura/rendimiento para atletas en Open 2023 femenino

def height_vs_rank_f (df):
    df_open_2023 = df[(df["competition"] == "open") & (df["year"] == 2023) & (~df["rank"].isna())]
    top_100 = df_open_2023[df_open_2023["rank"].between(1, 100) & (df_open_2023["gender"] == "F")]
    
    plt.scatter(top_100["height_cm"], top_100["rank"], color="deeppink") 
    plt.xlabel("Height (cm)")
    plt.ylabel("Ranking (lower is better)")
    plt.title("Height vs. Rank - Top Open Athletes 2023")
    plt.gca().invert_yaxis()  # Mejor ranking arriba
    plt.show()

# 20 - Gráfico relación peso/rendimiento para atletas en Open 2023 masculino

def weight_vs_rank_m (df):
    df_open_2023 = df[(df["competition"] == "open") & (df["year"] == 2023) & (~df["rank"].isna())]
    top_100 = df_open_2023[df_open_2023["rank"].between(1, 100) & (df_open_2023["gender"] == "M")]
    
    plt.scatter(top_100["weight_kg"], top_100["rank"], color="steelblue") 
    plt.xlabel("Weight (kg)")
    plt.ylabel("Ranking (lower is better)")
    plt.title("Weight vs. Rank - Top Open Athletes 2023")
    plt.gca().invert_yaxis()  # Mejor ranking arriba
    plt.show()

# 21 - Gráfico relación peso/rendimiento para atletas en Open 2023 femenino

def weight_vs_rank_f (df):
    df_open_2023 = df[(df["competition"] == "open") & (df["year"] == 2023) & (~df["rank"].isna())]
    top_100 = df_open_2023[df_open_2023["rank"].between(1, 100) & (df_open_2023["gender"] == "F")]
    
    plt.scatter(top_100["weight_kg"], top_100["rank"], color="deeppink") 
    plt.xlabel("Weight (kg)")
    plt.ylabel("Ranking (lower is better)")
    plt.title("Weight vs. Rank - Top Open Athletes 2023")
    plt.gca().invert_yaxis()  # Mejor ranking arriba
    plt.show()

# 22 - Gráfico relación edad/rendimiento para atletas en open 2023 (masculino y femenino)

def age_vs_rank (df):
    df_open_2023 = df[(df["competition"]=="open") & (df["year"]==2023)]
    top_100 = df_open_2023.sort_values("rank").head(100)
    colors = {"M":"steelblue","F":"deeppink"}

    for g, sub in top_100.groupby("gender"):
        plt.scatter(sub["age"], sub["rank"], c=colors[g], label=g, alpha=0.7)

    plt.gca().invert_yaxis()
    plt.xlabel("Age")
    plt.ylabel("Ranking (lower is better)")
    plt.title("Age vs Rank - Top 100 Open 2023")
    plt.legend()
    plt.show()
