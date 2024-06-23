import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

city_names = [
    "Bangkok", "Paris", "London", "Dubai", "Singapore", "Kuala Lumpur",
    "New York City", "Istanbul", "Tokyo", "Seoul", "Antalya", "Phuket",
    "Mecca", "Hong Kong", "Milan", "Palma de Mallorca", "Barcelona", 
    "Pattaya", "Osaka", "Vienna", "Rome", "Riyadh", "Guangzhou", "Taipei",
    "Medina", "Prague", "Shanghai", "Los Angeles", "Amsterdam", "Miami",
    "Las Vegas", "Denpasar", "Ho Chi Minh City", "Sydney", "Berlin",
    "Madrid", "Athens", "Moscow", "Cancún", "Orlando", "Toronto", "Beijing",
    "Lisbon", "Florence", "Dublin", "Saint Petersburg", "Brussels", "Jakarta",
    "Mexico City", "Rio de Janeiro", "Santiago", "Lima", "Bogota", "Caracas",
    "Montevideo", "Buenos Aires", "Hanoi",
    "Cairo", "Nairobi", "Cape Town", "Lagos", "Marrakech", "Tunis",
    "Algiers", "Harare", "Maputo", "Abidjan", "Dar es Salaam", "Addis Ababa",
    "Kampala", "Dakar", "Accra", "Luanda", "Bamako", "Freetown", "Kigali",
    "Kinshasa", "Libreville", "Lilongwe", "Windhoek", "Port Louis", 
    "Victoria, Seychelles", "Pretoria", "Lusaka", "Gaborone", "Nouakchott", 
    "Monrovia", "N'Djamena", "Mogadishu", "Djibouti City", "Malabo", 
    "São Tomé", "Praia", "Banjul", "Bissau", "Conakry", "Lomé", 
    "Ouagadougou", "Yaoundé", "Rabat"
]

african_cities = [
    "Cairo", "Nairobi", "Cape Town", "Lagos", "Marrakech", "Tunis",
    "Algiers", "Harare", "Maputo", "Abidjan", "Dar es Salaam", "Addis Ababa",
    "Kampala", "Dakar", "Accra", "Luanda", "Bamako", "Freetown", "Kigali",
    "Kinshasa", "Libreville", "Lilongwe", "Windhoek", "Port Louis", 
    "Victoria, Seychelles", "Pretoria", "Lusaka", "Gaborone", "Nouakchott", 
    "Monrovia", "N'Djamena", "Mogadishu", "Djibouti City", "Malabo", 
    "São Tomé", "Praia", "Banjul", "Bissau", "Conakry", "Lomé", 
    "Ouagadougou", "Yaoundé", "Rabat"
]

criteria = [
    "Cuisine",
    "Accessibility",
    "Cultural Experience",
    "Shopping",
    "Festivals and Events",
    "Natural Scenery",
    "Urban Scenery"
]

def see_corr(data):
    sample = data.select_dtypes(include='number')
    corr = sample.corr()
    mask = np.zeros_like(corr, dtype = np.bool_)
    mask[np.triu_indices_from(mask)] = True
    plt.figure(figsize=(10,10))
    sns.heatmap(corr, mask=mask)
    plt.show()

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

def main_func(data, fav_city):
    scaled = StandardScaler()
    sample = data.select_dtypes(include='number')
    scaled_data = scaled.fit_transform(sample)

    recommendations = NearestNeighbors(algorithm='kd_tree')
    recommendations.fit(scaled_data)
    df = pd.DataFrame(scaled_data, columns = criteria, index = city_names)
    

    value = df.iloc[df.index==fav_city].values.reshape(1,-1)
    distance, indice = recommendations.kneighbors(value,n_neighbors=99)#近い順で99のリスト（→最大）
    reco = df.index[indice[0]][1:].tolist()#delete name itself
    return reco

def take_only_africa(list):
    t = 0
    l= []
    for i in list:
        if i in african_cities:
            l.append(i)
            t += 1
        if t == 3:
            
            break
    return l


df = pd.read_csv('sightseeing_places_ratings.csv', index_col=0)
# see_corr(df)

list_of_reco = main_func(df, 'Accra')
list_of_reco_africa = take_only_africa(list_of_reco)
print(list_of_reco_africa)