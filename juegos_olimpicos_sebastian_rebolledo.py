import pandas as pd
import numpy as np

df = pd.read_csv("athlete_events.csv")
# 1

ejercicio_1 = df.shape

# 2

ejercicio_2 = df.loc[:,"Games"].value_counts().shape

# 3


ejercicio_3 = [df.loc[:,"Season"].value_counts()["Summer"]/df.loc[:,"Season"].value_counts().sum(), 
df.loc[:,"Season"].value_counts()["Winter"]/df.loc[:,"Season"].value_counts().sum()]


# 4

fecha_primera_competencia = df.loc[:,"Year"].min()
season_summer = df[df["Season"]== "Summer"]
ejercicio_4 = season_summer[season_summer["Year"] == fecha_primera_competencia]["City"].unique() 


# 5

season_winter = df[df["Season"]=="Winter"]
fecha_primera_competencia_winter = season_winter.loc[:,"Year"].min()
ejercicio_5 = season_winter[season_winter["Year"]==fecha_primera_competencia_winter]["City"].unique()

# 6

ejercicio_6= df["Team"].value_counts().head(10)


# 7

gold = df[df["Medal"].isnull() == False].loc[:,"Medal"].value_counts()["Gold"]/df[df["Medal"].isnull() == False].shape[0]
silver = df[df["Medal"].isnull() == False].loc[:,"Medal"].value_counts()["Silver"]/df[df["Medal"].isnull() == False].shape[0]
bronze = df[df["Medal"].isnull() == False].loc[:,"Medal"].value_counts()["Bronze"]/df[df["Medal"].isnull() == False].shape[0]
ejercicio_7 = [gold, silver, bronze]


# 8

ejercicio_8 = df[df["Year"] == fecha_primera_competencia]["NOC"].unique()

##################################################################################################################################

#Desafio el caso de Chile

# 1

chile = df[df["Team"] == "Chile"]

# 2

chilenos_por_ano = chile["Year"].value_counts()

mayor_participacion_chilena = chile["Year"].value_counts().max()

# 3

nombres_chilenos_con_medalla = chile[chile["Medal"].isnull()==False]["Name"]

# 4
#No supe como obtener solo el año con mas medallas xC
anos_con_medallas = chile[chile["Medal"].isnull()==False]["Year"].value_counts()


###########################################################################################################################
###########################################################################################################################
#Juegos olimpicos V2

#1
medal_gold = df[df["Medal"] == "Gold"]
medal_silver = df[df["Medal"] == "Silver"]
medal_bronze = df[df["Medal"] == "Bronze"]
no_medal = df[df["Medal"].isnull() == True]

#2
df["Female"] = np.where(df["Sex"]== "F", 1, 0)
medal_gold = df[df["Medal"] == "Gold"]
medal_silver = df[df["Medal"] == "Silver"]
medal_bronze = df[df["Medal"] == "Bronze"]
no_medal = df[df["Medal"].isnull() == True]

#3

primeros_10_gold = medal_gold.loc[:,"Team"].value_counts().head(10)
primeros_10_silver = medal_silver.loc[:,"Team"].value_counts().head(10)
primeros_10_bronze = medal_bronze.loc[:,"Team"].value_counts().head(10)
primeros_10_no_medal = no_medal.loc[:,"Team"].value_counts().head(10)

men_and_female_gold = medal_gold.loc[:,"Sex"].value_counts()
men_and_female_silver = medal_silver.loc[:,"Sex"].value_counts()
men_and_female_bronze = medal_bronze.loc[:,"Sex"].value_counts()
men_and_female_no_medal = no_medal.loc[:,"Sex"].value_counts()

# 4 
mens_and_female_gold = medal_gold.loc[:,"Sex"].value_counts()
mens_and_female_silver = medal_silver.loc[:,"Sex"].value_counts()
mens_and_female_bronze = medal_bronze.loc[:,"Sex"].value_counts()
mens_and_female_no_medal = no_medal.loc[:,"Sex"].value_counts()

# 5
def medias(df,analyze,gender="Female"):
    subset= df[df[analyze].isnull() == False]
    media_hombres = subset[subset[gender]==0].loc[:,analyze].sum()/len(subset[subset[gender]==0].loc[:,analyze])
    media_mujeres = subset[subset[gender]==1].loc[:,analyze].sum()/len(subset[subset[gender]==1].loc[:,analyze])
    return [media_hombres,media_mujeres]

# 6
medias(medal_gold,"Height")
medias(medal_gold,"Weight")

medias(medal_silver,"Height")
medias(medal_silver,"Weight")

medias(medal_bronze,"Height")
medias(medal_bronze,"Weight")

medias(no_medal,"Height")
medias(no_medal,"Weight")