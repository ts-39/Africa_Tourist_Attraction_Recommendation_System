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

criteria = [
    "Cuisine",
    "Accessibility",
    "Cultural Experience",
    "Shopping",
    "Festivals and Events",
    "Natural Scenery",
    "Urban Scenery"
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

africa_city_urls = {
    'Cairo': 'https://www.tripadvisor.com/Tourism-g294201-Cairo_Cairo_Governorate-Vacations.html',
    'Nairobi': 'https://www.tripadvisor.com/Tourism-g294207-Nairobi-Vacations.html',
    'Cape Town': 'https://www.tripadvisor.com/Tourism-g1722390-Cape_Town_Western_Cape-Vacations.html',
    'Lagos': 'https://www.tripadvisor.com/Tourism-g304026-Lagos_Lagos_State-Vacations.html',
    'Marrakech': 'https://www.tripadvisor.com/Tourism-g293734-Marrakech_Marrakech_Safi-Vacations.html',
    'Tunis': 'https://www.tripadvisor.com/Tourism-g293758-Tunis_Tunis_Governorate-Vacations.html',
    'Algiers': 'https://www.tripadvisor.com/Tourism-g293718-Algiers_Algiers_Province-Vacations.html',
    'Harare': 'https://www.tripadvisor.com/Tourism-g293760-Harare_Harare_Province-Vacations.html',
    'Maputo': 'https://www.tripadvisor.com/Tourism-g293819-Maputo_Maputo_Province-Vacations.html',
    'Abidjan': 'https://www.tripadvisor.com/Tourism-g297513-Abidjan_Lagunes_Region-Vacations.html',
    'Dar es Salaam': 'https://www.tripadvisor.com/Tourism-g293748-Dar_es_Salaam_Dar_Es_Salaam_Region-Vacations.html',
    'Addis Ababa': 'https://www.tripadvisor.com/Tourism-g293791-Addis_Ababa-Vacations.html',
    'Kampala': 'https://www.tripadvisor.com/Tourism-g293841-Kampala_Central_Region-Vacations.html',
    'Dakar': 'https://www.tripadvisor.com/Tourism-g293831-Dakar_Dakar_Region-Vacations.html',
    'Accra': 'https://www.tripadvisor.com/Tourism-g293797-Accra_Greater_Accra-Vacations.html',
    'Luanda': 'https://www.tripadvisor.com/Tourism-g293763-Luanda_Luanda_Province-Vacations.html',
    'Bamako': 'https://www.tripadvisor.com/Tourism-g293813-Bamako-Vacations.html',
    'Freetown': 'https://www.tripadvisor.com/Tourism-g293833-Freetown_Western_Area-Vacations.html',
    'Kigali': 'https://www.tripadvisor.com/Tourism-g293829-Kigali_Kigali_Province-Vacations.html',
    'Kinshasa': 'https://www.tripadvisor.com/Tourism-g294187-Kinshasa-Vacations.html',
    'Libreville': 'https://www.tripadvisor.com/Tourism-g293793-Libreville_Estuaire_Province-Vacations.html',
    'Lilongwe': 'https://www.tripadvisor.com/Tourism-g293811-Lilongwe_Central_Region-Vacations.html',
    'Windhoek': 'https://www.tripadvisor.com/Tourism-g293821-Windhoek_Khomas_Region-Vacations.html',
    'Port Louis': 'https://www.tripadvisor.com/Tourism-g293817-Port_Louis-Vacations.html',
    'Victoria, Seychelles': 'https://www.tripadvisor.com/Tourism-g298572-Victoria_Mahe_Island-Vacations.html',
    'Pretoria': 'https://www.tripadvisor.com/Tourism-g312583-Pretoria_Gauteng-Vacations.html',
    'Lusaka': 'https://www.tripadvisor.com/Tourism-g293843-Lusaka_Lusaka_Province-Vacations.html',
    'Gaborone': 'https://www.tripadvisor.com/Tourism-g293767-Gaborone_South_East_District-Vacations.html',
    'Nouakchott': 'https://www.tripadvisor.com/Tourism-g293815-Nouakchott-Vacations.html',
    'Monrovia': 'https://www.tripadvisor.com/Tourism-g293805-Monrovia_Montserrado_County-Vacations.html',
    "N'Djamena": 'https://www.tripadvisor.com/Tourism-g293779-N_Djamena-Vacations.html',
    'Mogadishu': 'https://www.tripadvisor.com/Tourism-g294440-Mogadishu-Vacations.html',
    'Djibouti City': 'https://www.tripadvisor.com/Tourism-g293786-Djibouti-Vacations.html',
    'Malabo': 'https://www.tripadvisor.com/Tourism-g294438-Malabo_Bioko_Island-Vacations.html',
    'São Tomé': 'https://www.tripadvisor.com/Tourism-g480235-Sao_Tome_Island-Vacations.html',
    'Praia': 'https://www.tripadvisor.com/Tourism-g293775-Praia_Santiago-Vacations.html',
    'Banjul': 'https://www.tripadvisor.com/Tourism-g293795-Banjul_Banjul_Division-Vacations.html',
    'Bissau': 'https://www.tripadvisor.com/Tourism-g293801-Bissau-Vacations.html',
    'Conakry': 'https://www.tripadvisor.com/Tourism-g293799-Conakry_Conakry_Region-Vacations.html',
    'Lomé': 'https://www.tripadvisor.com/Tourism-g293839-Lome_Maritime_Region-Vacations.html',
    'Ouagadougou': 'https://www.tripadvisor.com/Tourism-g293769-Ouagadougou_Centre_Region-Vacations.html',
    'Yaoundé': 'https://www.tripadvisor.com/Tourism-g293773-Yaounde_Centre_Region-Vacations.html',
    'Rabat': 'https://www.tripadvisor.com/Tourism-g293736-Rabat_Rabat_Sale_Kenitra-Vacations.html'
}

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

def take_only_africa(list, n=3):
    t = 0
    l= []
    for i in list:
        if i in african_cities:
            l.append(i)
            t += 1
        if t == n:
            
            break
    return l


df = pd.read_csv('sightseeing_places_ratings.csv', index_col=0)
# see_corr(df)


import streamlit as st

st.title('Recommendation Sightseeing Places in Africa')

name = st.selectbox('Choose your most favorite city among these', city_names, index = None, placeholder="Choose an option")
# st.write(type(name))
number_of_places = st.number_input('How many recommended places you want to know', value = 3, max_value=30, step=1)
if name != None:
    st.write(f'Top {number_of_places} recommended cities in Africa')
    list_of_reco = main_func(df, name)
    list_of_reco_africa = take_only_africa(list_of_reco, n = number_of_places)
    for i, m in zip(list_of_reco_africa, range(number_of_places)):
        m += 1
        st.subheader(f"No.{m}")
        st.write(i)
        url = africa_city_urls[i]
        st.link_button(f'Go to Tripadvisor to explore {i}', url)
        st.text("")
        st.text("")
        st.text("----------------------------------------")


# print(list_of_reco_africa)
